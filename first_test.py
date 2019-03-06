# define function that takes two arguments and returns sum
import unittest

def add_two(a,b):
    return a + b

def multiply_two(a,b):
    return a * b

def scalar(my_list,scl):
    for i in range(len(my_list)):
        my_list[i] *= scl
    return my_list

class MyTest(unittest.TestCase):

    def test_add_two(self):
        result = add_two(10,20)
        self.assertEqual(result, 30)
        self.assertEqual(add_two(230, 20), 250)
        self.assertRaises(TypeError, add_two, None, 4)
        self.assertRaises(TypeError, add_two, "Hello", 4.9)

    def test_multiply_two(self):
        self.assertEqual(multiply_two(5,4), 20)
        self.assertEqual(multiply_two(50,4), 200)
        self.assertEqual(multiply_two(-10,-10), 100)

    def test_scalar(self):
        self.assertEqual(scalar([10,20,30,40], 4), [40,80,120,160])
        self.assertEqual(scalar([5,6,7], 4), [20,24,28])
        self.assertEqual(scalar([], 100), [])

if __name__ == "__main__":
    unittest.main()