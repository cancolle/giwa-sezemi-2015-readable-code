from pprint import pprint

class Recipe:
    """
    Recipe class for sezemi 2015
    """
    def __init__(self):
        self._recipes = []

    @staticmethod
    def test():
        """
        Task1 print a dish

        >>> recipe = Recipe()
        >>> recipe.test()
        オムライス
        """
        print("オムライス")

    def read_file(self, file_path):
        """
        Recipe from a file. Data are added to existing recipes
        File format is supposed to one recipe at one line.

        >>> recipe = Recipe()
        >>> recipe.read_file("./data/recipe-data.txt")
        >>> print(recipe)
        オムライス
        親子丼
        杏仁豆腐
        ...
        """
        with open(file_path) as f:
            recipes = f.readlines()
            cleaned_recipes = map(lambda recipe: recipe.strip(), recipes)
        self._recipes.extend(cleaned_recipes)

    def __str__(self):
        for recipe in self._recipes:
            print(recipe)
        return ""



def _test():
    import doctest
    (failure_count, test_count) = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if failure_count:
        exit(-1)


if __name__ == "__main__":
    _test()
