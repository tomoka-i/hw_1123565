#Tomoka 1123565
#20241128

import heapq

def addTask(heap, name, priority):
    #using like max heap by multiplying priority by -1
    heapq.heappush(heap, (-priority, name))

def getHighest(heap):
    if heap:
        priority, name = heapq.heappop(heap)
        return name
    return None

def getRemaining(heap):
    #reset priority to their original values
    return [(name, -priority) for priority, name in heap]

def main():
    n = int(input())
    taskHeap = []  

    for _ in range(n):
        command = input().strip().split()
        if command[0] == "ADD":
            name = command[1]
            priority = int(command[2])
            addTask(taskHeap, name, priority)
        elif command[0] == "GET":
            highestTask = getHighest(taskHeap)
            if highestTask:
                print(highestTask)

    remainingTasks = getRemaining(taskHeap)
    print("Remaining tasks:", remainingTasks)

if __name__ == "__main__":
    main()
