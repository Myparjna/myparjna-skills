# Security Checklist

详细的安全审计清单，基于 OWASP Top 10，来自 Anthropic code-reviewer。

## SQL Injection Prevention（SQL 注入防护）

### BAD
```python
# 字符串拼接 SQL
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
```

### GOOD
```python
# 参数化查询
cursor.execute("SELECT * FROM users WHERE id = %s", [user_id])

# ORM
user = User.objects.get(id=user_id)
```

## XSS Prevention（XSS 防护）

### BAD
```tsx
// 信任用户输入
<div dangerouslySetInnerHTML={{ __html: userInput }} />
```

### GOOD
```tsx
// 自动转义
<div>{userInput}</div>
```

## Hardcoded Secrets（硬编码密钥）

### BAD
```python
API_KEY = "sk-abc123..."
password = "admin123"
```

### GOOD
```python
import os
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY environment variable not set")
```

## Authentication/Authorization（认证授权）

### BAD
```python
@app.post("/api/motion_control")
async def control(request: Request):
    # 无认证
    ...
```

### GOOD
```python
from fastapi import Depends

async def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {settings.API_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.post("/api/motion_control", dependencies=[Depends(verify_token)])
async def control(request: Request):
    ...
```

## Input Validation（输入验证）

### BAD
```python
data = await request.json()
action = data.get("action", "status")  # 未校验
config = data.get("config", {})        # 未校验，直接透传
```

### GOOD
```python
from pydantic import BaseModel, Field
from typing import Literal

class MotionControlRequest(BaseModel):
    action: Literal["start", "stop", "update", "status"]
    config: dict = Field(default_factory=dict, max_items=50)

@app.post("/api/motion_control")
async def control(request: MotionControlRequest):
    ...
```

## Information Disclosure（信息泄露）

### BAD
```python
# 暴露内部实现细节
data = {
    "ptz": {
        "sdk_connected": controller.login_id != 0,
        "login_id": controller.login_id,  # 内部 SDK 句柄
        "rtsp_url": config.rtsp_url,       # 可能含密码
    }
}
```

### GOOD
```python
data = {
    "ptz": {
        "sdk_connected": controller.is_connected,  # 用 property
        # login_id 移除
        # rtsp_url 移除或脱敏
    }
}
```

## CSRF Protection（CSRF 防护）

状态变更操作必须有 CSRF token：
- 表单提交：使用 CSRF token
- API：使用 SameSite cookie 或 custom header

## OWASP Top 10 Checklist

1. **Injection** — SQL/NoSQL/OS/LDAP 注入
2. **Broken Authentication** — 弱认证、会话管理
3. **Sensitive Data Exposure** — 明文传输、存储
4. **XML External Entities (XXE)** — XML 解析
5. **Broken Access Control** — 权限校验缺失
6. **Security Misconfiguration** — 默认配置、错误信息泄露
7. **Cross-Site Scripting (XSS)** — 输出转义
8. **Insecure Deserialization** — 反序列化
9. **Using Components with Known Vulnerabilities** — 依赖漏洞
10. **Insufficient Logging & Monitoring** — 日志不足

## Dependency Security

```bash
# 检查依赖漏洞
npm audit          # Node.js
pip-audit          # Python
safety check       # Python
govulncheck ./...  # Go
```
