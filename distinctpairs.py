from queue import PriorityQueue
 

def getPairsCount(lists, sum):
    pq = PriorityQueue()
    count = 0  # Initialize result
    s=set()
    
    for i in lists:
        s.add(i)
        pq.put(i)
       
    while not pq.empty():   
        x = pq.get()
        if x+sum in s:
            count += 1
    return count

print(getPairsCount([1,7,5,-1,5],6))