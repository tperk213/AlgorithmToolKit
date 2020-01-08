


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        #base case
        
        cur_tree = self.root
        #make a branch from sub_string
        for char in string:
            if char in cur_tree:
                cur_tree = cur_tree[char]
            else:
                cur_tree[char] = {}
                cur_tree = cur_tree[char]
        cur_tree[self.endSymbol] = True
        #add substrings
        if len(string) == 1:
            return
        self.populateSuffixTrieFrom(string[-(len(string)-1):])
        return self
        
    def contains(self, string):
        # Write your code here.
        cur_tree = self.root
        for char in string:
            if char in cur_tree:
                cur_tree = cur_tree[char]
            else:
                return False
        if self.endSymbol in cur_tree:
            return True
        else:
            return False


if __name__ == "__main__":
    a = SuffixTrie("tomatoe")
    print("done")