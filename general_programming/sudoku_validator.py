# this is program to validate sudoku board
# row and columnwise validate
# blockwise validate

def rows_and_cols(sudoku_mat):

	rows_list = [{None} for i in range(9)]
	cols_list = [{None} for i in range(9)]

	for i in range(9):
		for j in range(9):
			el = sudoku_mat[i][j]
			if el == 0:
				continue
			if el in rows_list[i] or el in cols_list[j]:
				return False
			else:
				rows_list[i].add(el)
				cols_list[j].add(el)
	return True

def block_val(sudoku_mat):
	block_set = [{None} for i in range(9)]

	for i in range(3):
		for j in range(3):
			for m in range(3):
				for n in range(3):
					curr_row = m + i * 3
					curr_col = n + j * 3
					b_no = i * 3 + j
					el = sudoku_mat[curr_row][curr_col]
					if el == 0:
						continue
					elif el in block_set[b_no]:
						return False 
					else:
						block_set[b_no].add(el)
	return True

def sudoku_validator(sudoku_mat):
	return rows_and_cols(sudoku_mat) and block_val(sudoku_mat)

def main():
	sudoku_mat = [	

					[8, 0, 0, 4, 0, 6, 0, 0, 7],
					[0, 0, 0, 0, 0, 0, 4, 0, 0],
					[0, 1, 0, 0, 0, 0, 6, 5, 0],
					[5, 0, 9, 0, 3, 0, 7, 8, 0],
					[0, 0, 0, 0, 7, 0, 0, 0, 0],
					[0, 4, 8, 0, 2, 0, 1, 0, 3],
					[0, 5, 2, 0, 0, 0, 0, 9, 0],
					[0, 0, 1, 0, 0, 0, 0, 0, 0],
					[3, 0, 0, 0, 9, 0, 2, 0, 5]
				 ]
	print(sudoku_validator(sudoku_mat))


main()