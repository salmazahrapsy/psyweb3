#!/usr/bin/env bash
# One-time publish of PsyWeb3 to GitHub + GitHub Pages from Salma's own computer.
# Needs: git and GitHub CLI (https://cli.github.com), logged in as salmazahrapsy:  gh auth login
set -euo pipefail
OWNER=salmazahrapsy
REPO=psyweb3
cd "$(dirname "$0")"
[ "$(gh api user -q .login)" = "$OWNER" ] || { echo "Log in as $OWNER first: gh auth login"; exit 1; }
git init -q -b main 2>/dev/null || true
git add -A
git commit -q -m "Publish PsyWeb3 site" || true
if ! gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  gh repo create "$OWNER/$REPO" --public --description "PsyWeb3 - understanding human behaviour in decentralised communities" --homepage "https://$OWNER.github.io/$REPO/" --source . --remote origin --push
else
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$OWNER/$REPO.git"
  git push -u origin main
fi
# Turn on Pages with GitHub Actions as the source (ignore error if already on)
gh api -X POST "repos/$OWNER/$REPO/pages" -f build_type=workflow >/dev/null 2>&1 || \
gh api -X PUT  "repos/$OWNER/$REPO/pages" -f build_type=workflow >/dev/null 2>&1 || true
echo "Pushed. Watch the deploy: gh run watch -R $OWNER/$REPO"
echo "Site (live in ~2 minutes): https://$OWNER.github.io/$REPO/"
