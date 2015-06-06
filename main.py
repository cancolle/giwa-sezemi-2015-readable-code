from recipe import Recipe

def task1():
    recipe = Recipe()
    recipe.test()

# For Task3 and 4
def task3_task4():
    recipe = Recipe()
    recipe.read_file("./data/recipe-data.txt")
    print(recipe)

# For Task5
def task5():
    recipe = Recipe()
    recipe.read_file_id("./data/recipe-data.txt")
    print(recipe)

if __name__ == "__main__":
    task1()
    task3_task4()
    task5()