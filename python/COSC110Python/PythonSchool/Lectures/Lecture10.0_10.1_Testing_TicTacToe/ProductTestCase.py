from Product import *
from Product import Product

import unittest # is object oriented so test has to be in a class.as



class ProductTestCase(unittest.TestCase):

    # this is part of a test fixture, run before each test case individually.
    def setUp(self):
        self.p = Product(10, 2.5)

    def testPurchaseSuccess(self):
        # args: first, second, numplaces (2 dec. places)
        self.assertAlmostEqual(self.p.purchase(10), 25, 2) # testing boundary case.

    def testPurchaseFailure(self):
        with self.assertRaises(ValueError):
            self.p.purchase(20)

# not necessary but useful
def suite():
    suite = unittest.TestSuite()
    suite.addTest(ProductTestCase("testPurchaseSuccess"))
    suite.addTest(ProductTestCase("testPurchaseFailure"))
    return suite


if __name__ == "__main__":
    # Method 1 of returning results
    # unittest.main() # note run setup, run failure, run teardown (if available), run set up, run test success.
    # in command line run:
    # python3 ProductTestCase.py -v
    # to get more detail about tests run.

    # Method 2 of returning results
    unittest.TextTestRunner(verbosity=2).run(suite()) # run just those in the suite, and in order WE state
    # the first method runs in alphabetical order