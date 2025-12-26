

from collections import defaultdict

def groupAnagrams(strs):

    d = {}

    ans = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)

    x = list(ans.values())
    return x

    # for i in range(len(strs)):
    #     new_d = {}
    #     for letter in strs[i]:
    #         if letter in new_d:
    #             new_d[letter] += 1
    #         else:
    #             new_d[letter] = 1
    #     d[i] = sorted(new_d)

    # print(d)

    # answer = []
    # d2 = {v:k for k,v in d.items()}
    # print(d2)


        



x = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(x)
