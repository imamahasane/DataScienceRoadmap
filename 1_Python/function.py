
def total_exp(exp):
    total = 0
    for valu in exp:
        total += valu
    return total

samiul = [1100, 2200, 3300, 4400, 5500, 6600, 7700]
naima = [1010, 2020, 2222, 3333, 4444, 5555, 6666]

samiul_total = total_exp(samiul)
naima_total = total_exp(naima)

print(f"Samiul's Total Expencess: {samiul_total}")
print(f"Naima's Total Expencess: {naima_total}")