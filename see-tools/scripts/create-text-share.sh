#!/usr/bin/env bash
set -euo pipefail

TITLE="${1:?title required}"
CONTENT="${2:?content required}"
TEXT_TYPE="${3:-plain_text}"

if [[ -z "${SEE_API_KEY:-}" ]]; then
  echo "SEE_API_KEY is not set." >&2
  exit 1
fi

curl -sS \
  -X POST "https://s.ee/api/v1/text" \
  -H "Authorization: ${SEE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"${TITLE}\",\"content\":\"${CONTENT}\",\"text_type\":\"${TEXT_TYPE}\"}"
