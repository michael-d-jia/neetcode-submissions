class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a map
        # make an array of length of list + 1
        count = {}
        freq = [[] for i in range (len(nums) + 1)]

        # record counts of each distinct integer in map
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # add distinct integer to array based on count
        # [0 |    1    |  2  | 3 | ...]
        # [  | [1 , 3] | [2] | ... ]
        for n, c in count.items():
            freq[c].append(n)

        # create result array
        res = []

        # loop starting from length of freq array going down to 0
        # since starting from the end, these are the highest and once we append k number of ints, we have our result
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        