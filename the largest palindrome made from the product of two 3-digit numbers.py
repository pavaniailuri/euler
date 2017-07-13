def is_pal(c):
    return int(str(c)[::-1]) == c

maxpal = 0
for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        prod = a * b
        if is_pal(prod) and prod > maxpal:
            maxpal = prod

print maxpal
