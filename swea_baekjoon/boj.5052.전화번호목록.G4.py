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
            if node.is_end:
                return True
        return True


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    trie = Trie()
    is_consistent = True
    for i in range(n):
        numbers = input()
        if trie.prefix_check(numbers):
            is_consistent = False
            for _ in range(n-i-1):
                input()
            break
        trie.insert(numbers)
    if not is_consistent:
        print('NO')
    else:
        print('YES')
