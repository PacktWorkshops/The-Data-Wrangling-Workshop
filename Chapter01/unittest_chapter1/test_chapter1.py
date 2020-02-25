# These are the unit tests for each exersize, load the module and pass the answer to each function and it will
# return a bool of True or False depending on the answer being correct or false.

# exercise 1


def test_exercise_1_1(x) -> bool:
    return x == ['218-68-9955',
                 '165-73-3124',
                 '432-47-4043',
                 '563-93-1393',
                 '153-93-3401',
                 '670-09-7369',
                 '123-05-9652',
                 '812-13-2476',
                 '726-13-1007',
                 '825-05-4836']


def test_exercise_1_2(x) -> bool:
    return x == '218-68-9955'


def test_exercise_1_3(x) -> bool:
    return x == '563-93-1393'


def test_exercise_1_4(x) -> bool:
    return x == '825-05-4836'


def test_exercise_1_5(x) -> bool:
    return x == '825-05-4836'


def test_exercise_1_6(x) -> bool:
    return x == ['165-73-3124', '432-47-4043']


def test_exercise_1_7(x) -> bool:
    return x == ['726-13-1007', '825-05-4836']


def test_exercise_1_8(x) -> bool:
    return x == ['218-68-9955',
                 '165-73-3124',
                 '432-47-4043',
                 '563-93-1393',
                 '153-93-3401',
                 '670-09-7369',
                 '123-05-9652',
                 '812-13-2476']


def test_exercise_1_9(x) -> bool:
    return x == ['825-05-4836',
                 '726-13-1007',
                 '812-13-2476',
                 '123-05-9652',
                 '670-09-7369',
                 '153-93-3401',
                 '563-93-1393',
                 '432-47-4043',
                 '165-73-3124',
                 '218-68-9955']


# exercise 2


def test_exercise_2_1(x) -> bool:
    return x == ['218-68-9955',
                 '165-73-3124',
                 '432-47-4043',
                 '563-93-1393',
                 '153-93-3401',
                 '670-09-7369',
                 '123-05-9652',
                 '812-13-2476',
                 '726-13-1007',
                 '825-05-4836']


def test_exercise_2_2(x) -> bool:
    return x == ['soc: 218-68-9955',
                 'soc: 165-73-3124',
                 'soc: 432-47-4043',
                 'soc: 563-93-1393',
                 'soc: 153-93-3401',
                 'soc: 670-09-7369',
                 'soc: 123-05-9652',
                 'soc: 812-13-2476',
                 'soc: 726-13-1007',
                 'soc: 825-05-4836']


def test_exercise_2_4(x) -> bool:
    return x == ['soc: 218-68-9955',
                 'soc: 165-73-3124',
                 'soc: 563-93-1393',
                 'soc: 153-93-3401',
                 'soc: 123-05-9652',
                 'soc: 825-05-4836']


def test_exercise_2_5(x) -> bool:
    return x == ['102-90-0314',
                 '247-17-2338',
                 '318-22-2760',
                 '218-68-9955',
                 '165-73-3124',
                 '432-47-4043',
                 '563-93-1393',
                 '153-93-3401',
                 '670-09-7369',
                 '123-05-9652',
                 '812-13-2476',
                 '726-13-1007',
                 '825-05-4836']


def test_exercise_2_6(x) -> bool:
    return x == ['218-68-9955',
                 '165-73-3124',
                 '432-47-4043',
                 '563-93-1393',
                 '153-93-3401',
                 '670-09-7369',
                 '123-05-9652',
                 '812-13-2476',
                 '726-13-1007',
                 '825-05-4836',
                 '102-90-0314',
                 '247-17-2338',
                 '318-22-2760']


# exercise 3

def test_exercise_3_1(x) -> bool:
    return x == ["Escalade",
                 "X5 M", "D150",
                 "Camaro",
                 "F350",
                 "Aurora",
                 "S8",
                 "E350",
                 "Tiburon",
                 "F-Series Super Duty"]


def test_exercise_2__2(x) -> bool:
    return x == True


def test_exercise_2__3(x) -> bool:
    return x == False


# exercise 4


def test_exercise_4__1(x) -> bool:
    return x == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def test_exercise_4_2(x) -> bool:
    return x == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# exercise 5

def test_exercise_5__1(x) -> bool:
    import sys
    if "random" not in sys.modules:
        return False
    else:
        return True


def test_exercise_5__2(x) -> bool:
    return 100 == len(x)


# exercise 6


