#!/usr/bin/env bash
set -euo pipefail

FILE_PATH="${1:?file path required}"

if [[ -z "${SEE_API_KEY:-}" ]]; then
  echo "SEE_API_KEY is not set." >&2
  exit 1
fi

if [[ ! -f "${FILE_PATH}" ]]; then
  echo "File not found: ${FILE_PATH}" >&2
  exit 1
fi

# Quote the filename for curl's multipart parser, not just for the shell.
FORM_PATH="${FILE_PATH//\\/\\\\}"
FORM_PATH="${FORM_PATH//\"/\\\"}"

curl --fail-with-body -sS --connect-timeout 10 --max-time 300 \
  -X POST "https://s.ee/api/v1/file/upload" \
  -H "Authorization: ${SEE_API_KEY}" \
  -F "file=@\"${FORM_PATH}\""
