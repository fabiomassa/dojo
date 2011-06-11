import unittest

from problem1 import Natural

class NaturalNumberIsMultipleTest(unittest.TestCase):
    def test1IsNotMultiple(self):
        self.assertFalse(Natural().isMultiple(1))
        
    def test2IsNotMultiple(self):
        self.assertFalse(Natural().isMultiple(2))
    
    def test3IsMultiple(self):
        self.assertTrue(Natural().isMultiple(3))
        
    def test4IsNotMultiple(self):
        self.assertFalse(Natural().isMultiple(4))
        
    def test5IsMultiple(self):
        self.assertTrue(Natural().isMultiple(5))
        
    def test6IsMultiple(self):
        self.assertTrue(Natural().isMultiple(6))
        
class NaturalNumberSumTest(unittest.TestCase):
    
    def testSequence1Return0(self):
        self.assertEquals(0, Natural().sum(1))
        
    def testSequence2Return0(self):
        self.assertEquals(0, Natural().sum(2))
        
    def testSequence3Return3(self):
        self.assertEquals(3, Natural().sum(3))
        
    def testSequence4Return3(self):
        self.assertEquals(3, Natural().sum(4))
        
    def testSequence5Return8(self):
        self.assertEquals(8, Natural().sum(5))
        
    def testSequence6Return14(self):
        self.assertEquals(14, Natural().sum(6))
        
    def testSequence7Return14(self):
        self.assertEquals(14, Natural().sum(7))
        
    def testSequence10Return23(self):
        self.assertEquals(23, Natural().sum(9))