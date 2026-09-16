class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
         # close in terms of distance
        # so pop, turn into distance, push onto heap
        # then it tuns into the other problem
        # so basc only have max k at a time
        # if more than k then pop the biggest distance somehow
        # cd use negative thingy here to make sure he pop the biggest   distance
        # then return the entire thing

        import heapq
        heap = []

        for point in points:
            ans = []
            distance = (point[0]**2+point[1]**2)
            ans.append(distance*-1)
            ans.append(point)

            if len(heap)<k:
                heapq.heappush(heap,ans)
            else:
                if ans[0]*-1 < heap[0][0]*-1:
                    heapq.heappop(heap)
                    heapq.heappush(heap,ans)
        
        final = []
        for i in range(len(heap)):
            final.append(heap[i][1])

        return final



