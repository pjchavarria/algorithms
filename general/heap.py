from math import floor

class Solution(object):
    def __init__(self):
        self.array = []

    def insert(self, number):
        self.array.append(number)
        self.bubble_up(len(self.array)-1)


    def extract(self):
        if not len(self.array):
            return None

        element = self.array[0]
        self.array[0] = self.array.pop()
        self.bubble_down(0)
        return element

    def heapify(self, A):
        self.array = A
        for idx in reversed(xrange(1, len(A)/2)):
            self.bubble_down(idx)

    def getMin(self):
        print self.array
        return self.array[0]


    def bubble_up(self, i):
        while self.array[i] < self.array[i/2]:
            aux = self.array[i]
            self.array[i] = self.array[i/2]
            self.array[i/2] = aux
            i = i/2

    def bubble_down(self, i):
        leftChildIndex = i*2+1
        rightChildIndex = i*2+2
        largest = i

        if len(self.array) > leftChildIndex and self.array[largest] > self.array[leftChildIndex]:
            largest = leftChildIndex
        if len(self.array) > rightChildIndex and self.array[largest] > self.array[rightChildIndex]:
            largest = rightChildIndex

        if largest != i:
            aux = self.array[i]
            self.array[i] = self.array[largest]
            self.array[largest] = aux

            self.bubble_down(largest)

            print "After Extraction:"
            print self.array
            





heap = Solution()
heap.insert(2)
heap.insert(1)
heap.insert(5)
heap.insert(4)
heap.insert(3)
heap.insert(40)
heap.insert(-1)
heap.insert(0)

heap.extract()
heap.extract()
heap.extract()

print "Min"
print heap.getMin()




