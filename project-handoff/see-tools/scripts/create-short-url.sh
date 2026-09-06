#!/usr/bin/env bash
set -euo pipefail

TARGET_URL="${1:?target url required}"
DOMAIN="${2:-s.ee}"
CUSTOM_SLUG="${3:-}"

if [[ -z "${SEE_API_KEY:-}" ]]; then
  echo "SEE_API_KEY is not set." >&2
  exit 1
fi

PAYLOAD="{\"domain\":\"${DOMAIN}\",\"target_url\":\"${TARGET_URL}\""
if [[ -n "${CUSTOM_SLUG}" ]]; then
  PAYLOAD="${PAYLOAD},\"custom_slug\":\"${CUSTOM_SLUG}\""
fi
PAYLOAD="${PAYLOAD}}"

curl -sS \
  -X POST "https://s.ee/api/v1/shorten" \
  -H "Authorization: ${SEE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "${PAYLOAD}"
