#Tomoka 1123565
#20241128

import heapq

def scheduling(tasks, n):
    #sort tasks by highest profit
    def sortKey(x):
      return x[0]

    tasks.sort(key=sortKey, reverse=True)
    
    #get the longest deadline
    maxDeadline = max(task[1] for task in tasks)
    #implement 1-based index by adding 1
    slots = [False] * (maxDeadline + 1)
    
    maxProfit = 0
    scheduledTasks = []

    for profit, deadline in tasks:
        for i in range(min(deadline, maxDeadline), 0, -1):
            if not slots[i]:
                slots[i] = True
                maxProfit += profit
                scheduledTasks.append(profit)
                break

    return maxProfit, scheduledTasks

def main():
    n = int(input("Enter the number of tasks: "))
    tasks = []
    print("Enter profit and deadline: ")
    for _ in range(n):
        profit, deadline = map(int, input().split())
        tasks.append((profit, deadline))
    
    maxProfit, scheduledTasks = scheduling(tasks, n)

    print(f"Maximum Profit: {maxProfit}")
    print(f"Scheduled Tasks: {scheduledTasks}")

if __name__ == "__main__":
    main()