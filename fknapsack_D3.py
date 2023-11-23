def fractional_knapsack(value, weight, capacity):
    # Calculate value-to-weight ratio for each item
    ratios = [(v / w, v, w) for v, w in zip(value, weight)]

    # Sort items by value-to-weight ratio in descending order
    ratios.sort(reverse=True)

    total_value = 0  # Total value in the knapsack
    knapsack = [0] * len(value)  # Fraction of each item in the knapsack

    for ratio, v, w in ratios:
        # Add as much of the item as possible to the knapsack
        if capacity >= w:
            knapsack[value.index(v)] = 1
            total_value += v
            capacity -= w
        else:
            fraction = capacity / w
            knapsack[value.index(v)] = fraction
            total_value += fraction * v
            break

    return total_value, knapsack

# Example usage:
value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

result_value, result_knapsack = fractional_knapsack(value, weight, capacity)

print("Maximum value in the knapsack:", result_value)
print("Fraction of each item in the knapsack:", result_knapsack)