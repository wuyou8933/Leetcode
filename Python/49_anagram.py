def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for singlestr in strs:
            temp = ''.join(sorted(singlestr))
            if temp not in result:
                result[temp] = []
                result[temp].append(singlestr)
            else:
                result[temp].append(singlestr)
        return [x for x in result.values()]
            
print groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])