from gurobipy import *

# Sets
Oils = ["Veg1", "Veg2", "Oil1", "Oil2", "Oil3"]
Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
I = range(len(Oils))
T = range(len(Months))

# Data
Cost = [
    [110, 120, 130, 110, 115],
    [130, 130, 110, 90, 115],
    [110, 140, 130, 100, 95],
    [120, 110, 120, 120, 125],
    [100, 120, 150, 110, 105],
    [90, 100, 140, 80, 135]
]

Hard = [8.8, 6.1, 2.0, 4.2, 5.0]
IsVeg = [True, True, False, False, False]
MaxVeg = 200
MaxNonVeg = 250
Sell = 150
MinH = 3
MaxH = 6
StoreMax = 1000
StoreCost = 5
Init = 500

# Model
m = Model("Oil Blending")

# Variables
X = {(i, t): m.addVar() for i in I for t in T}  # amount to process
S = {(i, t): m.addVar() for i in I for t in T}  # amount to store
Y = {(i, t): m.addVar() for i in I for t in T}  # amount to purchase

# Objective (revenue-cost)
m.setObjective(quicksum(Sell * X[i, t] for i in I for t in T) -
               quicksum(StoreCost * S[i, t] for i in I for t in T) -
               quicksum(Cost[t][i] * Y[i, t] for i in I for t in T), GRB.MAXIMIZE)

# Constraints
for t in T:
    # Process
    m.addConstr(quicksum(X[i, t] for i in I if IsVeg[i]) <= MaxVeg)
    m.addConstr(quicksum(X[i, t] for i in I if not IsVeg[i]) <= MaxNonVeg)

    # Hard
    m.addConstr(quicksum((Hard[i] - MaxH) * X[i, t] for i in I) <= 0)
    m.addConstr(quicksum((Hard[i] - MinH) * X[i, t] for i in I) >= 0)

    # Store
    for i in I:
        m.addConstr(S[i, t] <= StoreMax)
        if t == 0:
            m.addConstr(S[i, t] == Init - X[i, t] + Y[i, t])
        else:
            m.addConstr(S[i, t] == S[i, t - 1] - X[i, t] + Y[i, t])

# Initial
for i in I:
    m.addConstr(S[i, T[-1]] == Init)

# Optimizeation
m.optimize()

# Results
print("Profit is", m.objVal)

print("Processing")
for i in I:
    print(Oils[i], [round(X[i, t].x, 1) for t in T])

print("Storage")
for i in I:
    print(Oils[i], [round(S[i, t].x, 1) for t in T])

print("Purchasing")
for i in I:
    print(Oils[i], [round(Y[i, t].x, 1) for t in T])

print("Hardness")
print([sum([Hard[i] * X[i, t].x for i in I]) / sum([X[i, t].x for i in I]) for t in T])