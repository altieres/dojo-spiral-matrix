import unittest

class TestSequenceFunctions(unittest.TestCase):

	def testOneOne(self):
		matrix = Matrix(1, 1)
		expected = [[1]]
		self.assertEquals(expected, matrix.compute())
		
	def testOneThree(self):
		matrix = Matrix(1, 3)
		expected = [[1, 2, 3]]
		self.assertEquals(expected, matrix.compute())
		
	def testLastColumn(self):
		matrix = Matrix(3, 3).compute()
		for line in range(3):
			self.assertEquals(line+3, matrix[line][2])
	
	def testThreeThree(self):
		matrix = Matrix(3, 3).compute()
		expected = [[1, 2, 3],
								[8, 9, 4],
								[7, 6, 5]]
		self.assertEquals(expected, matrix)
			
	def testFourSix(self):
		matrix = Matrix(4, 6).compute()
		expected = [[ 1,  2,  3,  4,  5,  6],
								[16, 17, 18, 19, 20,  7],
								[15, 24, 23, 22, 21,  8],
								[14, 13, 12, 11, 10,  9]]
		self.assertEquals(expected, matrix)


class Matrix:
	
	def __init__(self, lines, columns):
		self.current = 1
		self.lines = lines
		self.columns = columns
		self.matrix = [[0 for i in range(self.columns)] for i in range(self.lines)]
		
	def compute(self):
		self.computeStep(0, 0, 0, +1)
		return self.matrix
		
	def computeStep(self, curr_line, curr_column, inc_line, inc_column):
		self.assingAndIncCurrent(curr_line, curr_column)
		if not self.hasMoreElements():
			return
		if not self.mustChangeDirection(curr_line, curr_column, inc_line, inc_column):
			self.computeStep(curr_line + inc_line, curr_column + inc_column, inc_line, inc_column)
		else:
			if inc_line != 0:
				inc_line *= -1
			aux = inc_line
			inc_line = inc_column
			inc_column = aux
			self.computeStep(curr_line + inc_line, curr_column + inc_column, inc_line, inc_column)
			
	def assingAndIncCurrent(self, curr_line, curr_column):
		self.matrix[curr_line][curr_column] = self.current
		self.current += 1
		
	def hasMoreElements(self):
		return self.current <= self.lines * self.columns
	
	def mustChangeDirection(self, curr_line, curr_column, inc_line, inc_column):
		try:
			if self.matrix[curr_line + inc_line][curr_column + inc_column] != 0:
				return True
		except:
			return True
		return False
			
if __name__ == '__main__':
    unittest.main()


#0 +1
#+1 0
#0 -1
#-1 0



