import numpy as np
from collections import defaultdict
import networkx as nx
from typing import Dict, List, Set, Tuple
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pandas as pd

class KnowledgeSpace:
    # Previous implementation remains the same
    def __init__(self, domain_name: str):
        self.domain_name = domain_name
        self.knowledge_states = set()
        self.prerequisites = defaultdict(set)
        self.learning_paths = nx.DiGraph()
        
    def add_concept(self, concept: str, prerequisites: Set[str] = None):
        if prerequisites is None:
            prerequisites = set()
        self.prerequisites[concept] = prerequisites
        self.update_knowledge_states(concept)
        
    def update_knowledge_states(self, new_concept: str):
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
        self.student_id = student_id
        self.knowledge_space = knowledge_space
        self.known_concepts = set()
        self.confidence_scores = defaultdict(float)
        self.learning_history = []
        self.learning_rate = []  # Track speed of concept acquisition
        self.attempt_counts = defaultdict(int)  # Track number of attempts per concept
        
    def assess_knowledge(self, concept: str, performance: float):
        self.confidence_scores[concept] = performance
        self.attempt_counts[concept] += 1
        
        if performance >= 0.8:
            self.known_concepts.add(concept)
            self.learning_history.append((concept, performance))
            self.learning_rate.append(self.attempt_counts[concept])
            
    def get_features(self) -> np.ndarray:
        """Extract features for machine learning"""
        features = [
            len(self.known_concepts),  # Total concepts mastered
            np.mean(list(self.confidence_scores.values())),  # Average performance
            np.mean(self.learning_rate) if self.learning_rate else 0,  # Average learning speed
            len(self.learning_history) / max(1, sum(self.attempt_counts.values())),  # Success rate
            np.std(list(self.confidence_scores.values())) if self.confidence_scores else 0  # Performance consistency
        ]
        return np.array(features)

class MLComponents:
    def __init__(self):
        self.success_predictor = RandomForestClassifier(n_estimators=100)
        self.behavior_clusterer = KMeans(n_clusters=4)
        self.scaler = StandardScaler()
        self.pattern_detector = nx.DiGraph()
        
    def train_success_predictor(self, student_features: np.ndarray, success_labels: np.ndarray):
        """Train the success prediction model"""
        self.success_predictor.fit(student_features, success_labels)
        
    def predict_success(self, student_features: np.ndarray) -> float:
        """Predict probability of success for a student"""
        return self.success_predictor.predict_proba(student_features.reshape(1, -1))[0][1]
        
    def cluster_behaviors(self, student_features: np.ndarray) -> np.ndarray:
        """Cluster students based on learning behaviors"""
        scaled_features = self.scaler.fit_transform(student_features)
        return self.behavior_clusterer.fit_predict(scaled_features)
        
    def detect_patterns(self, learning_paths: List[List[str]]):
        """Detect common patterns in learning paths"""
        for path in learning_paths:
            for i in range(len(path) - 1):
                if not self.pattern_detector.has_edge(path[i], path[i + 1]):
                    self.pattern_detector.add_edge(path[i], path[i + 1], weight=1)
                else:
                    self.pattern_detector[path[i]][path[i + 1]]['weight'] += 1
                    
    def get_common_paths(self, start_concept: str, n_paths: int = 3) -> List[List[str]]:
        """Get most common learning paths from a starting concept"""
        paths = []
        for target in self.pattern_detector.nodes():
            if target != start_concept:
                try:
                    paths.extend(
                        nx.shortest_paths(self.pattern_detector, start_concept, target, weight='weight')
                    )
                except nx.NetworkXNoPath:
                    continue
        
        # Sort paths by total weight
        path_weights = []
        for path in paths:
            weight = sum(self.pattern_detector[path[i]][path[i + 1]]['weight'] 
                        for i in range(len(path) - 1))
            path_weights.append((path, weight))
            
        return [path for path, _ in sorted(path_weights, key=lambda x: -x[1])[:n_paths]]