def test_exercise_6__1(x) -> bool:
    return x == {"Solar Capital Ltd.": "$920.44M",
                 "Zoe's Kitchen, Inc.": "$262.32M",
                 "Toyota Motor Corp Ltd Ord": "$156.02B",
                 "Nuveen Virginia Quality Municipal Income Fund": "$238.33M",
                 "Kinross Gold Corporation": "$5.1B",
                 "Vulcan Materials Company": "$17.1B",
                 "Hi-Crush Partners LP": "$955.69M",
                 "Lennox International, Inc.": "$8.05B",
                 "WMIH Corp.": "$247.66M",
                 "Comerica Incorporated": "n/a"}


def test_exercise_6__2(x) -> bool:
    return x == "'$247.66M'"


def test_exercise_6__3(x) -> bool:
    return x == "$300M"


def test_exercise_6__4(x) -> bool:
    return x == {'key1': 'Value1'}


# exercise 7

def test_exercise_7_1(x) -> bool:
    return x == {'Solar Capital Ltd.': '920.44M',
                 "Zoe's Kitchen, Inc.": '262.32M',
                 'Toyota Motor Corp Ltd Ord': '156.02B',
                 'Nuveen Virginia Quality Municipal Income Fund': '238.33M',
                 'Kinross Gold Corporation': '5.1B',
                 'Vulcan Materials Company': '17.1B',
                 'Hi-Crush Partners LP': '955.69M',
                 'Lennox International, Inc.': '8.05B',
                 'WMIH Corp.': '300M',
                 'Comerica Incorporated': 'n/a'}


def test_exercise_7_2(x) -> bool:
    return x == {'Solar Capital Ltd.': ['920.44', 'M'],
                 "Zoe's Kitchen, Inc.": ['262.32', 'M'],
                 'Toyota Motor Corp Ltd Ord': ['156.02', 'B'],
                 'Nuveen Virginia Quality Municipal Income Fund': ['238.33', 'M'],
                 'Kinross Gold Corporation': ['5.1', 'B'],
                 'Vulcan Materials Company': ['17.1', 'B'],
                 'Hi-Crush Partners LP': ['955.69', 'M'],
                 'Lennox International, Inc.': ['8.05', 'B'],
                 'WMIH Corp.': ['300', 'M'],
                 'Comerica Incorporated': ['n/', 'a']}


# exercise 8


def test_exercise_8__1(x) -> bool:
    return 100 == len(x)


def test_exercise_8__2(x) -> bool:
    return 31 == len(x)


# exercise 9

def test_exercise_9_1(x) -> bool:
    return x == {'key1': 1,
                 'key2': ['list_element1', 34],
                 'key3': 'value3',
                 'key4': {'subkey1': 'v1'},
                 'key5': 4.5}


def test_exercise_9_2(x) -> bool:
    return x == {'key1': 1, 'key3': 'value3', 'key4': {'subkey1': 'v1'}, 'key5': 4.5}


def test_exercise_9_3(x) -> bool:
    return x == {'key1': 1, 'key4': {'subkey1': 'v1'}, 'key5': 4.5}


def test_exercise_9_4(x) -> bool:
    return x == {'key1': 1, 'key5': 4.5}

# exercise 10

def test_exercise_10_1(x) -> bool:
    return x == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


def test_exercise_10_2(x) -> bool:
    return x == {'Tom': 100, 'Dick': 200, 'Harry': 300}


def test_exercise_10_3(x) -> bool:
    return x == {'Tom': 100, 'Dick': 200, 'Harry': 300}


# exercise 11


def test_exercise_11_1(x) -> bool:
    return x == ('1', '3', '5')


# exercise 12


def test_exercise_12_1(x) -> bool:
    return x == 'Hello World!'


def test_exercise_12_3(x) -> bool:
    return x == 'o'


def test_exercise_12_4(x) -> bool:
    return x == '!'


def test_exercise_12_5(x) -> bool:
    return x == '!'


# exercise 13


def test_exercise_13_1(x) -> bool:
    return x == 'Hello World! I am learning data wrangling'


def test_exercise_13_2(x) -> bool:
    return x == 'llo Worl'


def test_exercise_13_3(x) -> bool:
    return x == 'd! I am learning data wrangling'


def test_exercise_13_4(x) -> bool:
    return x == ' wran'


# exercise 14


def test_exercise_13_4(x) -> bool:
    return x == ['Name', ' Age', ' Sex', ' Address']


def test_exercise_13_4(x) -> bool:
    return x == 'Name |  Age |  Sex |  Address'
