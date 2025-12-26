def alphabetSort(str):
    sorted_str = sorted(str)
    return ''.join(sorted_str)

def groupAnagrams(strs):
    
    l = []

    for s in strs:
        l.append(alphabetSort(s))

    unique = list(dict.fromkeys(l))
    answer = []

    for i in range(len(unique)):
        sub_answer = []
        word = unique[i]
        for j in range(len(l)):
            if word == l[j]:
                sub_answer.append(strs[j])
        answer.append(sub_answer)

    return answer

# ASS RUNTIME




x = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(x)

