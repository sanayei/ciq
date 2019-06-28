def groupAnagrams(strs):
    #  O(nklogk) n = number of strings, k = maximum length of strings
    # d = {}
    # for s in strs:
    #     key = tuple(sorted(s))
    #     if key in d:
    #         d[key].append(s)
    #     else:
    #         d.update({key: [s]})
    # return list(d.values())

    # O(nk) n = number of strings, k = maximum length of strings
    from collections import defaultdict
    d = defaultdict(list)
    for s in strs:
        letters = [0] * 26
        for c in s:
            letters[ord(c) - ord('a')] += 1
        d[tuple(letters)].append(s)
    return list(d.values())

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))