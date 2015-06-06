# Programming language
Python 3.4.2

# Editor
PyCharm IDE

# Contribution guide
Please see circle ci after you submit PR. If all test are passed, you can merge your PR.
https://circleci.com/gh/giwa/giwa-sezemi-2015-readable-code
Please don't violate PEP8.

# Execute
I implement doctest for each method. You can refer them to get idea how to execute the code.
I assume that `Recipe` is already imported.

## Task1
```
        >>> recipe = Recipe()
        >>> recipe.test()
        オムライス
```

## Task3

```
        >>> recipe = Recipe()
        >>> recipe.read_file("./data/recipe-data.txt")
        >>> print(recipe)
        オムライス
        親子丼
        杏仁豆腐
        ...
```