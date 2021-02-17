# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#         self.nums = nums
#         self.index = 0

#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#         return self.index < len(self.nums)

#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
#         result = self.numbs[self.index]
#         self.index += 1
#         return result

    
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.has_next = self.iterator.hasNext()
        
        self.peeked = False


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeked and not self.iterator.hasNext():
            return None

        if not self.peeked:            
            self.peeked = self.iterator.next()
            self.has_next = True

        return self.peeked

    def next(self):
        """
        :rtype: int
        """

        if not self.peeked:
            return self.iterator.next()
        
        response = self.peeked
        
        self.peeked = False
        self.has_next = False

        return response


    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.peeked:
            return self.iterator.hasNext()

        
        return self.has_next
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].