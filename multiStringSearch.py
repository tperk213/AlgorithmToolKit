
def multiStringSearch(bigString, smallStrings):
    found = [False for i in range(len(smallStrings))]
    base = makeTrie(smallStrings)
    for i in range(len(bigString)):
        node = base
        j = i
        while j < len(bigString):
            if bigString[j] in node:
                node = node[bigString[j]]
            else:
                break
            if '*' in node:
                found[node['*']] = True
            j += 1
    return found

def makeTrie(smallStrings):
    trie = {}
    for i in range(len(smallStrings)):
        node = trie
        for l in smallStrings[i]:
            if l not in node:
                node[l] = {}
            node = node[l]
        node['*'] = i
    return trie
if __name__ == "__main__":
    smallStrings = ["the", "tree", "can", "copy"]
    bigString = "the tree is copy"
    k = multiStringSearch(bigString, smallStrings)
    print(k)
