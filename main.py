#Задача 1
with open("рецепты.txt") as file:
    cook_book = {}
    for line in file:
        name_food = line.strip()
        n = int(file.readline())
        ingredient_list = []
        for i in range(n):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(" | ")
            ingredient_list.append({"ingredient_name": ingredient_name, "quantity": quantity,  "measure": measure})
        cook_book[name_food] = ingredient_list
        file.readline()

#Задача 2
def get_shop_list_by_dishes(dishes, person_count):
    ingredient_dict = {}
    ingredients = []
    for food in dishes:
        ingredients = ingredients + cook_book[food]
    for ingred in ingredients:
        if ingred["ingredient_name"] in ingredient_dict:
            ingredient_dict[ingredient_name]["quantity"] += int(ingred["quantity"]) * person_count
        else:
            ingredient_dict[ingred["ingredient_name"]] = {"quantity": int(ingred["quantity"]) * person_count, "measure": ingred["measure"]}
    print(ingredient_dict)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

#Задача 3
with open("f1.txt") as f1:
    f1_list = f1.readlines()
with open("f2.txt") as f2:
    f2_list = f2.readlines()
    f2_list[-1] = f2_list[-1] + "\n"
with open("f3.txt", "w") as f3:
    if len(f1_list) < len(f2_list):
        f3_list = f1_list + f2_list
    else:
        f3_list = f2_list + f1_list
    for i in f3_list:
        f3.write(i)