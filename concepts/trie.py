class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.isEnd = True

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        if not cur.isEnd:
            return False
        return True

    def replaceWithRoot(self, word):
        cur = self.root
        chars = []
        for char in word:
            if char not in cur.children:
                return word
            chars.append(char)
            cur = cur.children[char]
            if cur.isEnd:
                return ''.join(chars)
        return word

    def startsWith(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return []
            cur = cur.children[char]
        if cur.isEnd:
            return [prefix]

        cur.val=''
        res = []

        def dfs(node, path):
            path = path + [node.val]
            if node.isEnd:
                res.append(''.join(path))
            for child in node.children:
                dfs(node.children[child], path)
        dfs(cur, [])
        return [prefix + el for el in res]

    def search2(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.isFound = False

        def dfs(word, cur):
            if len(word) == 0 and cur.isEnd:
                self.isFound = True
                return
            elif word[0] == '.':
                for char in cur.children:
                    dfs(word[1:], cur.children[char])
            else:
                if word[0] in cur.children:
                    dfs(word[1:], cur.children[word[0]])
                else:
                    return

        dfs(word, self.root)
        return self.isFound

if __name__ == '__main__':
    words = [["at"], ["and"], ["an"], ["add"], ["bat"]]
    searchs = [["a"], [".at"], [".at"], ["an."], ["a.d."], ["b."], ["a.d"], ["."]]
    trie = Trie()
    for word in words:
        trie.insert(word)

    for s in searchs:
        print(trie.search2(s))
