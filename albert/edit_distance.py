class Solution:

    memo = {}

    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if (word1, word2) in self.memo:
            return self.memo[(word1, word2)]

        mincost = max(len(word1), len(word2))
        for i in range(len(word1)):
            if i > mincost:
                break
            for j in range(len(word2)):
                if j > mincost:
                    break
                if word1[i] == word2[j]:
                    minlen = max(i, j) + self.minDistance(word1[i + 1:], word2[j + 1:])
                    mincost = min(minlen, mincost)

        self.memo[(word1, word2)] = mincost
        return mincost
