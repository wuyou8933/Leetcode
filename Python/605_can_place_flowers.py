def canPlaceFlowers(self, flowerbed, n):
        flowerbed += [0,1]
        flowerbed = [1,0]+flowerbed
        last = -1
        sum = 0
        for i,num in enumerate(flowerbed):
            if num == 1:
                empty = i-last-1
                last = i
                if empty <=1:
                    continue
                sum += (empty-1) //2
        
        return sum>=n