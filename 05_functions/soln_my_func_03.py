def microbe_growth(initial_count, rate=1.05):
    return initial_count * rate

projected_population = microbe_growth(500)
print(projected_population)

high_projected_population = microbe_growth(500, rate=1.35)
print(high_projected_population)