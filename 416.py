#Questão difícil 416. Partition Equal Subset Sum. Usa o algoritmo de knapsack modificado
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]

solution = Solution()
print(solution.canPartition([1, 5, 11, 5]))
print(solution.canPartition([1, 2, 3, 5])) 