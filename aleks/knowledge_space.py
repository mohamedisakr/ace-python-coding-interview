import numpy as np
from collections import defaultdict
import networkx as nx
from typing import Dict, List, Set, Tuple


class KnowledgeSpace:
    def __init__(self, domain_name: str):
        """Initialize a knowledge space for a specific domain (e.g., 'Algebra 1')"""
        self.domain_name = domain_name
        self.knowledge_states = set()  # Set of all possible knowledge states
        self.prerequisites = defaultdict(set)  # Prerequisite relationships
        self.learning_paths = nx.DiGraph()  # Directed graph of learning paths

    def add_concept(self, concept: str, prerequisites: Set[str] = None):
        """Add a concept to the knowledge space with its prerequisites"""
        if prerequisites is None:
            prerequisites = set()
        self.prerequisites[concept] = prerequisites
        self.update_knowledge_states(concept)

    def update_knowledge_states(self, new_concept: str):
        """Update possible knowledge states when adding a new concept"""
        if not self.knowledge_states:
            self.knowledge_states.add(frozenset([new_concept]))
            return

        new_states = set()
        for state in self.knowledge_states:
            if self.prerequisites[new_concept].issubset(state):
                new_states.add(frozenset(state | {new_concept}))
        self.knowledge_states.update(new_states)
