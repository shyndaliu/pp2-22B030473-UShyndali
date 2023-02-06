def has_33(nums):
    for i in range(1,len(nums)-1,1):
        if(nums[i]==3 and nums[i-1]==3):
            return True
    return False

print(has_33([1,2,3,3,4,5]))
print(has_33([1,2,3,5,4,5]))
