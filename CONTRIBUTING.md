# Contributing

Thank you for contributing! Please follow these steps:

1. Fork the repo and create a branch for your change.
2. Add or update skill entries in `data/skills.json` following `docs/skill-template.md`.
3. Run the validation: `python -m json.tool data/skills.json`.
4. Run `python scripts/build-rankings.py` and `python scripts/build-search.py` locally.
5. Open a pull request with a clear description and examples.

See CODE_OF_CONDUCT.md for behavior guidelines.
