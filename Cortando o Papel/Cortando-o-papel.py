 # Número de retângulos
N = input()

# Alturas
A = [int(x) for x in input().split()]

new_heights = []
new_heights.append([A[0], 0])

ascending = True if A[0] < A[1] else False
for i in range(1, len(A)):
        actual_ascending = True if A[i - 1] < A[i] else False
        if actual_ascending != ascending:
            new_heights.append([A[i - 1], new_heights[-1][1] + 1])
            ascending = actual_ascending

if A[-2] != A[-1]:
      new_heights.append([A[-1], new_heights[-1][1] + 1])


sorted_heights = new_heights[:]
sorted_heights.sort()

start = 0 if new_heights[0] > new_heights[1] else 1
max_count = 2
count = 1
for h in reversed(sorted_heights):
        if (h[1] - start) % 2 == 0:
            count += 1
        elif h != new_heights[0][1] and h != new_heights[-1]:
            count -= 1

        if count > max_count:
            max_count = count

print(max_count)