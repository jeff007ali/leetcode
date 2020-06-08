def twoCitySchedCost(costs):
    costs.sort(key=lambda cost: cost[0] - cost[1])
    costs_for_A = sum([cost[0] for cost in costs[:len(costs) // 2]])
    costs_for_B = sum([cost[1] for cost in costs[len(costs) // 2:]])
    return costs_for_A + costs_for_B


print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
print(twoCitySchedCost([(10, 50), (50, 40), (30, 100), (10, 20), (50, 90), (40, 20)]))
