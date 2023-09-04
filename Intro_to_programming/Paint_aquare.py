import math


def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = ((sqft_walls + sqft_ceiling) * (cost_per_gallon / sqft_per_gallon))
    return cost


one_coat_cost = get_cost(432, 144, 400, 15)
print(one_coat_cost)
