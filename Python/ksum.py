def fourSum(self, num, target):
    num.sort()
    def ksum(num, k, target):
        i = 0
        if k == 2:
            j = len(num) - 1
            while i < j:
                if num[i] + num[j] == target:
                    yield (num[i], num[j])
                    i += 1
                elif num[i] + num[j] > target:
                    j -= 1
                else:
                    i += 1
        else:
            for i in range(len(num) - k + 1):
                for sub in ksum(num[i+1:], k - 1, target - num[i]):
                    yield (num[i],) + sub
        
    
    return [list(t) for t in set(ksum(num, 4, target))]