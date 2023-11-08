n = int(input())

num_desc = [i for i in range(n, n//2, -1)]
num_asc = [i for i in range(1, n//2+1)]

nums = []

while num_desc or num_asc:
    if num_desc:
        nums.append(num_desc.pop(0))
    if num_asc:
        nums.append(num_asc.pop(0))

for num in nums:
    print('* ' * num)

for num in nums[::-1]:
    print('* ' * num)