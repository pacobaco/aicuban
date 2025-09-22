# aicuban-forming-workflow-tool

**Decision-point workflow engine for sequencing medical coding
procedures with CLI, API, and JSON-based workflow definitions.**

## Features

-   Model decision nodes and procedure nodes in JSON
-   Run workflows interactively via CLI or programmatically via Python
-   FastAPI API endpoint for remote automation
-   Unit tests included for core engine and I/O

## Quickstart

### 1. Setup

``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Example Workflow

Interactive mode:

``` bash
python -m aicuban.cli run workflows/example_workflow.json
```

Automated mode with pre-filled answers:

``` bash
python -m aicuban.cli run workflows/example_workflow.json --preanswers answers.json
```

`answers.json` example:

``` json
{
  "Is this an emergency case? (yes/no)": "no"
}
```

### 3. Run as API

``` bash
uvicorn aicuban.api:app --reload
```

Then POST to `/run` with JSON:

``` json
{
  "workflow_path": "workflows/example_workflow.json",
  "answers": {
    "Is this an emergency case? (yes/no)": "yes"
  }
}
```

### 4. Run Tests

``` bash
pytest tests/
```

## Roadmap

-   Add GUI front-end for visualizing workflows
-   Add CPT/ICD lookup service integration
-   Add cycle detection, validation, and audit logging

## License

Apache 2.0
