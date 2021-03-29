class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        index_to_remove = []

        for n in range(len(nums)):
            if nums[n] == val:
                index_to_remove.append(n)

        offset = 0
        for index in index_to_remove:
            del nums[index - offset]
            offset += 1
        return len(nums)