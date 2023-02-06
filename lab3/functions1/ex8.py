def spy_game(nums):
    for i in range(2,len(nums)-1,1):
        if(nums[i]==7 and nums[i-1]==0 and nums[i-2]==0):
            return True
    return False

print(spy_game([1,2,0,0,7,5]))
print(spy_game([1,0,3,0,7,5]))
