result = 0
allIngredients = set()
allAllergens = set()

foods = []

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip().strip(")")
        ingredients, allergens = line.split(" (contains ")
        ingredientsSet = set(ingredients.split())
        allergensSet = set(allergens.split(", "))
        allIngredients.update(ingredientsSet)
        allAllergens.update(allergensSet)

        foods.append(
            {
                "ingredients": ingredientsSet.copy(),
                "allergens": allergensSet.copy()
            }
        )

allergenCorrisp = {}

for allergen in allAllergens:
    allergenCorrisp[allergen] = allIngredients.copy()
    for food in foods:
        if allergen in food["allergens"]:
            allergenCorrisp[allergen].intersection_update(food["ingredients"])
    # notAllergens.difference_update(allergenCorrisp[allergen])

ingredientsFound = {}
while len(ingredientsFound) < len(allergenCorrisp):
    for allergen in allergenCorrisp:
        if allergen not in ingredientsFound and len(allergenCorrisp[allergen]) == 1:
            for otherAllergen in allergenCorrisp:
                if otherAllergen != allergen:
                    allergenCorrisp[otherAllergen] -= allergenCorrisp[allergen]
            ingredientsFound[allergen] = list(allergenCorrisp[allergen])[0]

allergNames = list(ingredientsFound.keys())
allergNames.sort()
allergGibberish = []

for name in allergNames:
    allergGibberish.append(ingredientsFound[name])

result = ",".join(allergGibberish)

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))
