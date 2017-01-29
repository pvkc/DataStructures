"""Binary Heap implementation, the input to the heap is array of objects
parent(i) = i/2
left(i) = 2*i
right(i) = 2*i + 1"""
from random import randint


class MinBinaryHeap(object):
    def __init__(self,values):
        self.heap = [None]
        self._size = 0
        for value in values:
            self.insert(value)

    def _parent(self, pos):
        return self.heap[pos//2]

    @staticmethod
    def _parent_pos(pos):
        return pos//2

    def _left_child(self, pos):
        """For a given node in the heap
            Return the left_child and the left_child position, if exists"""
        if 2*pos > self._size:
            return None, None
        else:
            return self.heap[2*pos], 2*pos

    def _right_child(self, pos):
        """For a given node in the heap
            Return the right_child and right_child position, if exists"""
        if 2*pos + 1 > self._size:
            return None, None
        else:
            return self.heap[(2*pos)+1], 2*pos + 1

    def _find_min_child_pos(self,pos):
        """For a given Node Return the position of immediate child which has minimum value"""
        left_child, left_child_pos = self._left_child(pos)
        right_child, right_child_pos = self._right_child(pos)
        # if curr node in heap has both left and right child
        #       return the position of node with min value
        # else return the position of the left_child or right_child which ever exists
        # if no child exists return None
        if left_child and right_child:
            if left_child < right_child:
                return left_child_pos
            else:
                return right_child_pos
        else:
            return left_child_pos or right_child_pos

    def insert(self, value):
        """Insert value in to the Minimum Binary heap.
            The heap is expected to be a min heap before the insertion of value """
        self.heap.append(value)
        self._size +=1
        if self._size == 1:
            return

        curr_pos = self._size
        while curr_pos > 1:
            if self._parent(curr_pos) > value:
                self.heap[curr_pos], self.heap[MinBinaryHeap._parent_pos(curr_pos)] = \
                    self.heap[MinBinaryHeap._parent_pos(curr_pos)], self.heap[curr_pos]
            curr_pos //= 2

    def extract_min(self, **kwargs):
        """Delete the minimum of the binary heap and return the value"""
        if self._size == 0:
            return "Empty Heap"

        # Copy the min value and return it in the end
        min_val = self.heap[1]
        # Swap the root and the last leaf of the heap, delete the last leaf
        self.heap[1], self.heap[self._size] = self.heap[self._size], self.heap[1]
        del self.heap[self._size]
        self._size -= 1
        # Repair the min heap property after the swap.
        # Starting from the root, swap the parent with the minimum of the two children, till we only have leafs.
        # All the elements with index > size//2 are the leafs of the heap
        curr_pos = 1
        while curr_pos <= (self._size//2):
            min_child_pos = self._find_min_child_pos(curr_pos)
            if self.heap[curr_pos] > self.heap[min_child_pos]:
                self.heap[curr_pos], self.heap[min_child_pos] = self.heap[min_child_pos], self.heap[curr_pos]
            else:
                break
            curr_pos = min_child_pos

        return min_val

    def sort(self):
        """The heap is sorted"""
        sorted_arr = []
        if self._size == 0:
            return "Empty Heap"
        for i in range(0,self._size):
            sorted_arr.append(self.extract_min())
        return sorted_arr

    def __str__(self):
        if self._size > 0:
            return str(self.heap[1:self._size+1])
        else:
            return ""


if __name__ == '__main__':
    from heapq import heapify, heappop
    arr = [randint(11,5000) for i in range(1000)]
    #arr = [16, 19, 37, 54, 75, 74, 40, 99, 86, 94]
    heap = MinBinaryHeap(arr)
    print("Heap: ", heap)
    heapify(arr)
    print("Heapify: ", arr)
    #print("Heap: ", heap.sort())
    assert sorted(arr) == heap.sort()
    #for i in range(10):
    #    #print(heap.extract_min())
    #    #print(heappop(arr), end="\n")
    #    assert heap.extract_min() == heappop(arr)
    #    print("Heap: ", heap, end="\n")
    #    print("Heapify: ", arr, end="\n\n")