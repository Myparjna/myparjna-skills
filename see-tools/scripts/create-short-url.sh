#!/usr/bin/env bash
set -euo pipefail

TARGET_URL="${1:?target url required}"
DOMAIN="${2:-s.ee}"
CUSTOM_SLUG="${3:-}"

if [[ -z "${SEE_API_KEY:-}" ]]; then
  echo "SEE_API_KEY is not set." >&2
  exit 1
fi

PAYLOAD=$(python - "$DOMAIN" "$TARGET_URL" "$CUSTOM_SLUG" <<'PY'
import json, sys
body = dict(domain=sys.argv[1], target_url=sys.argv[2])
if sys.argv[3]:
    body['custom_slug'] = sys.argv[3]
print(json.dumps(body))
PY
)

curl --fail-with-body -sS --connect-timeout 10 --max-time 60 \
  -X POST "https://s.ee/api/v1/shorten" \
  -H "Authorization: ${SEE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "${PAYLOAD}"
