#!/bin/bash
set -e

# Initialize git if not already a repo
git rev-parse --is-inside-work-tree 2>/dev/null || git init

# Remove existing origin if present, then add your GitHub repo
if git remote | grep -q '^origin$'; then
  git remote remove origin
fi
git remote add origin https://github.com/your-org/nexasphere-ura.git

git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
