# First, let's add necessary imports
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Optional
import os
import csv
from scipy import stats
import plotly.io as pio


class AdvancedVisualizationExport:
    """Enhanced visualization with export capabilities"""

    def __init__(self):
        self.color_palette = px.colors.qualitative.Set3
        self.export_path = "learning_analytics_exports"
        os.makedirs(self.export_path, exist_ok=True)

    def create_detailed_performance_dashboard(self, student: 'EnhancedStudentModel') -> go.Figure:
        """Create detailed interactive performance dashboard"""
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=(
                'Performance Timeline', 'Concept Mastery Heatmap',
                'Learning Velocity Trends', 'Time Distribution',
                'Performance by Concept Type', 'Learning Patterns'
            ),
            specs=[[{"type": "scatter"}, {"type": "heatmap"}],
                   [{"type": "scatter"}, {"type": "histogram"}],
                   [{"type": "bar"}, {"type": "scatter"}]]
        )

        # Performance Timeline with Moving Average
        scores = [score for _, score in student.learning_history]
        dates = [date for date, _ in student.learning_history]
        ma_window = 5
        moving_avg = pd.Series(scores).rolling(window=ma_window).mean()

        fig.add_trace(
            go.Scatter(x=dates, y=scores, mode='markers',
                       name='Performance', marker_color='blue'),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=dates, y=moving_avg, mode='lines',
                       name=f'{ma_window}-point Moving Average',
                       line=dict(color='red')),
            row=1, col=1
        )

        # Enhanced Concept Mastery Heatmap
        concepts = list(student.confidence_scores.keys())
        scores = list(student.confidence_scores.values())
        attempts = [student.attempt_counts[c] for c in concepts]

        fig.add_trace(
            go.Heatmap(
                z=[scores, attempts],
                x=concepts,
                y=['Mastery', 'Attempts'],
                colorscale='YlOrRd'
            ),
            row=1, col=2
        )

        # Learning Velocity with Trend
        velocity_data = [student.get_learning_velocity()
                         for _ in range(len(student.learning_history))]
        trend = np.polyfit(range(len(velocity_data)), velocity_data, 1)
        trend_line = np.poly1d(trend)(range(len(velocity_data)))

        fig.add_trace(
            go.Scatter(y=velocity_data, mode='lines+markers',
                       name='Learning Velocity'),
            row=2, col=1
        )
        fig.add_trace(
            go.Scatter(y=trend_line, mode='lines',
                       name='Velocity Trend',
                       line=dict(dash='dash')),
            row=2, col=1
        )

        # Enhanced Time Distribution
        completion_times = list(student.completion_times.values())
        fig.add_trace(
            go.Histogram(x=completion_times,
                         nbinsx=20,
                         name='Time Distribution'),
            row=2, col=2
        )

        # Performance by Concept Type
        concept_types = self._categorize_concepts(concepts)
        avg_performance = {}
        for ctype, concepts_list in concept_types.items():
            scores = [student.confidence_scores[c] for c in concepts_list]
            avg_performance[ctype] = np.mean(scores) if scores else 0

        fig.add_trace(
            go.Bar(x=list(avg_performance.keys()),
                   y=list(avg_performance.values()),
                   name='Performance by Type'),
            row=3, col=1
        )

        # Learning Patterns
        pattern_data = self._analyze_learning_patterns(student)
        fig.add_trace(
            go.Scatter(x=list(pattern_data.keys()),
                       y=list(pattern_data.values()),
                       mode='lines+markers',
                       name='Learning Patterns'),
            row=3, col=2
        )

        fig.update_layout(height=1200, showlegend=True,
                          title_text="Detailed Student Performance Analysis")
        return fig

    def _categorize_concepts(self, concepts: List[str]) -> Dict[str, List[str]]:
        """Categorize concepts by type"""
        categories = {
            'foundational': [],
            'intermediate': [],
            'advanced': []
        }

        for concept in concepts:
            if 'properties' in concept or 'variables' in concept:
                categories['foundational'].append(concept)
            elif 'equations' in concept or 'expressions' in concept:
                categories['intermediate'].append(concept)
            else:
                categories['advanced'].append(concept)

        return categories

    def _analyze_learning_patterns(self, student: 'EnhancedStudentModel') -> Dict[str, float]:
        """Analyze detailed learning patterns"""
        patterns = {
            'initial_performance': np.mean(
                [score for _, score in student.learning_history[:3]]
            ),
            'recent_performance': np.mean(
                [score for _, score in student.learning_history[-3:]]
            ),
            'improvement_rate': student.get_improvement_rate(),
            'consistency': student.get_consistency_score(),
            'mastery_speed': student.get_mastery_speed()
        }
        return patterns

    def export_visualizations(self,
                              student_id: str,
                              visualizations: Dict[str, go.Figure]):
        """Export visualizations in multiple formats"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        student_folder = os.path.join(
            self.export_path, f"student_{student_id}")
        os.makedirs(student_folder, exist_ok=True)

        for viz_name, fig in visualizations.items():
            # Export as HTML
            html_path = os.path.join(
                student_folder,
                f"{viz_name}_{timestamp}.html"
            )
            fig.write_html(html_path)

            # Export as PNG
            png_path = os.path.join(
                student_folder,
                f"{viz_name}_{timestamp}.png"
            )
            fig.write_image(png_path)

            # Export as JSON
            json_path = os.path.join(
                student_folder,
                f"{viz_name}_{timestamp}.json"
            )
            fig.write_json(json_path)


class AdvancedStudentProfiles:
    """Extended student profiles with detailed characteristics"""

    def __init__(self):
        self.profiles = {
            'accelerated_learner': {
                'performance_range': (0.90, 1.0),
                'time_range': (3, 8),
                'learning_style': 'quick_mastery',
                'characteristics': {
                    'retention_rate': 0.95,
                    'review_frequency': 'low',
                    'preferred_pace': 'very_fast'
                }
            },
            'fast_learner': {
                'performance_range': (0.85, 0.95),
                'time_range': (5, 10),
                'learning_style': 'steady_progress',
                'characteristics': {
                    'retention_rate': 0.90,
                    'review_frequency': 'moderate',
                    'preferred_pace': 'fast'
                }
            },
            'methodical_learner': {
                'performance_range': (0.75, 0.90),
                'time_range': (8, 15),
                'learning_style': 'thorough_understanding',
                'characteristics': {
                    'retention_rate': 0.85,
                    'review_frequency': 'high',
                    'preferred_pace': 'moderate'
                }
            },
            'steady_learner': {
                'performance_range': (0.70, 0.85),
                'time_range': (10, 18),
                'learning_style': 'consistent_practice',
                'characteristics': {
                    'retention_rate': 0.80,
                    'review_frequency': 'moderate',
                    'preferred_pace': 'steady'
                }
            },
            'struggling_learner': {
                'performance_range': (0.50, 0.75),
                'time_range': (15, 25),
                'learning_style': 'needs_support',
                'characteristics': {
                    'retention_rate': 0.70,
                    'review_frequency': 'very_high',
                    'preferred_pace': 'slow'
                }
            },
            'variable_learner': {
                'performance_range': (0.60, 0.90),
                'time_range': (8, 20),
                'learning_style': 'inconsistent',
                'characteristics': {
                    'retention_rate': 0.75,
                    'review_frequency': 'variable',
                    'preferred_pace': 'variable'
                }
            }
        }

    def get_profile_characteristics(self, profile_type: str) -> Dict:
        """Get detailed characteristics for a profile type"""
        return self.profiles.get(profile_type, {})

    def identify_student_profile(self, student: 'EnhancedStudentModel') -> str:
        """Identify the most matching profile for a student"""
        student_metrics = {
            'avg_performance': np.mean(list(student.confidence_scores.values())),
            'avg_time': np.mean(list(student.completion_times.values())),
            'consistency': student.get_consistency_score(),
            'review_frequency': len(student.review_history) / max(1, len(student.learning_history))
        }

        best_match = None
        best_score = float('-inf')

        for profile_name, profile_data in self.profiles.items():
            match_score = self._calculate_profile_match(
                student_metrics, profile_data
            )
            if match_score > best_score:
                best_score = match_score
                best_match = profile_name

        return best_match

    def _calculate_profile_match(self,
                                 student_metrics: Dict[str, float],
                                 profile_data: Dict) -> float:
        """Calculate how well a student matches a profile"""
        score = 0

        # Performance match
        if profile_data['performance_range'][0] <= student_metrics['avg_performance'] <= profile_data['performance_range'][1]:
            score += 1

        # Time match
        if profile_data['time_range'][0] <= student_metrics['avg_time'] <= profile_data['time_range'][1]:
            score += 1

        # Consistency match
        if (profile_data['learning_style'] == 'consistent_practice' and student_metrics['consistency'] > 0.8) or \
           (profile_data['learning_style'] == 'inconsistent' and student_metrics['consistency'] < 0.6):
            score += 1

        # Review frequency match
        if (profile_data['characteristics']['review_frequency'] == 'high' and student_metrics['review_frequency'] > 0.3) or \
           (profile_data['characteristics']['review_frequency'] == 'low' and student_metrics['review_frequency'] < 0.1):
            score += 1

        return score


class AdvancedAnalysisMetrics:
    """Sophisticated analysis metrics for learning assessment"""

    @staticmethod
    def calculate_learning_efficiency(student: 'EnhancedStudentModel') -> float:
        """Calculate learning efficiency score"""
        if not student.learning_history:
            return 0.0

        mastery_speed = len(student.known_concepts) / \
            max(1, sum(student.completion_times.values()))
        performance_quality = np.mean(list(student.confidence_scores.values()))

        return mastery_speed * performance_quality

    @staticmethod
    def calculate_knowledge_retention(student: 'EnhancedStudentModel') -> float:
        """Calculate knowledge retention rate"""
        if not student.review_history:
            return 0.0

        review_scores = [score for _, score in student.review_history]
        initial_scores = [student.learning_history[0][1]
                          for _ in review_scores]

        retention_rates = [review/initial for review,
                           initial in zip(review_scores, initial_scores)]
        return np.mean(retention_rates)

    @staticmethod
    def calculate_learning_stability(student: 'EnhancedStudentModel') -> float:
        """Calculate learning stability score"""
        if len(student.learning_history) < 2:
            return 0.0

        scores = [score for _, score in student.learning_history]
        return 1.0 - np.std(scores) / max(1, np.mean(scores))

    @staticmethod
    def calculate_concept_relationships(student: 'EnhancedStudentModel') -> Dict[str, float]:
        """Analyze relationships between concept performances"""
        relationships = {}

        for concept1 in student.confidence_scores:
            for concept2 in student.confidence_scores:
                if concept1 < concept2:
                    score1 = student.confidence_scores[concept1]
                    score2 = student.confidence_scores[concept2]
                    correlation = np.corrcoef([score1], [score2])[0, 1]
                    relationships[f"{concept1}-{concept2}"] = correlation

        return relationships

    @staticmethod
    def generate_advanced_metrics(student: 'EnhancedStudentModel') -> Dict[str, Any]:
        """Generate comprehensive set of advanced metrics"""
        metrics = {
            'efficiency': AdvancedAnalysisMetrics.calculate_learning_efficiency(student),
            'retention': AdvancedAnalysisMetrics.calculate_knowledge_retention(student),
            'stability': AdvancedAnalysisMetrics.calculate_learning_stability(student),
            'concept_relationships': AdvancedAnalysisMetrics.calculate_concept_relationships(student),
            'learning_velocity': student.get_learning_velocity(),
            'mastery_depth': np.mean([
                score for score in student.confidence_scores.values()
                if score >= 0.8
            ]),
            'learning_consistency': stats.variation([
                score for _, score in student.learning_history
            ]) if student.learning_history else 0,
            'review_effectiveness': np.mean([
                score for _, score in student.review_history
            ]) if student.review_history else 0
        }

        return metrics


class DataExporter:
    """Handle export of learning analytics data"""

    def __init__(self, base_path: str = "learning_analytics_exports"):
        self.base_path = base_path
        os.makedirs(base_path)
