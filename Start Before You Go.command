#!/bin/bash
cd "$(dirname "$0")" || exit 1
if /usr/bin/python3 -V >/dev/null 2>&1; then
  exec /usr/bin/python3 start.py
fi
echo 'Python 3 is needed for local playback. You can open index.html for individual camera links.'
read -r -p 'Press Return to close.'
