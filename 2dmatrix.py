matrix = [
  [1, 2, 3],  # Row 0
  [4, 5, 6],  # Row 1
  [7, 8, 9]   # Row 2
]

sum_main = sum_second = 0

for r in range(len(matrix)):
    sum_main += matrix[r][r]
    
    i = 0
for c in range(len(matrix)-1,-1, -1):
    sum_second += matrix[c][i]
    i += 1
    
print(sum_main)
print(sum_second)