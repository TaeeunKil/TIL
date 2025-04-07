N, M = map(int, input().split())


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

trie = Trie()

for _ in range(N):
    word = input()
    trie.insert(word)

print(trie.root)
ans =0
for _ in range(M):
    word = input()
    if trie.search(word):
        ans +=1

print(ans)