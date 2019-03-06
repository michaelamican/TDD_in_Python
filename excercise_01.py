import unittest

string = "This is a string"

def min(l):
    # Should find and return minimum value in a given list
    min = l[0]
    for val in l:
        if val < min:
            min = val
    return min
def sum_list(l):
    # Should return total value of all list items
    total = 0
    for val in l:
        total += val
    return total
def less_than(a):
    # Should return a bool of whether given value is less than 100
    return a < 100
### For this exercise, work within this class. This is something you will come up with on your own soon ###
class MainTest(unittest.TestCase):
    def test_min(self):
        result = min([10,3,7,-5,12])
        self.assertEqual(result, -5)
        self.assertEqual(min([-2, 3, 9, -100, 12]), -100)
        self.assertRaises(TypeError, min, [-2, .5], string)
        self.assertRaises(TypeError, min, [string, "a"], "c")
        self.assertRaises(TypeError, min, [-2, .5], 12)
    
    def test_sum_list(self):
        result = sum_list([1, 2, 3, 4, 5])
        self.assertEqual(result, 15)
        self.assertRaises(TypeError, sum_list, [2, 3, 5, string])
        self.assertRaises(TypeError, sum_list, [2, None, 3])
        self.assertRaises(TypeError, sum_list, [2, 3, [4, 5, 6]])
        self.assertRaises(TypeError, sum_list, ["a", "b", "c", "d"])

    def less_than(self):
        result = less_than(20)
        self.assertEqual(result, true)
        self.assertRaises(TypeError, less_than, None)
        self.assertRaises(TypeError, less_than, [2,101])
        self.assertRaises(TypeError, less_than, string)

if __name__ == "__main__":
    unittest.main()