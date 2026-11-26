#!/bin/sh
# Build the file people upload to Claude: dist/job-search.plugin
# Runs the tests first and refuses to package if any fail.
set -e
cd "$(dirname "$0")/.."
python3 -m unittest discover -s tests
mkdir -p dist
rm -f dist/job-search.plugin
(cd plugins/job-search && zip -r -q ../../dist/job-search.plugin . -x "*.DS_Store" -x "*__pycache__*")
echo "Built dist/job-search.plugin, version $(python3 -c "import json;print(json.load(open('plugins/job-search/.claude-plugin/plugin.json'))['version'])")"
