import heapq

def read_column(file_path, column_index):
    with open(file_path, 'r') as file:
        for line in file:
            values = line.split()
            yield int(values[column_index])

def generate_sorted_column(file_path, column_index, reverse=False):
    column_generator = read_column(file_path, column_index)
    sorted_values = []

    if reverse:
        for value in column_generator:
            heapq.heappush(sorted_values, -value)
        while sorted_values:
            yield -heapq.heappop(sorted_values)
    else:
        for value in column_generator:
            heapq.heappush(sorted_values, value)
        while sorted_values:
            yield heapq.heappop(sorted_values)

