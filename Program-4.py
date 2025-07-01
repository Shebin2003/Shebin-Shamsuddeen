numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
multiples = [1,2,3,4,5,6,7,8,9]
counts = {m: 0 for m in multiples}
for num in numbers:
    for m in multiples:
        if num % m == 0:
            counts[m] += 1
print(counts)
