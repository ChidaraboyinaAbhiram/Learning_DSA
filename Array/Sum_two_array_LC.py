def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


print("This is brute force approach (using nested loop)")
print(two_sum([2, 7, 11, 15], 9))


def Two_sum(nums, target):
    hash_Map = {}
    for i in range(len(nums)):
        search_value = target - nums[i]
        if search_value in hash_Map:
            return [i, hash_Map[search_value]]
        hash_Map[nums[i]] = i


print("This is hash map approach")
print(Two_sum([2, 7, 11, 15], 9))