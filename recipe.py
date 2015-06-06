class Recipe:
    """
    Recipe class for sezemi 2015
    """
    def _init__(self):
        pass

    @staticmethod
    def test():
        """
        Task1 print a dish

        >>> recipe = Recipe()
        >>> recipe.test()
        オムライス
        """
        print("オムライス")


def _test():
    import doctest
    (failure_count, test_count) = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if failure_count:
        exit(-1)


if __name__ == "__main__":
    _test()
