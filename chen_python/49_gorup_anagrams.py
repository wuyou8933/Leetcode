def groupAnagrams(strs):
    ans = dict()
    for s in strs:
    	if tuple(sorted(s)) not in ans.keys():
    		ans[tuple(sorted(s))]=[]
    		ans[tuple(sorted(s))].append(s)
    	else:
    		ans[tuple(sorted(s))].append(s)
        
        
        
    return ans.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))