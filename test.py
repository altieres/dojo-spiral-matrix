import unittest

class TestSequenceFunctions(unittest.TestCase):

	def testOneOne(self):
		expected = [[1]]
		matrix = Matrix(1)
		self.assertEquals(expected, matrix.compute())
		
	def testOneThree(self):
		expected = [[1, 2, 3]]
		matrix = Matrix(3)
		self.assertEquals(expected, matrix.compute())
		

class Matrix:
	
	def __init__(self, columns):
		self.columns = columns
		
	def compute(self):
		matrix = [[0 for i in range(self.columns)]]
		for column in range(self.columns):
			matrix[0][column] = column + 1
		return matrix
		

if __name__ == '__main__':
    unittest.main()
