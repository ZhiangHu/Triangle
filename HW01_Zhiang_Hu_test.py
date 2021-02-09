import unittest
from HW01_Zhiang_Hu import Triangle
tr = Triangle()

class Testtriangle(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(tr.triangle(-2, -3, 11), 3)
        self.assertNotEqual(0, tr.triangle(-2, -3, 11))
 
    
    def test2(self):
        self.assertEqual(tr.triangle(3, 4, 5), 1)
        self.assertNotEqual(2, tr.triangle(3, 4, 5))
    
   
    def test3(self):
        self.assertEqual(tr.triangle(8, 8, 8), 3)
        self.assertNotEqual(2, tr.triangle(8, 8, 8))
    
   
    def test4(self):
        self.assertEqual(tr.triangle(8, 8, 6), 2)
        self.assertNotEqual(3, tr.triangle(8, 8, 6))
    
   
    def test5(self):
        self.assertEqual(tr.triangle(1, 2, 3), 0)
        self.assertNotEqual(3, tr.triangle(1, 2, 3))
    
    
    def test6(self):
        self.assertEqual(tr.triangle(3, 6, 4), 1)
        self.assertNotEqual(1, tr.triangle(3, 6, 4))
 
if __name__ == '__main__':
    unittest.main()
