n = int(input())
nums = []
for i in range(n):
    num = float(input())
    nums.append(num)
for j in range(n):
    for k in range(j):
        if nums[j] > nums[k]:
            nums[k],nums[j] = nums[j],nums[k]

for l in nums:
    print(f'{l:.2f}')
