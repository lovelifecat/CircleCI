# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')


    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 should be a isosceles triangle')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 should be a Equilateral Triangle')

    def TestScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be a scalene triangle')

    def testValidInputButNotATriangle(self):
        self.assertEqual(classifyTriangle(1,2,5),'NotATriangle','1,2,5 should be a valid input but not a triangle')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

