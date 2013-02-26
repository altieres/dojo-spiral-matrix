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


class MatrixBase:
	def __init__(self, lines, columns):
		self.matrix = [[0 for i in range(columns)] for i in range(lines)]
		
	def raw(self):
		return self.matrix
		
	def assign(self, curr_line, curr_column, current):
		self.matrix[curr_line][curr_column] = current
		
	def isZero(self, line, column):
		try:
			if self.matrix[line][column] == 0:
				return True
		except:
			return False
		return False
		
		
class Matrix:
	
	def __init__(self, lines, columns):
		self.matrix = MatrixBase(lines, columns)
		self.lines = lines
		self.columns = columns
		
	def compute(self):
		self.current = 1
		self.curr_line = 0
		self.curr_column = 0
		self.inc_line = 0
		self.inc_column = +1
		self.computeStep()
		return self.matrix.raw()
		
	def computeStep(self):
		self.assingAndIncCurrent()

		if self.mustChangeDirection():
			self.changeDirection()

		if self.hasMoreElements():
			self.incrementAndCallRecursively()
			
	def assingAndIncCurrent(self):
		self.matrix.assign(self.curr_line, self.curr_column, self.current)
		self.current += 1
		
	def mustChangeDirection(self):
		return not self.matrix.isZero(self.curr_line + self.inc_line, self.curr_column + self.inc_column)
		
	def changeDirection(self):
		if self.inc_line != 0:
			self.inc_line *= -1
		aux = self.inc_line
		self.inc_line = self.inc_column
		self.inc_column = aux
		
	def hasMoreElements(self):
		return self.current <= self.lines * self.columns

	def incrementAndCallRecursively(self):
		self.curr_line += self.inc_line
		self.curr_column += self.inc_column
		self.computeStep()
		

if __name__ == '__main__':
    unittest.main()

