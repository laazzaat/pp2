def spy_game(nums):
    stroka = ""
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            stroka = stroka + str(nums[i])
        else:
            continue
    if "007" in stroka:
        return True
    else:
        return False

nums = list(map(int, input().split()))
print(spy_game(nums))