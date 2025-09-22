import json, tempfile
from aicuban.io import save_workflow_to_json, load_workflow_from_json
from aicuban.models import Node, Procedure

def test_roundtrip():
    nodes = {"p": Node(id="p", type="procedure",
                       procedure=Procedure(id="p1", name="X", suggested_codes=["C1"]))}
    fd, path = tempfile.mkstemp(suffix=".json")
    save_workflow_to_json(nodes, "p", path)
    loaded, start = load_workflow_from_json(path)
    assert start == "p"
    assert loaded["p"].procedure.id == "p1"
