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

class StudentModel:
    def __init__(self, student_id: str, knowledge_space: KnowledgeSpace):
        """Initialize a student model within a knowledge space"""
        self.student_id = student_id
        self.knowledge_space = knowledge_space
        self.known_concepts = set()
        self.confidence_scores = defaultdict(float)
        self.learning_history = []
        
    def assess_knowledge(self, concept: str, performance: float):
        """Update student's knowledge state based on assessment performance"""
        self.confidence_scores[concept] = performance
        if performance >= 0.8:  # Threshold for concept mastery
            self.known_concepts.add(concept)
            self.learning_history.append((concept, performance))
            
    def get_ready_to_learn(self) -> List[str]:
        """Determine concepts the student is ready to learn next"""
        ready_concepts = []
        for concept in self.knowledge_space.prerequisites:
            if (concept not in self.known_concepts and 
                self.knowledge_space.prerequisites[concept].issubset(self.known_concepts)):
                ready_concepts.append(concept)
        return ready_concepts

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
            concept_scores.append((concept, prereq_count, avg_prereq_performance))
            
        # Sort by prerequisite performance and complexity
        sorted_concepts = sorted(
            concept_scores,
            key=lambda x: (-x[2], x[1])  # Higher performance first, then lower complexity
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
