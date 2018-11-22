import X


epsilon = 0.00001


def nearlyEqual(val, target):
    return abs(val - target) < epsilon

# testing add,sub, mul, div --------------------------------------------------------------------------

def testAddProperties():
    assert X.add(-5, 9) == 4
    assert X.add(5, -9) == -4
    assert X.add(-5, -9) == -14
    assert X.add(5, 9) == 14

def testSubProperties():
    assert X.sub(23, 4) == 19
    assert X.sub(4, 23) == -19
    assert X.sub(18, -3) == 21
    assert X.sub(-18, -3) == -15

def testMulProperties():
    assert X.mul(0, 123123) == 0
    assert X.mul(-2, -4) == 8
    assert X.mul(-2, 4) == -8


def testDivCorrect():
    assert nearlyEqual(X.div(2,3), 0.6666666666666666667)
    assert nearlyEqual(X.div(56,8), 7)


def testDivByZero():
    try:
        X.div(1, 0)
    except AssertionError:
        pass
    else:
        assert False, "Div by zero not accounted for!"



# testing calc strange value --------------------------------------------------------------------------

def testCalcStrangeValue_X_GreaterThan_Y():
    div = X.div(89, 7)
    assert nearlyEqual(div, 12.7142857)
    sub = X.sub(89, 7)
    assert sub == 82
    assert nearlyEqual(X.mul(div, sub), 1042.571429)
    assert nearlyEqual(X.mul(div, sub), X.calculateStrangeValue(89, 7))

def testCalcStrangeValue_X_LessThan_Y():
    mul = X.mul(7, 89)
    assert nearlyEqual(mul, 623)
    add = X.add(7, 89)
    assert add == 96
    assert nearlyEqual(X.mul(mul, add), 59808)
    assert nearlyEqual(X.mul(mul, add), X.calculateStrangeValue(7, 89))

def testCalcStrangeValue_X_Equal_Y():
    assert X.calculateStrangeValue(4, 4) == 1
    assert X.calculateStrangeValue(0, 0) == 1
    assert X.calculateStrangeValue(0, 10) != 1




# testing is valid pos int --------------------------------------------------------------------------

def testIsValidPosInt():
    assert not X.isValidPositiveIntegerInput("wrong")
    assert X.isValidPositiveIntegerInput("23") == True
    assert X.isValidPositiveIntegerInput(23) == True
    assert not X.isValidPositiveIntegerInput("-23")
    assert not X.isValidPositiveIntegerInput(-23)
    assert not X.isValidPositiveIntegerInput(1.5)
    assert not X.isValidPositiveIntegerInput(0)




if __name__ == "__main__":
    testAddProperties()
    testSubProperties()
    testMulProperties()
    testDivByZero()
    testDivCorrect()
    testCalcStrangeValue_X_Equal_Y()
    testCalcStrangeValue_X_GreaterThan_Y()
    testCalcStrangeValue_X_LessThan_Y()
    testIsValidPosInt()