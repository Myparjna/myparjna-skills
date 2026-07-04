# Common Issues

常见代码问题模式，来自 Jeffallan code-reviewer。

## N+1 Query Problem

```typescript
// N+1 queries - BAD
const posts = await Post.findAll();
for (const post of posts) {
  post.author = await User.findById(post.authorId); // N queries!
}

// Single query with join - GOOD
const posts = await Post.findAll({ include: [User] });

// Or batch load
const posts = await Post.findAll();
const authorIds = posts.map(p => p.authorId);
const authors = await User.findByIds(authorIds);
```

## Missing Error Handling

```typescript
// Unhandled rejection - BAD
const data = await fetch('/api/data').then(r => r.json());

// Proper error handling - GOOD
try {
  const response = await fetch('/api/data');
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }
  const data = await response.json();
} catch (error) {
  logger.error('Failed to fetch data', { error });
  throw new DataFetchError('Could not load data');
}
```

## Magic Numbers/Strings

```typescript
// Magic number - BAD
if (user.age >= 18) { ... }
setTimeout(fn, 86400000);

// Named constant - GOOD
const MINIMUM_AGE = 18;
const ONE_DAY_MS = 24 * 60 * 60 * 1000;

if (user.age >= MINIMUM_AGE) { ... }
setTimeout(fn, ONE_DAY_MS);
```

## Deep Nesting

```typescript
// Deep nesting - BAD
if (user) {
  if (user.isActive) {
    if (user.hasPermission) {
      doSomething();
    }
  }
}

// Early returns - GOOD
if (!user || !user.isActive || !user.hasPermission) {
  return;
}
doSomething();
```

## God Functions

```typescript
// Does too much - BAD
async function processOrder(order) {
  // validate
  // check inventory
  // process payment
  // send email
  // update database
  // log analytics
}

// Single responsibility - GOOD
async function processOrder(order) {
  await validateOrder(order);
  await reserveInventory(order);
  await chargePayment(order);
  await sendConfirmation(order);
}
```

## Mutable Shared State

```typescript
// Shared mutable - BAD
const config = { debug: false };
function setDebug(val) {
  config.debug = val; // 任何模块都能改
}

// Immutable - GOOD
const config = Object.freeze({ debug: false });
function withDebug(config, val) {
  return { ...config, debug: val };
}
```

## Blocking Calls in Async（async 中的阻塞调用）

```python
# BAD - 阻塞事件循环
@app.get("/api/status")
async def status():
    position = controller.read_position()  # 同步阻塞
    return {"position": position}

# GOOD - 放入线程池
@app.get("/api/status")
async def status():
    position = await asyncio.to_thread(controller.read_position)
    return {"position": position}
```

## Deprecated APIs（弃用的 API）

```python
# BAD - Python 3.10+ 弃用
loop = asyncio.get_event_loop()

# GOOD
loop = asyncio.get_running_loop()
# 或直接
await asyncio.to_thread(func, *args)
```

## Unbounded Resources（无限资源）

```python
# BAD - 无大小限制
config = data.get("config", {})  # 客户端可发超大 dict

# GOOD - 限制大小
class Request(BaseModel):
    config: dict = Field(default_factory=dict, max_items=50)
```

## Closure Capture of State（闭包捕获状态）

```python
# BAD - 注册时捕获，运行时替换失效
def register_routes(app):
    motion_locator = app.state.motion_locator  # 闭包捕获

    @app.get("/api/status")
    async def status():
        return motion_locator.get_status()  # 用旧引用

# GOOD - 每次请求动态获取
def register_routes(app):
    @app.get("/api/status")
    async def status(request: Request):
        return request.app.state.motion_locator.get_status()
```
