NUM = 100

num_list = range(1, NUM + 1)
square_of_sum = sum(num_list) ** 2
sum_of_square = sum([ i*i for i in num_list])

print square_of_sum - sum_of_square
