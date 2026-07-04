# Change Impact Analysis Guide

变更影响分析指南，来自 OpenAI Codex code-review。

## Breaking Changes（破坏性变更）

搜索外部集成接口中的破坏性变更。**不要找到一个就停止，要分析所有可能。**

### 检查范围

#### 1. App-server APIs（API 接口）
- [ ] 端点路径是否变化？（`/api/old` → `/api/new`）
- [ ] HTTP 方法是否变化？（GET → POST）
- [ ] 请求参数是否变化？（新增必填、删除、改类型）
- [ ] 响应结构是否变化？（字段重命名、删除、改类型）
- [ ] 错误码/错误消息是否变化？
- [ ] 认证机制是否变化？

#### 2. CLI Parameters（命令行参数）
- [ ] 参数名是否变化？
- [ ] 参数默认值是否变化？
- [ ] 必填参数是否新增？
- [ ] 参数格式是否变化？（`--flag` → `-f`）

#### 3. Configuration Loading（配置加载）
- [ ] 配置文件格式是否变化？（yaml → toml）
- [ ] 环境变量名是否变化？
- [ ] 配置字段名是否变化？
- [ ] 默认值是否变化？
- [ ] 配置必填项是否新增？

#### 4. Session/State Resume（会话恢复）
- [ ] 序列化格式是否变化？
- [ ] 数据结构是否变化？
- [ ] 版本号是否提升？
- [ ] 旧版本数据能否加载？

### 检查方法

```bash
# 查看 API 变更
git diff -- '**/api/**' '**/routes/**'

# 查看配置变更
git diff -- '**/config/**' '**/*.env*'

# 查看类型定义变更（影响 API 契约）
git diff -- '**/models/**' '**/types/**' '**/schemas/**'

# 查看序列化变更
git diff -- '**/serializers/**' '**/dto/**'
```

## Change Size（变更大小）

### 评估标准
- **机械性变更**（格式化、重命名）：< 800 行可接受
- **复杂逻辑变更**：< 500 行
- **超出标准**：必须说明能否拆分

### 拆分建议
如变更较大，回答：
1. 能否拆分为可评审的阶段？
2. 最小可上线的连贯阶段是什么？
3. 各阶段的依赖关系是什么？

```bash
# 统计变更行数
git diff --stat
git diff --shortstat
```

## State / Context Management（状态/上下文管理）

### 检查项

1. **No history rewrite（不能重写历史）**
   - 状态/上下文必须增量构建
   - 不能在运行时重置历史

2. **Cache-friendly（缓存友好）**
   - 避免频繁变更导致缓存未命中
   - 热路径的数据结构应稳定

3. **Bounded size（边界大小）**
   - 所有注入项必须有边界大小和硬上限
   - 不能有无限增长的集合

4. **No unbounded items（无无限项）**
   - 单项不超过 10K tokens（或等效负载）
   - 超过 1K tokens 的新项标记为 P0

5. **Closure capture（闭包捕获）**
   - 状态是否通过闭包捕获？
   - 运行时替换是否会导致引用失效？
   - 应动态从 `app.state` / `request.app.state` 获取

6. **Multi-instance（多实例）**
   - 多实例部署是否竞争同一资源？
   - 日志文件是否用 PID 区分？
   - 是否需要分布式锁？

7. **State serialization（状态序列化）**
   - 所有注入片段是否明确定义为结构体/类型？
   - 序列化/反序列化是否安全？
