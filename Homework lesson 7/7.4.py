
def common_elements():

    set_3 = set(range(0, 100, 3))
    set_5 = set(range(0, 100, 5))

    return set_3 & set_5


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
