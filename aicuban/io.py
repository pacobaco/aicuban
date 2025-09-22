import json
from .models import Node, Decision, Procedure

def load_workflow_from_json(path):
    with open(path, 'r') as f:
        obj = json.load(f)
    start = obj['start']
    nodes = {n['id']: Node(**n) for n in obj['nodes']}
    return nodes, start
