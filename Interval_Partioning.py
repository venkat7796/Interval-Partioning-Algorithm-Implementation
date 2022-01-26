import heapq
def interval_partioning(schedule):
    schedule.sort()
    minHeap = []
    heapq.heappush(minHeap,schedule[0][1])
    for i in range(1,len(schedule)):
        if minHeap[0] <= schedule[i][0]:
            heapq.heappop(minHeap)
        heapq.heappush(minHeap,schedule[i][1])
    return len(minHeap)

k = interval_partioning([[1,4],[3,5],[0,6],[4,7],[3,8],[5,9],[6,10],[8,11]])
print(k)
    
