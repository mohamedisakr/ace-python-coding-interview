# finance_tracker/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.CharField(max_length=200)
    date = models.DateField()
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='budgets')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-start_date']

# finance_tracker/serializers.py
from rest_framework import serializers
from .models import Category, Transaction, Budget

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class TransactionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'description', 'date', 'type', 'category', 'category_name']
        
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class BudgetSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    spent = serializers.SerializerMethodField()
    
    class Meta:
        model = Budget
        fields = ['id', 'category', 'category_name', 'amount', 'start_date', 'end_date', 'spent']
    
    def get_spent(self, obj):
        return Transaction.objects.filter(
            user=obj.user,
            category=obj.category,
            type='expense',
            date__range=[obj.start_date, obj.end_date]
        ).aggregate(total=models.Sum('amount'))['total'] or 0

# finance_tracker/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Category, Transaction, Budget
from .serializers import CategorySerializer, TransactionSerializer, BudgetSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        today = timezone.now().date()
        start_date = today.replace(day=1)
        end_date = (start_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        
        transactions = self.get_queryset().filter(date__range=[start_date, end_date])
        
        income = transactions.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
        expenses = transactions.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
        
        by_category = transactions.filter(type='expense').values(
            'category__name'
        ).annotate(total=Sum('amount'))
        
        return Response({
            'total_income': income,
            'total_expenses': expenses,
            'balance': income - expenses,
            'spending_by_category': by_category
        })

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def current(self, request):
        today = timezone.now().date()
        current_budgets = self.get_queryset().filter(
            start_date__lte=today,
            end_date__gte=today
        )
        serializer = self.get_serializer(current_budgets, many=True)
        return Response(serializer.data)

# finance_tracker/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TransactionViewSet, BudgetViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'budgets', BudgetViewSet, basename='budget')

urlpatterns = [
    path('', include(router.urls)),
]

# settings.py additions
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'corsheaders',
    'finance_tracker',
]

MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

# For development only
CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}