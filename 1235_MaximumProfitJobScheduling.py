from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #Ordenar por tempo de término
        tarefas = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        startTime, endTime, profit = zip(*tarefas)
        
        #p(j) com busca binária
        def p(j):
            left, right = 0, j - 1
            while left <= right:
                mid = (left + right) // 2
                if endTime[mid] <= startTime[j]:
                    if endTime[mid + 1] <= startTime[j]:
                        left = mid + 1
                    else:
                        return mid
                else:
                    right = mid - 1
            return -1
        
        n = len(tarefas)
        mv = [0]*n #memoization
        mv[0] = profit[0]
        
        for i in range(1, n):
            #Não levar
            NE = mv[i-1]
            
            #Levar
            prev_index = p(i)
            ET = profit[i] + (mv[prev_index] if prev_index != -1 else 0)
            
            mv[i] = max(NE, ET)
        
        return mv[-1]