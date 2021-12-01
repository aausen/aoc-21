with open("day1.txt") as f:
    nums = [int(line) for line in f.readlines()]



numA = nums[0]
numB = nums[1]
numC = nums[2]

 
def num_of_increase():
    last_num = nums[0]
    num_increase = 0
    for num in nums[1:]:
        if num > last_num:
            num_increase += 1
        last_num = num
    print("number of increases = ", num_increase)

def window_increase():
    total_increase = 0
    for i in range(len(nums) - 3):
       
        sumA = nums[i] + nums[i + 1] + nums[i + 2]
        sumB = nums[i + 1] + nums[i + 2] + nums[i + 3]
        if sumA < sumB:
            total_increase += 1
     
    print("total increase = ", total_increase)