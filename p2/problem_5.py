## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        self.children[char] = TrieNode()
        
    def suffixes(self):
        suffixes = []
        for child in self.children:
            if self.children[child].is_word:
                suffixes.append(child)
            child_suffixes = self.children[child].suffixes()
            for cs in child_suffixes:
                suffixes.append(child + cs)
        return suffixes
        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
                continue
            else:
                current_node.insert(letter)
                current_node = current_node.children[letter]
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if not prefix:
            return False
        current_node = self.root
        for letter in prefix:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return False
        return current_node

# Tests
tn = TrieNode()
tn.insert('a')
assert type(tn.children['a']) == type(TrieNode())
print(tn.children.keys())
# dict_keys(['a'])

t = Trie()
assert type(t.root) == type(TrieNode())
print(type(t.root))
# <class '__main__.TrieNode'>

t.insert('at')
assert list(t.root.children.keys()) == ['a']
print(list(t.root.children.keys()))
# ['a']
assert t.root.children['a'].is_word == False
print(t.root.children['a'].is_word)
# False
assert list(t.root.children['a'].children.keys()) == ['t']
print(list(t.root.children['a'].children.keys()))
# ['t']
assert t.root.children['a'].children['t'].is_word == True
print(t.root.children['a'].children['t'].is_word)
# True

node = t.find('a')
assert node == t.root.children['a']
print(node == t.root.children['a'])
# True

node = t.find('at')
assert node == t.root.children['a'].children['t']
print(node == t.root.children['a'].children['t'])
# True

node = t.find('b')
assert node == False
print(node == False)
# True

assert t.root.suffixes() == ['at']
print(t.root.suffixes() == ['at'])
# True

node = t.find('a')
assert node.suffixes() == ['t']
print(node.suffixes() == ['t'])
# True
