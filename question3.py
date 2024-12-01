#Tomoka 1123565
#20241128

import heapq

def merge(arrays):
    minPriQue = []
    result = []

    for i in range(len(arrays)):
        #add the first elements of each arrays to min prority heap
        if arrays[i]:
            heapq.heappush(minPriQue, (arrays[i][0], i, 0))

    while minPriQue:
        #add the minimum elements in min priority heap to result list
        value, arrIdx, elemIdx = heapq.heappop(minPriQue)
        result.append(value)

        #add next minimum element of the array containing the current minimum element
        if elemIdx + 1 < len(arrays[arrIdx]):
            nextVal = arrays[arrIdx][elemIdx + 1]
            heapq.heappush(minPriQue, (nextVal, arrIdx, elemIdx + 1))

    return result

def main():
    k = int(input("Enter the number of sorted arrays (K): "))
    arrays = []

    for _ in range(k):
        arr = list(map(int, input().split()))
        arrays.append(arr)

    mergedArr = merge(arrays)
    print("Merged Array:", mergedArr)

if __name__ == "__main__":
    main()
