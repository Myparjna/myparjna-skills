# Simplification Rules

Apply only rules that improve comprehension or reduce a verified defect risk in the frozen scope.

## Control flow

- Use guard clauses and early returns when they make preconditions visible.
- Flatten avoidable nesting; keep meaningful domain grouping.
- Replace nested ternaries and dense boolean expressions with named decisions or explicit branches.
- Prefer positive, intention-revealing conditions when they do not obscure the exceptional path.
- Do not replace a readable branch with a clever chain merely to remove lines.

## Names and structure

- Name data with nouns and actions with verbs.
- Prefer names that reveal intent and units over abbreviations or generic `data`, `result`, `tmp`, and `value`.
- Keep vocabulary consistent with the surrounding module and public API.
- Extract a function when it has a clear responsibility, a useful name, reuse, or an independently testable boundary—not because it exceeds an arbitrary line count.

## Duplication and abstraction

- Treat repetition as a lead, not a threshold: verify shared responsibility and compatible evolution before abstracting even three occurrences.
- Prefer data-driven tables when they make variation explicit and preserve order.
- Do not create a one-use utility, generic wrapper, speculative configuration, or framework layer.
- Keep helpful domain abstractions even when they add lines.

## Dead code and comments

- Delete code proven unused or unreachable; do not leave it commented out.
- Remove comments that only restate syntax.
- Keep comments that explain why, compatibility, invariants, security, operational constraints, or non-obvious tradeoffs.
- Do not remove TODO/FIXME items unless they are stale and evidence supports removal.

## Idioms

Use language and standard-library idioms conditionally. Check evaluation order, error propagation, allocation, mutation, ordering, and supported runtime before converting loops, matches, callbacks, comprehensions, iterator chains, or error handling.

## Anti-patterns

Do not:

- optimize for fewer lines or lower character count;
- introduce nested ternaries, dense one-liners, hidden coercion, or clever metaprogramming;
- convert sync to async or vice versa during cleanup;
- change imports, exports, public names, schemas, or error messages without authorization;
- mix formatting churn with semantic cleanup;
- broaden a local cleanup into architecture migration.

## Worked examples

Short ❌/✅ pairs that anchor the judgment boundaries. Adapt to the repository's language and existing style; never copy blindly.

### Guard clauses over nesting (control flow)

```ts
// ❌ Preconditions are buried inside nested branches
function discount(user: User | null, cart: Cart): number {
  if (user) {
    if (user.isMember) {
      if (cart.total > 100) {
        return cart.total * 0.1;
      }
    }
  }
  return 0;
}

// ✅ Each precondition is visible and testable on its own line
function discount(user: User | null, cart: Cart): number {
  if (!user?.isMember) return 0;
  if (!(cart.total > 100)) return 0;
  return cart.total * 0.1;
}
```

### Named decisions over nested ternaries (control flow)

```ts
// ❌ The policy is unreadable and cannot be breakpointed
const fee = isVip ? (amount > 1000 ? 0 : 5) : amount > 500 ? 10 : 15;

// ✅ The decision has a name and explicit branches
function serviceFee(isVip: boolean, amount: number): number {
  if (isVip) {
    return amount > 1000 ? 0 : 5;
  }
  return amount > 500 ? 10 : 15;
}
```

The negated comparison preserves the original result for `NaN`; `<= 100` would not.

### Shared responsibility over superficial duplication

```python
# Keep separate policies when they can evolve independently.
def price_usd(item):
    base = item.cost * 1.08
    return round(base, 2)

def price_eur(item):
    base = item.cost * 1.21
    return round(base, 2)

```

Three similar functions would still not prove one shared policy. If a common calculation is established, an internal helper may preserve these existing entrypoints; replacing them with `price(item, currency)` changes the public interface and introduces new failure cases.

### Delete, do not comment out (dead code)

```ts
// ❌ Commented-out code invites confusion about whether it still applies
// if (legacyMode) {
//   sendV1(payload);
// }
sendV2(payload);

// ✅ Delete it; version control remembers. If the reason for removal
// is non-obvious, keep a why-comment instead of the code.
// V1 transport was retired in v2.3; see migration notes.
sendV2(payload);
```
