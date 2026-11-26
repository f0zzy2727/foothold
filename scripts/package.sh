#!/bin/sh
# Build the file people upload to Claude: dist/foothold.plugin
# Runs the tests first and refuses to package if any fail.
set -e
cd "$(dirname "$0")/.."
python3 -m unittest discover -s tests
mkdir -p dist
rm -f dist/foothold.plugin
(cd plugins/foothold && zip -r -q ../../dist/foothold.plugin . -x "*.DS_Store" -x "*__pycache__*")
echo "Built dist/foothold.plugin, version $(python3 -c "import json;print(json.load(open('plugins/foothold/.claude-plugin/plugin.json'))['version'])")"
