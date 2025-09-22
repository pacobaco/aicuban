import typer
from .io import load_workflow_from_json
from .engine import WorkflowEngine

app = typer.Typer()

class CLIResponder:
    def __init__(self, answers=None):
        self.answers = answers or {}
    def query(self, q):
        return self.answers.get(q) or typer.prompt(q)

@app.command()
def run(workflow: str):
    nodes, start = load_workflow_from_json(workflow)
    responder = CLIResponder()
    engine = WorkflowEngine(nodes, start)
    result = engine.run(responder)
    typer.echo(result)

if __name__ == '__main__':
    app()