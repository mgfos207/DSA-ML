def robFrom(i, nums, memo, count=None):

    curr_num = None
    try:
        curr_num = nums[i]
    except:
        curr_num = "out of bounds"
    print(f"Current index: {i}, Current num: {curr_num}, One or Two Indexes Ahead: {count}, Length of Array: {len(nums)}")
    # No more houses left to examine.
    if i >= len(nums):
        print("No more houses left to examine")
        # print(i, len(nums))
        return 0
    
    # Return cached value.
    if i in memo:
        print("Cached the result")
        return memo[i]
    
    # Recursive relation evaluation to get the optimal answer.
    ans = max(robFrom(i + 1, nums, memo, "plus 1"), robFrom(i + 2, nums, memo, "plus 2") + nums[i])
    # print(ans, i, nums[i])
    print("The answer and index", ans, i)
    # Cache for future use.
    memo[i] = ans
    return ans

if __name__ == "__main__":
    # max_house = robFrom(0, [2,1,4,5,8,8,9,10], {})
    max_house = robFrom(0, [2,1,4,5], {})

    # print(max_house)