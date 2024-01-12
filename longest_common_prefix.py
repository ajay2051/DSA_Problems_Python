# Common leading prefix
def longest_common_prefix(strs):
    longest_pre = []
    if strs and len(strs) > 0:
        strs = sorted(strs)
        # e.g. before sort: ["flower","flow","flight","fake"]
        # after sort: ['fake', 'flight', 'flow', 'flower']
        first, last = strs[0], strs[-1]
        for i in range(len(first)):
            if len(last) > i and last[i] == first[i]:
                longest_pre.append(last[i])
            else:
                return "".join(longest_pre)
    return "".join(longest_pre)


result = longest_common_prefix(('flake', 'flight', 'flow', 'flower'))
print(result)
