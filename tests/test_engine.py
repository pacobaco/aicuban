from aicuban.models import Node, Decision, Procedure
from aicuban.engine import WorkflowEngine

class DummyResponder:
    def __init__(self, answers): self.answers = answers
    def query(self, q): return self.answers.get(q, "default")

def test_basic_flow():
    nodes = {
        "d1": Node(id="d1", type="decision",
                   decision=Decision(id="d1", question="Q1",
                                     outcomes={"a": "p1", "default": "p1"})),
        "p1": Node(id="p1", type="procedure",
                   procedure=Procedure(id="proc1", name="Proc 1",
                                       suggested_codes=["C1"]))
    }
    engine = WorkflowEngine(nodes, "d1")
    result = engine.run(DummyResponder({"Q1":"a"}))
    assert result["procedures"][0]["id"] == "proc1"
