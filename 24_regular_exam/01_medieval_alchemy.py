from collections import deque


potions_energy = {
    "Brew of Immortality": 110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility":  80,
    "Elixir of Strength": 70
}

substances = [int(x) for x in input().split(", ")]
crystals = deque(int(x) for x in input().split(", "))

crafted_potions = []

while substances and crystals and len(crafted_potions) < 5:
    substance = substances.pop()
    crystal = crystals.popleft()
    total_energy = substance + crystal
    potion_made = None

    for potion, energy in potions_energy.items():
        if potion not in crafted_potions and energy == total_energy:
            potion_made = potion
            break

    if potion_made:
        crafted_potions.append(potion_made)
        continue

    max_energy = float("-inf")

    for potion, energy in potions_energy.items():
        if potion not in crafted_potions and energy <= total_energy:
            if energy > max_energy:
                max_energy = energy
                potion_made = potion

    if potion_made:
        crafted_potions.append(potion_made)
        crystal -= 20
        if crystal > 0:
            crystals.append(crystal)
        continue

    crystal -= 5
    if crystal > 0:
        crystals.append(crystal)

if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")

if substances:
    print(f"Substances: {', '.join(map(str, reversed(substances)))}")

if crystals:
    print(f"Crystals: {', '.join(map(str, crystals))}")
