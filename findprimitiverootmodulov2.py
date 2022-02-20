
def primroots(modulo, math):
    print("finding prime root modulo's for encryption")
    required_set = {num for num in range(1, modulo) if math.gcd(num, modulo) }
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]