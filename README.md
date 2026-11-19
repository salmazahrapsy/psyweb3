# PsyWeb3

**Understanding human behaviour in decentralised communities.**

Research and education studio on trust, identity, participation and wellbeing in online and Web3 communities. Operated by PT Psyweb Tiga Indonesia. Founder: Salma Zahra.

Website: https://salmazahrapsy.github.io/psyweb3/

## How this repository works

- `build.py` generates the website into `site/` (Python standard library only).
- Every push to `main` runs `.github/workflows/pages.yml`: build → link check → secret scan → deploy to GitHub Pages. No manual publishing.
- Settings to fill in at the top of `build.py`: `SIGNUP_URL` (e.g. a Google Form) and `CONTACT_EMAIL`.

## First publish

From your computer, logged in to GitHub CLI as `salmazahrapsy`:

```bash
./deploy.sh
```

It creates the public repo `salmazahrapsy/psyweb3`, pushes, and switches Pages to GitHub Actions.

## Rules

- Every citation verified against its DOI or original page before it goes on the site.
- Label claims: Established / Web3 evidence / Perspective / Hypothesis.
- No customers, numbers, testimonials or partnerships that are not real.
- AI-drafted text is reviewed by Salma before it is published.
- Never commit tokens, passwords, private research data or interview notes. Private research stays in the private `psyweb3-research-lab` repo.

Content © PT Psyweb Tiga Indonesia. Code MIT.
