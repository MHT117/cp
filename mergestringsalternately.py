class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])
            i += 1
        return ''.join(res)


if __name__ == "__main__":
    sol = Solution()

    # Sample test cases
    print(sol.mergeAlternately("abc", "pqr"))   # apbqcr
    print(sol.mergeAlternately("ab", "pqrs"))   # apbqrs
    print(sol.mergeAlternately("", "hello"))    # hello
    print(sol.mergeAlternately("world", ""))    # world
    print(sol.mergeAlternately("a", "b"))       # ab
