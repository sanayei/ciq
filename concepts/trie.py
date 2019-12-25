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



if __name__ == '__main__':
    words = ['ami2323232', 'america', 'amir.sanayei', 'amir']
    trie = Trie()
    for w in words:
        trie.insert(w)
    print(trie.search('amir'))
    print(trie.search('ami'))
    print(trie.startsWith('am'))
