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

notAllergens = allIngredients.copy()

for allergen in allAllergens:
    possibleIngredients = allIngredients.copy()
    for food in foods:
        if allergen in food["allergens"]:
            possibleIngredients.intersection_update(food["ingredients"])
    notAllergens.difference_update(possibleIngredients)

for food in foods:
    result += len(
        notAllergens & food["ingredients"]
    )

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))
