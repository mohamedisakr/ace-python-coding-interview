import numpy as np
from collections import defaultdict
import networkx as nx
from typing import Dict, List, Set, Tuple, Optional
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.cluster import KMeans, DBSCAN, SpectralClustering
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class AdvancedMLComponents:
    def __init__(self):
        # Enhanced prediction models
        self.success_predictor = GradientBoostingClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=3
        )
        self.concept_difficulty_predictor = RandomForestClassifier(n_estimators=100)
        
        # Multiple clustering methods
        self.clustering_methods = {
            'kmeans': KMeans(n_clusters=4),
            'dbscan': DBSCAN(eps=0.5, min_samples=5),
            'spectral': SpectralClustering(n_clusters=4),
            'gmm': GaussianMixture(n_components=4)
        }
        
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=2)
        self.pattern_detector = nx.DiGraph()
        
        # Track model performance
        self.model_metrics = defaultdict(list)
        
    def extract_advanced_features(self, student: 'StudentModel') -> np.ndarray:
        """Extract advanced features for ML models"""
        basic_features = student.get_features()
        
        # Calculate additional features
        time_based_features = [
            np.mean(student.completion_times.values()),  # Average completion time
            np.std(list(student.completion_times.values())) if student.completion_times else 0,
            len(student.review_history) / max(1, len(student.learning_history))  # Review ratio
        ]
        
        # Calculate concept difficulty features
        difficulty_features = [
            np.mean([student.attempt_counts[c] for c in student.known_concepts]) if student.known_concepts else 0,
            len(student.failed_attempts) / max(1, sum(student.attempt_counts.values()))  # Failure ratio
        ]
        
        # Calculate learning pattern features
        pattern_features = [
            len(student.learning_streaks) / max(1, len(student.learning_history)),  # Streak ratio
            student.get_learning_velocity(),  # Learning speed
            student.get_consistency_score()  # Performance consistency
        ]
        
        return np.concatenate([basic_features, time_based_features, difficulty_features, pattern_features])
    
    def predict_concept_difficulty(self, features: np.ndarray) -> float:
        """Predict difficulty level for a concept based on student features"""
        return self.concept_difficulty_predictor.predict_proba(features.reshape(1, -1))[0][1]
    
    def analyze_learning_patterns(self, learning_paths: List[List[str]]) -> Dict:
        """Enhanced pattern analysis of learning paths"""
        pattern_stats = defaultdict(int)
        sequence_patterns = defaultdict(list)
        
        for path in learning_paths:
            # Analyze transitions
            for i in range(len(path) - 1):
                transition = (path[i], path[i + 1])
                pattern_stats[transition] += 1
                
            # Analyze sequences of length 3
            for i in range(len(path) - 2):
                sequence = tuple(path[i:i+3])
                sequence_patterns[sequence].append(path)
        
        # Calculate pattern significance scores
        pattern_scores = {}
        total_paths = len(learning_paths)
        
        for pattern, occurrences in pattern_stats.items():
            support = occurrences / total_paths
            confidence = occurrences / max(1, sum(1 for p in learning_paths if p[0] == pattern[0]))
            pattern_scores[pattern] = (support, confidence)
            
        return {
            'transitions': pattern_stats,
            'sequences': sequence_patterns,
            'scores': pattern_scores
        }
    
    def visualize_learning_patterns(self, pattern_analysis: Dict):
        """Create visualizations for learning patterns"""
        # Create pattern graph
        G = nx.DiGraph()
        
        # Add edges with weights based on transition frequencies
        for (source, target), count in pattern_analysis['transitions'].items():
            G.add_edge(source, target, weight=count)
            
        # Create plot
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G)
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
        
        # Draw edges with varying thickness based on weight
        edges = G.edges()
        weights = [G[u][v]['weight'] for u, v in edges]
        nx.draw_networkx_edges(G, pos, width=[w/max(weights)*3 for w in weights])
        
        # Add labels
        nx.draw_networkx_labels(G, pos)
        
        plt.title("Learning Path Patterns")
        plt.axis('off')
        return plt.gcf()
    
    def visualize_clusters(self, features: np.ndarray, labels: np.ndarray):
        """Create visualization for student clusters"""
        # Reduce dimensionality for visualization
        features_2d = self.pca.fit_transform(self.scaler.fit_transform(features))
        
        # Create plot
        plt.figure(figsize=(10, 8))
        scatter = plt.scatter(features_2d[:, 0], features_2d[:, 1], 
                            c=labels, cmap='viridis')
        plt.colorbar(scatter)
        
        plt.title("Student Clusters")
        plt.xlabel("First Principal Component")
        plt.ylabel("Second Principal Component")
        return plt.gcf()
    
    def visualize_performance_metrics(self, metrics: Dict[str, List]):
        """Create visualization for performance metrics"""
        plt.figure(figsize=(15, 5))
        
        # Plot metrics over time
        for metric_name, values in metrics.items():
            plt.plot(values, label=metric_name)
            
        plt.title("Performance Metrics Over Time")
        plt.xlabel("Time")
        plt.ylabel("Score")
        plt.legend()
        return plt.gcf()

