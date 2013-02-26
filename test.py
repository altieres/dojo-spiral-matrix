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
		self.matrix = [[0 for i in range(columns)] for i in range(lines)]
		self.lines = lines
		self.columns = columns
		self.current = 1
		self.curr_line = 0
		self.curr_column = 0
		self.inc_line = 0
		self.inc_column = +1
		
	def compute(self):
		self.computeStep()
		return self.matrix
		
	def computeStep(self):
		self.assingAndIncCurrent()
		if not self.hasMoreElements():
			return
		if self.mustChangeDirection():
			if self.inc_line != 0:
				self.inc_line *= -1
			aux = self.inc_line
			self.inc_line = self.inc_column
			self.inc_column = aux

		self.curr_line += self.inc_line
		self.curr_column += self.inc_column
		self.computeStep()
			
	def assingAndIncCurrent(self):
		self.matrix[self.curr_line][self.curr_column] = self.current
		self.current += 1
		
	def hasMoreElements(self):
		return self.current <= self.lines * self.columns
	
	def mustChangeDirection(self):
		try:
			if self.matrix[self.curr_line + self.inc_line][self.curr_column + self.inc_column] != 0:
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



