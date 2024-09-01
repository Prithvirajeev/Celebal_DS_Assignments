#Question: Print the triangle pattern
#Solution : For printing the triangle pattern we shall use loop and function which we have learnt in this weeks lectures 
#Code : 
def print_equilateral_triangle(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

rows = 4
print_equilateral_triangle(rows)


