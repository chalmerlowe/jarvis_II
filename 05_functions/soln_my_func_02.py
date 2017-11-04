def microbe_growth(initial_count, rate):
    return initial_count * rate

projected_population = microbe_growth(500, 1.05)
print(projected_population)