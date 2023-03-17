class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        tree = self.trie
        for k in range(len(word)):
            if word[k] not in tree:
                tree[word[k]]={}
            tree = tree[word[k]]
        tree[''] = 1

    def search(self, word: str) -> bool:
        tree = self.trie
        for k in range(len(word)):
            if word[k] not in tree:
                return False
            tree=tree[word[k]]
        if tree.get('', None):
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        tree = self.trie
        for k in range(len(prefix)):
            if prefix[k] not in tree:
                return False
            tree=tree[prefix[k]]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)