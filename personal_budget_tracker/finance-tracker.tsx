import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { PieChart, Pie, Cell, ResponsiveContainer, Legend } from 'recharts';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { CreditCard, LineChart, DollarSign, BarChart } from 'lucide-react';

const API_BASE_URL = 'http://localhost:8000/api';

const FinanceTracker = () => {
  const [transactions, setTransactions] = useState([]);
  const [budgets, setBudgets] = useState([]);
  const [summary, setSummary] = useState({
    total_income: 0,
    total_expenses: 0,
    balance: 0,
    spending_by_category: []
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch transactions
        const transResponse = await fetch(`${API_BASE_URL}/transactions/`);
        const transData = await transResponse.json();
        setTransactions(transData);

        // Fetch current budgets
        const budgetResponse = await fetch(`${API_BASE_URL}/budgets/current/`);
        const budgetData = await budgetResponse.json();
        setBudgets(budgetData);

        // Fetch financial summary
        const summaryResponse = await fetch(`${API_BASE_URL}/transactions/summary/`);
        const summaryData = await summaryResponse.json();
        setSummary(summaryData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const CHART_COLORS = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'];

  return (
    <div className="w-full max-w-6xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Personal Finance Tracker</h1>
      
      {/* Overview Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Total Balance</CardTitle>
            <CreditCard className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">${summary.balance.toFixed(2)}</div>
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Monthly Income</CardTitle>
            <LineChart className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-green-600">
              ${summary.total_income.toFixed(2)}
            </div>
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Monthly Expenses</CardTitle>
            <DollarSign className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-red-600">
              ${summary.total_expenses.toFixed(2)}
            </div>
          </CardContent>
        </Card>
      </div>

      <Tabs defaultValue="overview" className="space-y-4">
        <TabsList>
          <TabsTrigger value="overview">Overview</TabsTrigger>
          <TabsTrigger value="transactions">Transactions</TabsTrigger>
          <TabsTrigger value="budgets">Budgets</TabsTrigger>
        </TabsList>

        <TabsContent value="overview" className="space-y-4">
          <Card>
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle>Spending Breakdown</CardTitle>
                <BarChart className="h-4 w-4 text-muted-foreground" />
              </div>
            </CardHeader>
            <CardContent className="h-80">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={summary.spending_by_category}
                    cx="50%"
                    cy="50%"
                    innerRadius={60}
                    outerRadius={80}
                    paddingAngle={5}
                    dataKey="total"
                    nameKey="category__name"
                  >
                    {summary.spending_by_category.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={CHART_COLORS[index % CHART_COLORS.length]} />
                    ))}
                  </Pie>
                  <Legend />
                </PieChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="transactions" className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle>Recent Transactions</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-2">
                {transactions.map(transaction => (
                  <div
                    key={transaction.id}
                    className="flex items-center justify-between p-2 border rounded"
                  >
                    <div>
                      <div className="font-medium">{transaction.category_name}</div>
                      <div className="text-sm text-gray-500">{transaction.date}</div>
                    </div>
                    <div className={`font-bold ${
                      transaction.type === 'income' ? 'text-green-600' : 'text-red-600'
                    }`}>
                      {transaction.type === 'income' ? '+' : '-'}${transaction.amount.toFixed(2)}
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="budgets" className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle>Budget Overview</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {budgets.map(budget => {
                  const percentage = (budget.spent / budget.limit) * 100;
                  const isOverBudget = percentage > 100;

                  return (
                    <div key={budget.category} className="space-y-2">
                      <div className="flex justify-between">
                        <span className="font-medium">{budget.category}</span>
                        <span>${budget.spent.toFixed(2)} / ${budget.limit.toFixed(2)}</span>
                      </div>
                      <div className="h-2 bg-gray-200 rounded">
                        <div
                          className={`h-full rounded ${isOverBudget ? 'bg-red-500' : 'bg-blue-500'
                            }`}
                          style={{ width: `${Math.min(percentage, 100)}%` }}
                        />
                      </div>
                      {isOverBudget && (
                        <Alert variant="destructive">
                          <AlertDescription>
                            You've exceeded your {budget.category} budget by ${(budget.spent - budget.limit).toFixed(2)}
                          </AlertDescription>
                        </Alert>
                      )}
                    </div>
                  );
                })}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

     
{/* <TabsContent value="budgets" className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle>Budget Overview</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {budgets.map(budget => {
                  const percentage = (budget.spent / budget.amount) * 100;
                  const isOverBudget = percentage > 100;

                  // return (
                  //   <div key={budget.id} className="space-y-2">
                  //     <div className="flex justify-between">
                  //       <span className="font-medium">{budget.category_name}</span>
                  //       <span>${budget.spent.toFixed(2)} / ${budget.amount.toFixed(2)}</span>
                  //     </div>
                      
                  //     </div><div className="h-2 bg-gray-200 rounded">
                  //       <div className='' isOverBudget ? 'bg-re':''/></div>
                  //     </div></div>)
})}*/ */}