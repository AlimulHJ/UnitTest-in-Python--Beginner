import write_your_name as name_point

# def test_hi_my_name_is():
#     assert len(name_point.hi_my_name_is())  > 1

def test_hi_my_name_is():
    name1 = name_point.hi_my_name_is()
    name2 = name_point.hi_my_name_is()
    assert len(name1) > 0, "The entered 1st name is empty!"
    assert len(name2) > 0, "The entered 2nd name is empty!"

    print(f"Test passed! Your name is: {name1} & {name2}")


