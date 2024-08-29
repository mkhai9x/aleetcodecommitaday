class TriNode:
    def __init__(self, char) -> None:
        self.char = char
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TriNode(None)

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TriNode(char)
            curr_node = curr_node.children[char]
        curr_node.is_word = True

    def search_dfs(self, curr_node, next_char_index, word) -> bool:
        if next_char_index == len(word):
            return curr_node.is_word

        next_char = word[next_char_index]

        if next_char != "." and next_char not in curr_node.children:
            return False

        if next_char == ".":
            result = False
            for chil in curr_node.children.values():
                result = self.search_dfs(chil, next_char_index + 1, word)
                if result:
                    return result
            return result

        else:
            return self.search_dfs(
                curr_node.children[next_char], next_char_index + 1, word
            )

    def search(self, word: str) -> bool:
        curr_node = self.root

        return self.search_dfs(curr_node, 0, word)


word_dict = WordDictionary()

word_dict.addWord("bad")
word_dict.addWord("dad")
word_dict.addWord("mad")
word_dict.addWord("made")

print(word_dict.search("pad"))
print(word_dict.search("bad"))
print(word_dict.search(".ad"))
print(word_dict.search("b.."))
print(word_dict.search("b."))
