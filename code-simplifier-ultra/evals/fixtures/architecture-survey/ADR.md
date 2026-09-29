# Payment isolation

Keep the payment gateway interface even with one production implementation. It centralizes idempotent charging and isolates provider behavior. Its removal would expose provider policy to callers.
