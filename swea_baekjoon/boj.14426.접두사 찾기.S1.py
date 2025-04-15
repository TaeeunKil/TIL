class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def prefix_check(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

trie = Trie()


N, M = map(int, input().split())


for _ in range(N):
    word = input()
    trie.insert(word)


ans =0
for _ in range(M):
    word = input()
    if trie.prefix_check(word):
        ans +=1

print(ans)