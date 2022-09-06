import math

class MinHeap:
    def __init__(self):
        self.heap = [None]

    def insert(self, num):
        self.heap.append(num)
        heap_len = len(self.heap)
        if len(self.heap) > 2:
            idx = heap_len -1
            while(self.heap[idx] < self.heap[math.floor(idx/2)]):
                #Swap the nodes up the tree
                temp = self.heap[math.floor(idx/2)]
                self.heap[math.floor(idx/2)] = num
                self.heap[idx] = temp
                if(math.floor(idx/2) > 1):
                    idx = math.floor(idx/2)
                else:
                    break
    def remove(self):
        smallest = self.heap[1]
        #check if there are more than 2 elements in the heap
        heap_len = len(self.heap)
        if heap_len > 2 :
            self.heap[1] = self.heap.pop()
            heap_len = len(self.heap)
            #check if there are only three elements
            if heap_len == 3:
                if self.heap[1] > self.heap[2]:
                    temp = self.heap[1]
                    self.heap[1] = self.heap[2]
                    self.heap[2] = temp
                return smallest
            i = 1
            left = 2  * i
            right = 2 * i + 1
            if left >= heap_len or right >= heap_len:
                return smallest

            while self.heap[i] >= self.heap[left] or self.heap[i] >= self.heap[right]:
                if self.heap[left] < self.heap[right]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[left]
                    self.heap[left] = temp
                    i = i * 2
                else:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[right]
                    self.heap[right] = temp
                    i = i * 2 + 1
                
                left = 2 * i
                right = 2 * i + 1
                if left >= heap_len or right >= heap_len:
                    break

        elif heap_len == 2:
            self.heap.pop(1)
        else:
            return None
        
        return smallest

    def sort(self):
        result = list()
        while len(self.heap) > 1:
            result.append(self.remove())

        return result

def main():
    heap_obj = MinHeap()
    test = [3,4,5,19,20,1,4]
    for num in test:
        heap_obj.insert(num)
    
    sorted_arry = heap_obj.sort()
    print(sorted_arry)

if __name__ == "__main__":
    main()
            