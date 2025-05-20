# Data Generation

You can run the command below to generate training data for the memory experiment. It initiates multiple generators to generate data and saves the data to the output parquet file.  In addition, you can optionally register the dataset for the experiment in the experiment parquet file.

```sh
lamini generate \
--experiment-name <my_exp> \
--pipeline-yml <path_to_pipeline.yml> \
--seed-data-jsonl <path_to_seed_data.jsonl> \
--sqlite-file <path_to_db.sqlite> \
--output-parquet <path_to_res.parquet> \
--experiment-parquet <path_to_exp.parquet>
```

## Options

* `--experiment-name` (required) - name for the experiment
* `--pipeline-yml` (required) - path to pipeline config yml file
* `--seed-data-jsonl` (required) - path to seed data jsonl file
* `--sqlite-file` (required) - path to sqlite file
* `--output-parquet` (required) - path to save the generated data in parquet format
* `--experiment-parquet` (optional) - path to register the generated data for the experiment in parquet format

### Seed data jsonl

The seed data jsonl file should look like below. where each line contains three keys: `input`, `output`, and `glossary`.

* `input` - natural language description of the query
* `output` - SQL code for input
* `glossary` - a list of dicts where each `input` is a term and the corresponding `output` is the definition of the term.  **Note that the `glossary` value is the same in every line of the jsonl.**

```json
{"input": "find name from the highest ...",
  "output": "SELECT name FROM ...",
  "glossary": [
     {"input": "ABC", "output": "ABC means ..."},
     {"input": "BCD", "output": "BCD means ..."},
  ],
  "input": "find price ...",
  "output": "SELECT price FROM ...",
  "glossary": [
     {"input": "ABC", "output": "ABC means ..."},
     {"input": "BCD", "output": "BCD means ..."},
  ]
}
```
