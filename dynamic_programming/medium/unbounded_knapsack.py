from typing import List


class Solution:
    def unbounded_knapsack(self, weights: List[int], values: List[int], capacity: int) -> int:
        n = len(weights)

        # Create a 1D DP array initialized with 0
        dp = [0] * (capacity + 1)

        for j in range(capacity + 1):  # Iterate over capacities
            for i in range(n):  # Iterate over items
                if weights[i] <= j:
                    dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

        return dp[capacity]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

sol = Solution()
print(sol.unbounded_knapsack(weights, values, capacity))

Part I The Basics 1
Chapter 1 What Is Data Modeling?
1.1 Introduction 3
1.2 A Data-Centered Perspective 3
1.3 A Simple Example 4
1.4 Design, Choice, and Creativity 6
1.5 Why Is the Data Model Important? 8
1.5.1 Leverage 8
1.5.2 Conciseness 9
1.5.3 Data Quality 10
1.5.4 Summary 10
1.6 What Makes a Good Data Model? 10
1.6.1 Completeness 10
1.6.2 NonRedundancy 11
1.6.3 Enforcement of Business Rules 11
1.6.4 Data Reusability 11
1.6.5 Stability and Flexibility 12
1.6.6 Elegance 13
1.6.7 Communication 14
1.6.8 Integration 14
1.6.9 Conflicting Objectives 15
1.7 Performance 15
1.8 Database Design Stages and Deliverables 16
1.8.1 Conceptual, Logical, and Physical Data Models 16
1.8.2 The Three-Schema Architecture and Terminology 17
1.9 Where Do Data Models Fit In? 20
1.9.1 Process-Driven Approaches 20
1.9.2 Data-Driven Approaches 20
1.9.3 Parallel(Blended) Approaches 22
1.9.4 Object-Oriented Approaches 22
1.9.5 Prototyping Approaches 23
1.9.6 Agile Methods 23
1.10 Who Should Be Involved in Data Modeling? 23
1.11 Is Data Modeling Still Relevant? 24
1.11.1 Costs and Benefits of Data Modeling 25
1.11.2 Data Modeling and Packaged Software 26
1.11.3 Data Integration 27
1.11.4 Data Warehouses 27
1.11.5 Personal Computing and User-Developed Systems 28
1.11.6 Data Modeling and XML 28
1.11.7 Summary 28
1.12 Alternative Approaches to Data Modeling 29
1.13 Terminology 30
1.14 Where to from Here?—An Overview of Part I 31
1.15 Summary 32
