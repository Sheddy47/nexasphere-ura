#!/bin/bash
set -e

# Remove existing origin if it exists
git remote | grep -q '^origin$' && git remote remove origin

git remote add origin https://github.com/your-org/nexasphere-ura.git
git add .
git commit -m "feat: scaffold nexasphere-ura repo with core modules, tests, React components, CI, and docs"
