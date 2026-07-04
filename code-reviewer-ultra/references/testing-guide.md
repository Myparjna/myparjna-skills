# Testing Guide

测试编写指南，来自 OpenAI Codex code-review-testing。

## 测试优先级

对于 agent/系统变更，优先级：
**集成测试 > 单元测试**

## 集成测试 vs 单元测试

### 何时用集成测试
- 改变 agent 逻辑的功能
- 状态机转换（start→update→stop）
- 并发逻辑（threading.Lock, Event, Thread）
- API 接口契约
- 端到端流程

### 何时用单元测试
- 纯函数逻辑
- 数据转换
- 工具函数
- 算法实现

## 必须测试的场景

### 改变 agent 逻辑的功能 MUST 添加集成测试

列出需要测试的主要逻辑变更和面向用户的行为：
- [ ] 新增的状态转换
- [ ] 新增的错误处理路径
- [ ] 并发场景
- [ ] 边界条件

## 测试编写规范

### 集成测试示例（FastAPI）

```python
from fastapi.testclient import TestClient

def test_motion_control_start_stop(client):
    """测试状态转换 start → stop"""
    # start
    resp = client.post("/api/motion_control", json={"action": "start"})
    assert resp.json()["success"] is True
    
    # stop
    resp = client.post("/api/motion_control", json={"action": "stop"})
    assert resp.json()["success"] is True

def test_motion_control_unknown_action(client):
    """测试非法 action"""
    resp = client.post("/api/motion_control", json={"action": "invalid"})
    assert resp.status_code == 400
    assert resp.json()["success"] is False

def test_system_status_position_none(client, mock_controller):
    """测试 read_position 返回 None 的边界"""
    mock_controller.read_position.return_value = None
    resp = client.get("/api/system_status")
    data = resp.json()["data"]
    assert data["ptz"]["position_readable"] is False
    assert data["ptz"]["position"] is None
```

### 单元测试示例

```python
import tempfile
from pathlib import Path
from app.logging_config import setup_logging

def test_setup_logging_idempotent():
    """测试重复调用不重复添加 handler"""
    setup_logging()
    handlers_count = len(logging.getLogger().handlers)
    
    setup_logging()  # 再次调用
    
    assert len(logging.getLogger().handlers) == handlers_count

def test_setup_logging_creates_file():
    """测试日志文件创建"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # monkeypatch LOGS_DIR
        ...
        setup_logging()
        assert Path(tmpdir, "app.log").exists()
```

## 测试规范

### MUST
- 单元测试放在专用测试文件（`*_test.py` / `*_tests.rs`）
- 用 `tempfile.TemporaryDirectory` 和 `monkeypatch` 模拟文件系统
- 测试边界条件：空值、零值、超大输入、None
- 测试错误路径
- 测试状态转换

### MUST NOT
- 在主实现中写仅测试函数（test-only functions）
- 测试实现细节而非行为
- 跳过错误路径测试

## 测试覆盖检查清单

- [ ] Happy path tested（正常流程）
- [ ] Error cases tested（错误路径）
- [ ] Edge cases tested（边界条件）
  - [ ] 空数组/空字符串
  - [ ] None/null
  - [ ] 零值
  - [ ] 超大输入
  - [ ] 非法输入
- [ ] State machine tested（状态机）
- [ ] Concurrency tested（并发）
- [ ] Integration tests present（集成测试）

## 现有 helpers 检查

编写测试前先检查：
- [ ] 是否有现有 test helpers？
- [ ] 是否有 fixture 可复用？
- [ ] 是否有 mock 工厂？

复用现有 helpers 让测试更精简可读。

## 测试缺失的严重程度

| 场景 | Severity |
|------|----------|
| 并发/状态机代码无测试 | **P0 / CRITICAL** |
| 核心业务逻辑无测试 | **P1 / HIGH** |
| 工具函数无测试 | **P2 / MEDIUM** |
| 简单 getter/setter 无测试 | **P3 / LOW** |
