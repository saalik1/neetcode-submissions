class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        # since heapq only uses minheaps we gotta reverse to get negative
        # that means assume 5 is the biggest -5 will be smallest
        heap = []
        for x in stones:
            x = x*-1
            heapq.heappush(heap,x)

        while len(heap)>1:
            x = heapq.heappop(heap)*-1
            y = heapq.heappop(heap)*-1
            if x==y:
                pass
            
            if x<y:
                y = y-x
                heapq.heappush(heap,-y)
            if y<x:
                x = x-y
                heapq.heappush(heap,-x)
            
        if len(heap) == 0:
            return 0
        else:
             return (heap[0]*-1)