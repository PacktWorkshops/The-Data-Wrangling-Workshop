# These are the unit tests for each exersize, load the module and pass the answer to each function and it will
# return a bool of True or False depending on the answer being correct or false.

# exercise 15


def test_exercise_15_1(x) -> bool:
    return x == [1 for x in range(0, 10000000)]


def test_exercise_15_2(x) -> bool:
    return x == 81528056


def test_exercise_15_3(x) -> bool:
    return x == 56


def test_exercise_15_5(x) -> bool:
    import sys
    if "itertools" in sys.modules:
        return False
    else:
        return True

# exercise 16


def test_exercise_16_1(x) -> bool:
    return x == []


def test_exercise_16_2(x) -> bool:
    return x == [25]


def test_exercise_16_3(x) -> bool:
    return x == [25, -12]


def test_exercise_16_4(x) -> bool:
    return x == -12


def test_exercise_16_5(x) -> bool:
    return x == [25, 'Hello']

# exercise 17


def test_exercise_17_1(x) -> bool:
    return x == []


def test_exercise_17_2(x) -> bool:
    wikipedia_datascience = """Data science is an interdisciplinary 
    field that uses scientific methods, 
    processes, algorithms and systems to extract 
    knowledge [https://en.wikipedia.org/wiki/Knowledge] and i
    nsights from data [https://en.wikipedia.org/wiki/Data] in various
    forms, both structured and unstructured,similar to data mining 
    [https://en.wikipedia.org/wiki/Data_mining]"""
    return x == wikipedia_datascience


def test_exercise_17_3(x) -> bool:
    return x == 347


def test_exercise_17_4a(x) -> bool:
    wikipedia_datascience = """Data science is an interdisciplinary 
        field that uses scientific methods, 
        processes, algorithms and systems to extract 
        knowledge [https://en.wikipedia.org/wiki/Knowledge] and i
        nsights from data [https://en.wikipedia.org/wiki/Data] in various
        forms, both structured and unstructured,similar to data mining 
        [https://en.wikipedia.org/wiki/Data_mining]"""
    wd_list = wikipedia_datascience.split()
    return x == wd_list


def test_exercise_17_4b(x) -> bool:
    return x == 34


def test_exercise_17_5(x) -> bool:
    return x == ["https://en.wikipedia.org/wiki/Data_mining",
                 "https://en.wikipedia.org/wiki/Data",
                 "https://en.wikipedia.org/wiki/Knowledge"]


def test_exercise_17_8(x) -> bool:
    return x == []


# exercise 18


def test_exercise_18_1(x) -> bool:
    import sys
    if "math" in sys.modules:
        return False
    else:
        return True


def test_exercise_18_1(x) -> bool:
    return "my_sine" in dir() and "my_cosine" in dir()


def test_exercise_18_2(x) -> bool:
    return "my_sine" in dir() and "my_cosine" in dir()


def test_exercise_18_3(x) -> bool:
    return x == 1.0


# exercise 19


def test_exercise_19_1(x) -> bool:
    return x == [('USA', 'Washington'),
                 ('India', 'Delhi'),
                 ('France', 'Paris'),
                 ('UK', 'London')]


def test_exercise_19_2(x) -> bool:
    return x == [('India', 'Delhi'),
                 ('UK', 'London'),
                 ('France', 'Paris'),
                 ('USA', 'Washington')]

# exercise 20


def test_exercise_20_1(x) -> bool:
    return x == ['Hello', 'there.', 'How', 'are', 'you', 'doing?']


def test_exercise_20_2(x) -> bool:
    return x == ['How', 'are']


def test_exercise_20_3(x) -> bool:
    return x == True


# exercise 21

def test_exercise_21_1(x) -> bool:
    return x == range(0, 100000)


def test_exercise_21_2(x) -> bool:
    return x == []


# exercise 22


def test_exercise_22_1(x) -> bool:
    import sys
    if "os" in sys.modules:
        return False
    else:
        return True


def test_exercise_22_2(x) -> bool:
    return x == 'MY_VAL'



