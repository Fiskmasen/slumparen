varor = [
    ["monster", 20],
    ["coca-cola energy", 11],
    ["liten läsk", 8],
    ["mellan läsk", 16],
    ["stor läsk", 24],
    ["daim-glass", 25],
    ["kexchoklad", 8],
    ["OLW-snax", 20],
    ["ölkorv", 40]
]

print("Det är rast, dax att gå till COOP!")

budget = int(input("Vad är din budget i kronor: "))

import random, time

shoppinglista = []

print("Du vandrar runt och bestämmer dig för att köpa...")
time.sleep(2)

while budget > 5:
    vara = varor[random.randint(0, len(varor)-1)]
    if budget > vara[1]:
        shoppinglista.append(vara)
        budget = budget - vara[1]

print("Din COOP loot är: ")

for vara in shoppinglista:
    print(f"{vara[0]}")

print(f"Kvar i din ficka ligger {budget:0} kronor.")
