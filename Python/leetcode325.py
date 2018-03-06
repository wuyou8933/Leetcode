def maxSubArrayLen(self, nums, k):

        result, acc = 0, 0
        dic = {0: -1}

        for i in xrange(len(nums)):
            acc += nums[i]
            if acc not in dic:
                dic[acc] = i
            if acc - k in dic:
                result = max(result, i - dic[acc-k])

        return result