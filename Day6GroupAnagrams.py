class Solution:
    def groupAnagrams(self, strs):

        new_list = [''.join(sorted(i)) for i in strs]
        dic = {}

        for i in range(len(new_list)):
            if new_list[i] not in dic:
                dic[new_list[i]] = [strs[i]]
            else:
                dic[new_list[i]].append(strs[i])
        return dic.values()


def main():
    anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solve = Solution()
    print(solve.groupAnagrams(anagrams))


if __name__ == '__main__':
    main()
