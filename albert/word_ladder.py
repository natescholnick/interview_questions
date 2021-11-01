class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 1

        def sameness(word1, word2):
            samecount = 0
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    samecount += 1
            return samecount
                
            
        stack = []
        stack.append((beginWord, set(wordList), 1))
        curr_min = None
        while stack:
            word, available_words, steps = stack.pop()
            endsame = sameness(word, endWord)
            if curr_min and steps + 1 > curr_min:
                continue

            if sameness(word, endWord) == len(endWord) - 1:
                curr_min = steps + 1

            adjacent_words = [
                aw for aw in available_words
                if sameness(word, aw) == len(word) - 1
                and sameness(aw, endWord) >= endsame
            ]

            for aw in adjacent_words:
                new_available_words = available_words.copy()
                new_available_words.remove(aw)
                stack.append(((aw, new_available_words, steps + 1)))
        
        if not curr_min:
            return 0

        return curr_min
