class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['#'] = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char in cur:
                cur = cur[char]
            else:
                return False
        if '#' in cur and cur['#']:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char in cur:
                cur = cur[char]
            else:
                return False
        return True


if __name__ == '__main__':
    words = ['amir', 'munira', 'maral', 'mary']
    trie = Trie()
    for w in words:
        trie.insert(w)
    print(trie.search('amir'))
    print(trie.search('Ali'))
    print(trie.startsWith('am'))
