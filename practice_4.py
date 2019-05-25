#PF-Prac-4
def find_nine(nums):
    for i in range(0,4):
        if(nums[i]==9):
            return True
    else:
        return False

nums=[1, 2,3,4]
print(find_nine(nums))
