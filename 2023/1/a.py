import sys

data = open("2023/1/text.txt").read().strip()

sum = 0

for line in data.split("\n"):
    nums = []
    for x, char in enumerate(line):
        if char.isdigit():
            nums.append(char)
        numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        for i, val in enumerate(numbers):
            if line[x:].startswith(val):
                nums.append(str(i))    
    digit = int(nums[0]+nums[-1])
    sum += digit

print(sum)