class EnhancedStudentModel(StudentModel):
    def __init__(self, student_id: str, knowledge_space: KnowledgeSpace):
        super().__init__(student_id, knowledge_space)
        self.completion_times = defaultdict(float)
        self.review_history = []
        self.failed_attempts = set()
        self.learning_streaks = []
        self.current_streak = 0
        self.last_activity_time = None
        
    def assess_knowledge(self, concept: str, performance: float, completion_time: float):
        """Enhanced assessment with additional metrics"""
        super().assess_knowledge(concept, performance)
        
        # Track completion time
        self.completion_times[concept] = completion_time
        
        # Track streaks
        if performance >= 0.8:
            self.current_streak += 1
        else:
            if self.current_streak > 0:
                self.learning_streaks.append(self.current_streak)
            self.current_streak = 0
            self.failed_attempts.add(concept)
            
        # Update activity time
        current_time = datetime.now()
        if self.last_activity_time:
            time_diff = (current_time - self.last_activity_time).total_seconds()
            if time_diff > 86400:  # More than 24 hours
                self.current_streak = 0
        self.last_activity_time = current_time
        
    def get_learning_velocity(self) -> float:
        """Calculate learning velocity based on concept acquisition rate"""
        if not self.learning_history:
            return 0.0
        
        time_diffs = []
        for i in range(1, len(self.learning_history)):
            time_diff = (self.learning_history[i][1] - self.learning_history[i-1][1]).total_seconds()
            time_diffs.append(time_diff)
            
        return len(self.learning_history) / (max(1, sum(time_diffs)))
    
    def get_consistency_score(self) -> float:
        """Calculate consistency score based on performance variation"""
        if not self.confidence_scores:
            return 0.0
            
        scores = list(self.confidence_scores.values())
        return 1.0 - np.std(scores) / max(1, np.mean(scores))

class EnhancedAdaptiveLearningSystem(AdaptiveLearningSystem):
    def __init__(self):
        super().__init__()
        self.ml_components = AdvancedMLComponents()
        
    def generate_insights_report(self, student_id: str) -> Dict:
        """Generate comprehensive insights report for a student"""
        student = self.student_models[student_id]
        features = self.ml_components.extract_advanced_features(student)
        
        return {
            'success_probability': self.ml_components.predict_success(features),
            'learning_velocity': student.get_learning_velocity(),
            'consistency_score': student.get_consistency_score(),
            'concept_difficulties': {
                concept: self.ml_components.predict_concept_difficulty(features)
                for concept in student.knowledge_space.prerequisites
            },
            'recommended_path': self.update_learning_path(student_id),
            'cluster_assignment': self.analyze_student_behaviors()[student_id],
            'performance_trends': {
                'average_score': np.mean(list(student.confidence_scores.values())),
                'improvement_rate': self.calculate_improvement_rate(student),
                'mastery_speed': len(student.known_concepts) / max(1, len(student.learning_history))
            }
        }
    
    def visualize_student_progress(self, student_id: str):
        """Create comprehensive visualization of student progress"""
        student = self.student_models[student_id]
        
        # Create figure with subplots
        fig = plt.figure(figsize=(20, 15))
        
        # Performance over time
        ax1 = fig.add_subplot(221)
        scores = [score for _, score in student.learning_history]
        ax1.plot(scores)
        ax1.set_title("Performance Over Time")
        ax1.set_ylabel("Score")
        
        # Concept mastery heatmap
        ax2 = fig.add_subplot(222)
        mastery_data = pd.DataFrame(student.confidence_scores.items(), 
                                  columns=['Concept', 'Score']).pivot_table(
                                      index='Concept', values='Score')
        sns.heatmap(mastery_data, ax=ax2, cmap='YlOrRd')
        ax2.set_title("Concept Mastery Heatmap")
        
        # Learning velocity
        ax3 = fig.add_subplot(223)
        velocity_data = [student.get_learning_velocity() for _ in range(len(student.learning_history))]
        ax3.plot(velocity_data)
        ax3.set_title("Learning Velocity")
        
        # Streak distribution
        ax4 = fig.add_subplot(224)
        ax4.hist(student.learning_streaks, bins=10)
        ax4.set_title("Learning Streak Distribution")
        
        plt.tight_layout()
        return fig

def demo_enhanced_system():
    system = EnhancedAdaptiveLearningSystem()
    algebra = system.create_domain("Algebra 1")
    
    # Add concepts
    algebra.add_concept("number_properties")
    algebra.add_concept("variables", {"number_properties"})
    algebra.add_concept("expressions", {"variables"})
    algebra.add_concept("equations", {"expressions"})
    
    # Simulate students with different learning patterns
    for i in range(20):
        student = system.add_student(f"student_{i}", "Algebra 1")
        
        # Simulate learning with varying patterns
        completion_time = np.random.uniform(5, 15)
        student.assess_knowledge("number_properties", 
                               np.random.uniform(0.8, 1.0),
                               completion_time)
                               
        completion_time = np.random.uniform(10, 20)
        student.assess_knowledge("variables",
                               np.random.uniform(0.7, 0.9),
                               completion_time)
                               
        completion_time = np.random.uniform(15, 25)
        student.assess_knowledge("expressions",
                               np.random.uniform(0.6, 0.8),
                               completion_time)
    
    # Generate insights and visualizations
    system.ml_components.train_success_predictor(
        np.array([system.ml_components.extract_advanced_features(s) 
                 for s in system.student_models.values()]),
        np.array([len(s.known_concepts) > 2 
                 for s in system.student_models.values()])
    )
    
    # Generate sample visualizations
    pattern_analysis = system.ml_components.analyze_learning_patterns(
        [[c for c, _ in s.learning_history] 
         for s in system.student_models.values()]
    )
    
    return system, pattern_analysis
