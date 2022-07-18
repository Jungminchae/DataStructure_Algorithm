from collections import defaultdict
def groupAnagrams(strs):
    strs_dict = defaultdict(list)
    for str in strs:
        word = "".join(sorted(str))
        if word in strs_dict.keys():
            strs_dict[word].append(str)
        else:
            strs_dict[word] = [str]
    answer = list(strs_dict.values())
    answer = sorted(answer, key=lambda x: len(x))
    return answer
