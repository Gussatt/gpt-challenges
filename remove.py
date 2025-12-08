def remove(nums, val):
    i = len(nums) - 1
    k = 0

    for n in range(i):
        if nums[n] == val:
            nums.append(nums[n])
            nums[n] = 0
    
    for j in range(i):
        if nums[j] == val or nums[j] == 0:
            nums.pop(j)
        else:
            k+=1

    print(k)
    print(nums)

nums =[0,1,2,2,3,0,4,2]
val = 2

print(remove(nums,val))