class AdaptiveLearningSystem:
    def __init__(self):
        self.knowledge_spaces = {}
        self.student_models = {}
        self.performance_history = defaultdict(list)
        self.ml_components = MLComponents()
        
    def create_domain(self, domain_name: str) -> KnowledgeSpace:
        self.knowledge_spaces[domain_name] = KnowledgeSpace(domain_name)
        return self.knowledge_spaces[domain_name]
        
    def add_student(self, student_id: str, domain_name: str) -> StudentModel:
        if domain_name not in self.knowledge_spaces:
            raise ValueError(f"Domain {domain_name} does not exist")
        
        student = StudentModel(student_id, self.knowledge_spaces[domain_name])
        self.student_models[student_id] = student
        return student
        
    def update_learning_path(self, student_id: str) -> List[str]:
        student = self.student_models[student_id]
        ready_concepts = student.get_ready_to_learn()
        
        # Get student features for prediction
        features = student.get_features()
        
        # Predict success probability for each concept
        concept_scores = []
        for concept in ready_concepts:
            success_prob = self.ml_components.predict_success(features)
            prereq_count = len(student.knowledge_space.prerequisites[concept])
            avg_prereq_performance = np.mean([
                student.confidence_scores[p] 
                for p in student.knowledge_space.prerequisites[concept]
            ])
            concept_scores.append((concept, success_prob, prereq_count, avg_prereq_performance))
            
        # Sort by success probability, prerequisite performance, and complexity
        sorted_concepts = sorted(
            concept_scores,
            key=lambda x: (-x[1], -x[3], x[2])
        )
        return [concept for concept, _, _, _ in sorted_concepts]
    
    def analyze_student_behaviors(self):
        """Analyze and cluster student behaviors"""
        student_features = np.array([
            student.get_features() 
            for student in self.student_models.values()
        ])
        
        clusters = self.ml_components.cluster_behaviors(student_features)
        
        # Group students by cluster
        cluster_groups = defaultdict(list)
        for student_id, cluster in zip(self.student_models.keys(), clusters):
            cluster_groups[cluster].append(student_id)
            
        return cluster_groups
    
    def train_ml_components(self):
        """Train all machine learning components with current data"""
        # Prepare training data
        student_features = []
        success_labels = []
        learning_paths = []
        
        for student in self.student_models.values():
            student_features.append(student.get_features())
            success_labels.append(len(student.known_concepts) > 
                                len(student.knowledge_space.prerequisites) / 2)
            learning_paths.append([concept for concept, _ in student.learning_history])
            
        # Train success predictor
        self.ml_components.train_success_predictor(
            np.array(student_features), 
            np.array(success_labels)
        )
        
        # Detect learning path patterns
        self.ml_components.detect_patterns(learning_paths)

# Example usage
def demo_ml_components():
    system = AdaptiveLearningSystem()
    algebra = system.create_domain("Algebra 1")
    
    # Add concepts with prerequisites
    algebra.add_concept("number_properties")
    algebra.add_concept("variables", {"number_properties"})
    algebra.add_concept("expressions", {"variables"})
    algebra.add_concept("equations", {"expressions"})
    
    # Add some students and simulate their learning
    for i in range(10):
        student = system.add_student(f"student_{i}", "Algebra 1")
        
        # Simulate different learning patterns
        student.assess_knowledge("number_properties", np.random.uniform(0.8, 1.0))
        student.assess_knowledge("variables", np.random.uniform(0.7, 0.9))
        student.assess_knowledge("expressions", np.random.uniform(0.6, 0.8))
        
    # Train ML components
    system.train_ml_components()
    
    # Analyze student behaviors
    cluster_groups = system.analyze_student_behaviors()
    
    # Get common learning paths
    common_paths = system.ml_components.get_common_paths("number_properties")
    
    return system, cluster_groups, common_paths
