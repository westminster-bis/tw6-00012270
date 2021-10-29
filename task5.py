def test_is_valid(test):
    if isinstance(test, int) and test>=0 and test<=3:
        return True
    else:
        return False

print(test_is_valid(int(input())))