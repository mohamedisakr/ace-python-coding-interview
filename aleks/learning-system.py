import numpy as np
from collections import defaultdict
import networkx as nx
from typing import Dict, List, Set, Tuple


class AdaptiveLearningSystem:
    def __init__(self):
        """Initialize the adaptive learning system"""
        self.knowledge_spaces = {}
        self.student_models = {}
        self.performance_history = defaultdict(list)

    def create_domain(self, domain_name: str) -> KnowledgeSpace:
        """Create a new knowledge domain"""
        self.knowledge_spaces[domain_name] = KnowledgeSpace(domain_name)
        return self.knowledge_spaces[domain_name]

    def add_student(self, student_id: str, domain_name: str) -> StudentModel:
        """Add a new student to the system"""
        if domain_name not in self.knowledge_spaces:
            raise ValueError(f"Domain {domain_name} does not exist")

        student = StudentModel(student_id, self.knowledge_spaces[domain_name])
        self.student_models[student_id] = student
        return student

    def update_learning_path(self, student_id: str) -> List[str]:
        """Generate personalized learning path for a student"""
        student = self.student_models[student_id]
        ready_concepts = student.get_ready_to_learn()

        # Sort concepts by prerequisite complexity and historical performance patterns
        concept_scores = []
        for concept in ready_concepts:
            prereq_count = len(student.knowledge_space.prerequisites[concept])
            avg_prereq_performance = np.mean([
                student.confidence_scores[p]
                for p in student.knowledge_space.prerequisites[concept]
            ])
            concept_scores.append(
                (concept, prereq_count, avg_prereq_performance))

        # Sort by prerequisite performance and complexity
        sorted_concepts = sorted(
            concept_scores,
            # Higher performance first, then lower complexity
            key=lambda x: (-x[2], x[1])
        )
        return [concept for concept, _, _ in sorted_concepts]

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
