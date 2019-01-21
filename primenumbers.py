x = range(1, 101)
for p in x:
    if p > 1:
        for q in range(2, p):
            if (p % q) == 0:
                break
        else:
            print(p)

