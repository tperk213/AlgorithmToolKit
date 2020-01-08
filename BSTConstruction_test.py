import BSTConstruction
import unittest

test1 = BSTConstruction.BST(10).insert(5).insert(15).insert(2).insert(14).insert(22)

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(test1.left.value, 5)
    def test_case_2(self):
        self.assertEqual(test1.right.right.value, 22)
    def test_case_3(self):    
        self.assertEqual(test1.right.left.value, 14)
    def test_case_4(self):    
        self.assertEqual(test1.left.right.value, 5)
    def test_case_5(self):    
        self.assertEqual(test1.left.left.value, 2)
    def test_case_6(self):    
        self.assertEqual(test1.left.left.left, None)
    def test_case_7(self):    
        self.assertEqual(test1.right.left.right, None)
    
    
    
    