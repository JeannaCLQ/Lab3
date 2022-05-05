import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90,45,23,80]
    test_arr = [11, 12, 22,23, 25, 34,45, 64,80, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90,45,23,80]
    test_arr = [90, 80, 64, 45, 34, 25,23, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    input_arr = [64, 34, 25, 12, 22, 11, 90,45,67,89]
    test_arr = []

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == test_arr)

def test_bubble_more_than_ten():
    input_arr = [1,2,3,4,5,6,7,8,9,0,1]
    test_arr = 1

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_less_than_ten():
    input_arr = [1,2]
    test_arr = 2

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result==test_arr)

def test_bubble_no_numbers():
    input_arr =[]
    test_arr = 0

    result = Lab3.bubble_sort(input_arr,Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_none_integer():
    input_arr = [2.3,4.5,2.3,4.5]
    test_arr = 3

    result = Lab3.bubble_sort(input_arr,Lab3.SORT_DESCENDING)

    assert (result == test_arr)