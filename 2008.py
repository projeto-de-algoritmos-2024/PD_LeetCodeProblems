#Questão difícil 2008. Maximum Earnings From Taxi. Usa o algoritmo de Weigthed Interval Scheduling
import bisect

class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        rides.sort(key=lambda x: x[1])
        end_times = [ride[1] for ride in rides]
        dp = [0] * (len(rides) + 1)

        for i in range(1, len(rides) + 1):
            start, end, tip = rides[i-1]
            earnings = end - start + tip
            j = bisect.bisect_right(end_times, start) - 1
            dp[i] = max(dp[i-1], earnings + (dp[j+1] if j >= 0 else 0))

        return dp[-1]

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (5, [[2,5,4], [1,5,1]]),
        (20, [[1,6,1], [3,10,2], [10,12,3], [11,12,2], [13,18,1]])
    ]
    
    for i, (n, rides) in enumerate(test_cases):
        print(f"Caso de teste {i+1}: {solution.maxTaxiEarnings(n, rides)}")