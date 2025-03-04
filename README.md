**Changes to the docs must be done in the `lamini-platform` repo. Any changes to the docs in this repo will be overwritten.**

# Lamini documentation 🦙

## Links

* Docs: <https://lamini-ai.github.io/>
  * Code documentation and example snippets
* Website: <https://www.lamini.ai/>
  * Learn more about our product and check out our blog
* App: <https://app.lamini.ai/>
  * View your API key, training jobs, and chat playground
* Examples: <https://github.com/lamini-ai/lamini-examples>
  * Want the full pipeline? Our examples go step-by-step from inference to evaluation to fine tuning

## Launch local preview server

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
npx embedme "docs/**/*.md"
mkdocs serve
```

## Add an analytics tracker

* Add tracker code to `overrides/partials/integrations/analytics/custom.html`
* Add any secret keys to Github secrets
* Pass the secrets to mkdocs by adding them here:
  * `.github/workflows/ci.yaml`
  * `mkdocs.yaml`
