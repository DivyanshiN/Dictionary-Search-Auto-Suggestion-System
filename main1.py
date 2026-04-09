# 1. Word Search

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.definition = None
        self.frequency = 0


class Dictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str, definition: str = ""):
        word = word.lower().strip()
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.definition = definition

    def search(self, word: str) -> dict:
        word = word.lower().strip()
        node = self.root

        for char in word:
            if char not in node.children:
                return {"status": "NOT FOUND", "word": word, "frequency": 0}
            node = node.children[char]

        if node.is_end:
            node.frequency += 1
            return {"status": "FOUND", "word": word, "frequency": node.frequency, "definition": node.definition}

        return {"status": "NOT FOUND", "word": word, "frequency": 0}


# ─── Example ────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":

    d = Dictionary()

    d.add_word("apple")
    d.add_word("app")
    d.add_word("python")
    d.add_word("batch")

    queries = ["apple", "python", "apple", "ghost", "ap", "PYTHON", "xyz"]

    for q in queries:
        r = d.search(q)
        if r["status"] == "FOUND":
            print(f"FOUND     | '{r['word']}' | searched {r['frequency']} time(s) | {r['definition']}")
        else:
            print(f"NOT FOUND | '{q}'")
