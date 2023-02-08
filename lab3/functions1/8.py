def spy_game(nums, cnt = 0):
    for i in range(len(nums)- 1):
        if nums[i] == 0 and nums[i] == nums[i+1]:
            if nums[i+2] == 7:
                cnt += 1 
    if cnt > 0:
        return True
    else:
        return False



a = list(map(int, input().split()))
print(spy_game(a))

#spy_game([1,2,4,0,0,7,5]) --> True
#spy_game([1,0,2,4,0,5,7]) --> True
#spy_game([1,7,2,0,4,5,0]) --> False