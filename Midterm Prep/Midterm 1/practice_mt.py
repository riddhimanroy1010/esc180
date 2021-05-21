''' Problem 1 '''
def second_smallest(nums):
    return sorted(nums)[1]
    
''' Problem 2 '''
def has22(nums):
    for i in range(1, len(nums)):
        if (nums[i] == 2)and (nums[i - 1] == 2):
            return True
    return False

if __name__ == "__main__":
    pass