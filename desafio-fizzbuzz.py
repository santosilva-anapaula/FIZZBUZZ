
for elemento in range(1, 16):
    if elemento % 3 == 0 and elemento % 5 == 0:
        print("FIZZBUZZ")
    elif elemento % 3 == 0:
        print("FIZZ")
    elif elemento % 5 == 0:
        print("BUZZ")
    else:
        print(elemento)