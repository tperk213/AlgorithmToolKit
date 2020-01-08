
#Graph problem

#using hashtable
#Time (O(d))
#space (O(d))
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    ancestors = {}
    node = descendantOne
    while node.ancestor != None:
        node = node.ancestor
        ancestors[node.name] = True
        
    node = descendantTwo.ancestor
    while node.name not in ancestors:
        node = node.ancestor
    return node

#not using hashtable but comparing depths and checking ancestors at same depth
#time(O(d))
#Space(O(1))




#Graph 

#TopAncestor is the stoping point
#create hashtable for descendantOne
#enter ancestor as key and level of ancestory 
#when at topAncestor stop
#travel back from descendant Two
#if ancestor in hash table break and return ancestor
