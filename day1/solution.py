from utils import generate_sorted_column
file_path = 'day1/input'

col_1 = generate_sorted_column(file_path, 0)  # Sort column 0 in ascending order

col_2 = generate_sorted_column(file_path, 1)  # Sort column 1 in ascending order

dist_sum = 0

dist_sum = sum(abs(x - y) for x, y in zip(col_1, col_2))

print("Distance sum: ", dist_sum)
