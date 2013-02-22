import unittest

class TestSequenceFunctions(unittest.TestCase):

	def testOneOne(self):
		expected = [[1]]
		matrix = Matrix(1, 1)
		self.assertEquals(expected, matrix.compute())
		
	def testOneThree(self):
		expected = [[1, 2, 3]]
		matrix = Matrix(1, 3)
		self.assertEquals(expected, matrix.compute())
		
	def testLastColumn(self):
		matrix = Matrix(3, 3).compute()
		for line in range(3):
			self.assertEquals(line+3, matrix[line][2])
			

class Matrix:
	
	def __init__(self, lines, columns):
		self.lines = lines
		self.columns = columns
		self.matrix = [[0 for i in range(self.columns)] for i in range(self.lines)]
		
	def compute(self):
		for line in range(self.lines):
			for column in range(self.columns):
				self.matrix[line][column] = column + line + 1
		return self.matrix
		

if __name__ == '__main__':
    unittest.main()
