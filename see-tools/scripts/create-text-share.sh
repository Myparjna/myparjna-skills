#!/usr/bin/env bash
set -euo pipefail

TITLE="${1:?title required}"
CONTENT="${2:?content required}"
TEXT_TYPE="${3:-plain_text}"

if [[ -z "${SEE_API_KEY:-}" ]]; then
  echo "SEE_API_KEY is not set." >&2
  exit 1
fi

PAYLOAD=$(python - "$TITLE" "$CONTENT" "$TEXT_TYPE" <<'PY'
import json, sys
print(json.dumps(dict(title=sys.argv[1], content=sys.argv[2], text_type=sys.argv[3])))
PY
)

curl --fail-with-body -sS --connect-timeout 10 --max-time 60 \
  -X POST "https://s.ee/api/v1/text" \
  -H "Authorization: ${SEE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "${PAYLOAD}"
