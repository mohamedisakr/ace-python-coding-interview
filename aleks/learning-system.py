import numpy as np
from collections import defaultdict
import networkx as nx
from typing import Dict, List, Set, Tuple
from adaptive_learning_system import AdaptiveLearningSystem

# Example usage for Algebra 1


def create_algebra_domain() -> AdaptiveLearningSystem:
    system = AdaptiveLearningSystem()
    algebra = system.create_domain("Algebra 1")

    # Define basic concepts and prerequisites
    algebra.add_concept("number_properties")
    algebra.add_concept("variables", {"number_properties"})
    algebra.add_concept("expressions", {"variables"})
    algebra.add_concept("equations", {"expressions"})
    algebra.add_concept("inequalities", {"equations"})
    algebra.add_concept("functions", {"equations"})
    algebra.add_concept("linear_equations", {"equations"})
    algebra.add_concept("quadratic_equations", {"linear_equations"})

    return system
