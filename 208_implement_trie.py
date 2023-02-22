class Trie:

    def __init__(self):
        self.trie =[]
        

    def insert(self, word: str) -> None:
        self.trie.append(word)
        

    def search(self, word: str) -> bool:
        return word in self.trie
        

    def startsWith(self, prefix: str) -> bool:
        pref_len = len(prefix)
        for i in self.trie:
            temp = i[0:pref_len]
            if temp == prefix: return True
        
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)