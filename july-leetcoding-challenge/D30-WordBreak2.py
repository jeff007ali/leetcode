def wordBreak(s, wordDict):
    def helper(s, wordDict, memo):
        if s in memo: 
            return memo[s]

        if not s:
            return []

        ans = []
        for word in wordDict:
            if not s.startswith(word):
                continue

            if len(word) == len(s):
                ans.append(word)
            else:
                res = helper(s[len(word):], wordDict, memo)
                for item in res:
                    item = word + ' ' + item
                    ans.append(item)

        memo[s] = ans

        return ans 

    return helper(s, wordDict, {})


print(wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
# print(wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
# print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))