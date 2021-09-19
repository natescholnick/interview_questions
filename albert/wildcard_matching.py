class Solution:
    
    calc = {}
    
    def isMatchSolver(self, s: str, p: str) -> bool:
        if (s, p) in self.calc:
            return self.calc[(s, p)]

        if len(p) <= 1:
            if p == '*':
                self.calc[(s, p)] = True
                return True
            elif p == '?':
                res = len(s) == 1
                self.calc[(s, p)] = res
                return res
            else:
                res = s == p
                self.calc[(s, p)] = res
                return res

        else:
            if p[0] == '*':
                for j in range(max(len(s), 1)):
                    if self.isMatchSolver(s[j:], p[1:]):
                        self.calc[(s, p)] = True
                        return True
                self.calc[(s, p)] = False
                return False
            elif not s:
                res = not p
                self.calc[(s, p)] = res
                return res
            elif p[0] != '?' and s[0] != p[0]:
                self.calc[(s, p)] = False
                return False
            else:
                return self.isMatchSolver(s[1:], p[1:])

    
    def isMatch(self, s: str, p: str) -> bool:
        clean_p = ''
        last_p = ''
        for c in p:
            if c == '*' and last_p == '*':
                continue
            clean_p += c
            last_p = c
        print(s, p, clean_p)
        return self.isMatchSolver(s, clean_p)
