
scores = [3, 5, 2, 9, 0, 7, 0, 0]
count = 0
def minimax(index, depth, is_max):
global count
if depth == 3:
 count += 1
return scores[index]
left = minimax(index * 2, depth + 1, not is_max)
right = minimax(index * 2 + 1, depth + 1, not is_max)
if is_max:
return max(left, right)
else:
return min(left, right)
result = minimax(0, 0, True)

print("Minimax Value:", result)
print("Leaves Checked:", count)


