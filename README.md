# Lamini documentation 🦙

## Links

* Docs: https://lamini-ai.github.io/
  * Code documentation and example snippets
* Website: https://www.lamini.ai/
  * Learn more about our product and check out our blog
* App: https://app.lamini.ai/
  * View your API key, training jobs, and chat playground
* Examples: https://github.com/lamini-ai/lamini-examples
  * Want the full pipeline? Our examples go step-by-step from inference to evaluation to fine tuning

## Launch local preview server

```
python -m venv .venv
source .venv/bin/activate
pip install mkdocs mkdocs-material mkdocs-redirects
npx embedme "docs/**/*.md"
mkdocs serve
```
