def criate_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply

duplication = criate_multiplier(2)
triplication = criate_multiplier(3)
quadrupling = criate_multiplier(4)

print(
    duplication(5),
    triplication(4),
    quadrupling(7)
)