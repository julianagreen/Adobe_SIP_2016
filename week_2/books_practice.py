import random

meal_adj = [". Creamy ", ". Crunchy ", ". Spicy ", ". Chilled ", ". Crispy ", ". Raw ", ". Sizzling ", ". Filling ", ". Carefully ", ". Refreshing "]

meal_adj2 = ["Steamed ", "Fried ", "Sauted ", "Seasoned ", "Seared ", "Cured ", "Boiled ", "Baked ", "Grilled ", "Home-style "]

main_dish = ["Shrimp", "Chicken", "Steak", "Mushrooms", "Scallops", "Bacon and Beans", "Talapia", "Salmon", "Pork chops", "Crab"]

counter = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

for i in range(10):
    rand_adj1 = random.randint(0, 9)
    rand_adj2 = random.randint(0, 9)
    rand_dish = random.randint(0, 9)

    def meal(counter):
        print(counter + meal_adj[rand_adj1] + meal_adj2[rand_adj2] + main_dish[rand_dish])

    meal(counter[i])
