import heapq

def scheduling(tasks, n):
    def sort_key(x):
      return x[0]

    tasks.sort(key=sort_key, reverse=True)
    
    maxDeadline = max(task[1] for task in tasks)
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