Readable code

I joined readable code event hold by sezemi. Many top engineer in famous IT companies such as Treasure data and Freak out contribute to this event, which is pretty cool! yay! I was assigned to a Python group. I note my principle for writing Python code.

# Poem
## Why do I write this document in English?
In most of open sources, comitters and contributers are communicated in English. I know my English is bad. Never mind! Code is written in English. We alredy kwnow "technical English". Don't be shy! Practice makes perfect!

If you are unconfident in your English, ALC and Grammaly is your friend.

## Tool choice
* PyCharm

Considering the task for this event, I choose PyCharm as an editor becuase PyCharm has strong refactoring and lint functions. These functions are suitable for writing code. In daily coding, I definitely choose Vim for this task. I love Vim.

## Code convention and principle
* PEP8
* Zen of Python

Python has an amazing code convention, PEP 8. I believe this is defact standard for Python code convention for OSS. I will follow PEP8 as much as I can.

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

P.S
Uncle Tim is also famous for invention of Tim Sort.

## Python version
* 3.4.2

I choose Python 3.4.2 because 2.7.* become EOL by 2020 and it is the latest Python version supprted in circleci by default. If I have time, I will adapt my code to Python 2.7.*

## Testing
* doctest

All function should have a doctest. These tests are tested in circleci. Please look at circle.yml for details.

## Doc string
All class and function should have doc string and doc test. Doc string is useful to explain what this code does explicilty. Doc test is also useful to give examples of how to use the code.

## Contributing guide line
If all tests are passed, you can merge your PR. Lint are done by PEP 8. If you want to change code with PEP8 violation, please make a PR and describe why your proposal is more readable than PEP8.

# Memo Template
##
### Code

```Python

```

### Readbility

### Brief description

### Motivation

## Memo1
### Code
```
    def read_file(self, file_path):
```

This function gets file path as an input. If the name is jsut file, it cause confusion becuase it might be a file object.

### Motivation
Declare input explicity.

## Memo2
### Code
```
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
```


### Motivation
doctest is a pretty good exmaple to explan how to use the function.

## Memo3
### Code
```
def _test():
    import doctest
    (failure_count, test_count) = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if failure_count:
        exit(-1)


if __name__ == "__main__":
    _test()
```

### Motivation
_test function is a private method. Since this is only for test, test code should not expose to be public.

Stable Code. All function should be tested to improve reliability.



# Added by K.Mori

## Good points for these codes
* Divide the solving and Running
    * Easy for operation and maintenance
* Define the Class and Function
    * Easy for reading

## Memo5
### Code
Added the code to task4
```
        txt_length =sum(1 for line in open(file_path))
        recipe_id = [x+1 for x in range(txt_length)]
        for i in range(txt_length):
            print("{0}:{1}".format(recipe_id[i], self._recipes[i]))
```

### Motivation
Want to use list for ID & the name of recipe.
The name was already existed. So I made the ID's list.