#!/usr/bin/env bash
# Open a planning document for synchronous human review in a tmux popup,
# block until the editor closes, then verify an approval marker exists.
#
# Usage: review_in_popup.sh <file> <approval_pattern>
#   <file>             path to the file to review
#   <approval_pattern> grep -E pattern that the human must add for approval
#
# Exit codes:
#   0  approval pattern found (proceed past gate)
#   1  approval pattern not found (do not proceed)
#   2  not running inside tmux — caller must fall back to chat-based approval
#   3  usage error

set -euo pipefail

FILE="${1:-}"
PATTERN="${2:-}"

if [[ -z "$FILE" || -z "$PATTERN" ]]; then
  echo "usage: $0 <file> <approval_pattern>" >&2
  exit 3
fi

if [[ ! -f "$FILE" ]]; then
  echo "ERROR: file not found: $FILE" >&2
  exit 3
fi

if [[ -z "${TMUX:-}" ]]; then
  echo "ERROR: not running inside a tmux session." >&2
  echo "human-review-gate requires tmux for blocking review." >&2
  echo "Caller should fall back to chat-based approval." >&2
  exit 2
fi

# Open file in vim inside a blocking tmux popup.
#   -E              : close popup when command exits, propagate exit status.
#   -w 90% -h 90%   : nearly full-screen so reviewer sees the whole document.
#   +set ft=markdown: force markdown filetype regardless of detection.
#   +normal! gg     : jump to top of file on open.
tmux display-popup -E -w 90% -h 90% \
  "vim '+set ft=markdown' '+normal! gg' '$FILE'"

# After the popup closes, re-read the file and look for the approval marker.
if grep -qE "$PATTERN" "$FILE"; then
  echo "✓ approval marker matched: /$PATTERN/"
  exit 0
fi

echo "✗ approval marker not found in $FILE." >&2
echo "Pattern: /$PATTERN/" >&2
exit 1
