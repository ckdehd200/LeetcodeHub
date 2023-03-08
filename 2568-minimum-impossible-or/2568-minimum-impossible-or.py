import heapq

class Solution:
#     def __init__(self):
#         self.ran = [1<<e for e in range(28)]
        
#     def highestbit(self, n):
#         for k in range(28):
#             if self.ran[k]==n:
#                 return k
            
#         l,r = 0,28
#         while l<r:
#             mid = (l+r)//2
#             if n < self.ran[mid]:
#                 r = mid-1
#             else:
#                 l = mid
        # return mid
    def highestbit(self, n):
        e=-1
        while n:
            n>>=1
            e+=1
        return e
    
    def minImpossibleOR(self, nums: List[int]) -> int:
        m = max(nums)
        nums.sort(reverse=True)
        heap = list(map(lambda x:-x, nums))
        unsolved = []
        while len(heap)>1:
            a=-heapq.heappop(heap)
            b=-heapq.heappop(heap)
            # print('heap:', heap)
            if a==b:
                heapq.heappush(heap, -a)
            else:
                c = a|b
                if c<a and c<b:
                    heapq.heappush(heap, -c)
                else:
                    unsolved.append(a)
                    heapq.heappush(heap, -b)
        unsolved.append(-heap[0])
        # print(unsolved)
        for e in range(40):
            if (1<<e) not in unsolved:
                return 1<<e
            