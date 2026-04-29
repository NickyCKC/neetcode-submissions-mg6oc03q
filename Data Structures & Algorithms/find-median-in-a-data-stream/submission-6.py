class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        arr = self.arr
        arr.append(num)
        arr.sort()
        
    def findMedian(self) -> float:
        arr = self.arr
        length = len(arr)
        odd = length % 2
        print(length, odd)
        if odd:
            return arr[int(length / 2)]
        else:
            lower = arr[length // 2 - 1]
            upper = arr[length // 2]
            return (lower + upper) / 2
            