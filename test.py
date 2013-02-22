import unittest

class TestSequenceFunctions(unittest.TestCase):

	def test_oneOne(self):
		expected = [[1]]
		matrix = Matrix()
		self.assertEquals(expected, matrix.compute())
		

class Matrix:
	
	def compute(self):
		return [[1]]
		

if __name__ == '__main__':
    unittest.main()
