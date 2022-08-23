n, t = [int(x) for x in input().split(" ")]

potions = sorted([int(input()) for x in range(n)])[::-1]

print(potions)

def possible_cocktail() -> bool:
    for i, duration in enumerate(potions):
        if duration <= (n-i-1)*t:
            return False
    return True

print("YES") if possible_cocktail() else print("NO")