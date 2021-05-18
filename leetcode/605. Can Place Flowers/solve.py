class Solution:
    
    def canPlaceFlower(self, index, flowerbed):
        if flowerbed[index-1] == 1:
            return False
        if flowerbed[index+1] == 1:
            return False
        return True

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0)
        flowerbed.append(0)
        max_flowers = 0
        for index in range(1, len(flowerbed)-1):
            if flowerbed[index] == 1:
                continue
            if self.canPlaceFlower(index, flowerbed):
                max_flowers+=1
                flowerbed[index] = 1
        return max_flowers>=n
