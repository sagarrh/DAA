def subsets_with_sum(nums, target_sum):
    def backtrack(start, path_sum, path):
        # If the current subset sum equals the target sum, add it to the result
        if path_sum == target_sum:
            all_subsets.append(path[:])
            return
        
        # Explore all possible subsets by adding numbers to the current subset
        for i in range(start, len(nums)):
            # Include the current number in the subset
            path.append(nums[i])
            # Recur with the updated sum and path
            backtrack(i + 1, path_sum + nums[i], path)
            # Backtrack by removing the current number from the subset
            path.pop()
    
    all_subsets = []
    backtrack(0, 0, [])
    return all_subsets

# Example usage:
nums = [ 2, 3, 5, 6, 8, 10]
target_sum = 10
print("Subsets with sum", target_sum, ":", subsets_with_sum(nums, target_sum))
