def closest_to_zero(nums):
    closest = nums[0]
    for x in nums:
        if abs(x) < abs(closest):
            closest = x
            
    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest
            
if __name__ == "__main__":
    
    test_cases = [
        ([-4, -2, 1, 4, 8], 1),
        ([5, -3, -3, 7], -3),          
        ([-10, 0, 10], 0),
        ([-1, -2, -3], -1),
        ([4, 6, 8], 4)
    ]

    all_passed = True
    for nums, expected in test_cases:
        result = closest_to_zero(nums)
        if result == expected:
            print(f" {nums} -> {result}")
        else:
            print(f" {nums} -> {result} (expected {expected})")
            all_passed = False

    if all_passed:
        print("All tests passed.")