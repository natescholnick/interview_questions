class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        stack = []
        stack.append(([], s))
        sols = []
        while stack:
            wordchain, remaining = stack.pop()
            if not remaining:
                sols.append(' '.join(wordchain))
            else:
                for word in wordDict:
                    if remaining.startswith(word):
                        newchain = wordchain[:]
                        newchain.append(word)
                        stack.append((newchain, remaining[len(word):]))
        return sols
