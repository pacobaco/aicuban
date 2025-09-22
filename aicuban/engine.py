from typing import Dict
from .models import Node

class WorkflowEngine:
    def __init__(self, nodes: Dict[str, Node], start_node: str):
        self.nodes = nodes
        self.start_node = start_node

    def run(self, responder):
        path, procedures = [], []
        current = self.start_node
        while current:
            node = self.nodes[current]
            path.append(node.id)
            if node.type == 'decision':
                answer = responder.query(node.decision.question)
                current = node.decision.outcomes.get(answer, node.decision.outcomes.get('default'))
            elif node.type == 'procedure':
                procedures.append(node.procedure.dict())
                current = None
            else:
                current = None
        return {'path': path, 'procedures': procedures}
