from gurobipy import *

#Sets
Cakes = ["Chocolate","Pound"]
Ingredients = ["Time","Eggs","Milk"]

C = range(len(Cakes))
I = range(len(Ingredients))

#Data
price = [400, 200]
available = [8*60, 30, 5]
usage = [
        [20,50],
        [4,1],
        [0.25,0.2]
        ]

m = Model("IP")

#decide variables
X = {}
for c in C:
    X[c] = m.addVar(vtype=GRB.INTEGER) #set integer

#objective function
m.setObjective(quicksum(price[c]*X[c] for c in C), GRB.MAXIMIZE)

#constraints
for i in I:
    m.addConstr(quicksum(usage[i][c]*X[c] for c in C) <= available[i])

#solver
m.optimize()

#result
for c in C:
    print("Bake", X[c].x, Cakes[c])
print("Revenue is", m.objVal)