class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False

    def __repr__(self) -> str:
        return f"curr char: {self.char} with children \n {self.children}"


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode(char)
            curr_node = curr_node.children[char]

        curr_node.is_word = True

    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        return curr_node.is_word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return True


trie = Trie()

trie.insert("hellow")
trie.insert("helloworld")
trie.insert("hellothere")
print(trie.search("helloworld"))
print(trie.search("hellothere"))
print(trie.search("hello"))
print(trie.startsWith("hello"))
