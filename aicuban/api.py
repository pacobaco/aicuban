from fastapi import FastAPI
from pydantic import BaseModel
from .io import load_workflow_from_json
from .engine import WorkflowEngine

app = FastAPI()

class RunRequest(BaseModel):
    workflow_path: str
    answers: dict = {}

@app.post("/run")
def run_workflow(req: RunRequest):
    nodes, start = load_workflow_from_json(req.workflow_path)
    class DictResponder:
        def __init__(self, answers): self.answers = answers
        def query(self, q): return self.answers.get(q, "default")
    result = WorkflowEngine(nodes, start).run(DictResponder(req.answers))
    return result
