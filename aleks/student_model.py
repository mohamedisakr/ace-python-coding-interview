import numpy as np
from collections import defaultdict
import networkx as nx
from typing import Dict, List, Set, Tuple


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
