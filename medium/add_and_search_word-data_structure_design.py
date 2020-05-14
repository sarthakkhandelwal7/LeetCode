from collections import defaultdict


class Node:
    # Trie Tree node
    def __init__(self):
        self.next = defaultdict(Node)
        self.is_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for char in word:
            curr = curr.next[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def helper(i, curr):
            if i == len(word):
                return curr.is_word

            if word[i] == '.':
                return any(helper(i + 1, next_node) for next_node in curr.next.values())

            if word[i] not in curr.next:
                return False

            return helper(i + 1, curr.next[word[i]])

        return helper(0, self.root)
