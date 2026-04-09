# 2. Prefix  based Suggestion

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

    def suggest(self, prefix: str, limit: int) -> list:
        prefix = prefix.lower().strip()
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []                        
            node = node.children[char]

        results = []
        self._dfs(node, prefix, results, limit)
        return results

    def _dfs(self, node, current_word, results, limit):
        if len(results) >= limit:
            return
        if node.is_end:
            results.append(current_word)
        for char, child in sorted(node.children.items()):  
            if len(results) >= limit:
                break
            self._dfs(child, current_word + char, results, limit)


# ─────────────────────────────────── Examples ──────────────────────────────────────
if __name__ == "__main__":

    d = Dictionary()

    d.add_word("apple")
    d.add_word("app")
    d.add_word("apply")
    d.add_word("application")
    d.add_word("apt")
    d.add_word("bat")
    d.add_word("batch")
    d.add_word("ball")
    d.add_word("python")
    d.add_word("program")

    print("=" * 50)
    print("  PREFIX-BASED SUGGESTIONS")
    print("=" * 50)

    tests = [
        ("app", 3),  
        ("app", 5), 
        ("ba",  3), 
        ("pro", 5), 
        ("xyz", 3), 
    ]

    for prefix, limit in tests:
        result = d.suggest(prefix, limit)
        print(f"\n  suggest('{prefix}', {limit})")
        print(f"  → {result if result else '[]  # no matches found'}")

