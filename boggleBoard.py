#better way then below is to make a suffix trie and loop through the grid using
# depth first search to find matches in the trie will be faster then below

def boggleBoard(board, words):
#board is 2d matrix can be non square
# word is list of words to find
    found_words = []
    for word in words: 
        if searchForFirstLetter(board, word):
            found_words.append(word)
    return found_words
def searchForFirstLetter(board, word):
    for row in range(len(board)):
        for col in range(len(board[0])):
            pos_table = {}
            if board[row][col] == word[0]:
                #found start search for word
                idx = str(row) + str(col)
                pos_table[idx] = True
                if search(board, row, col, word[1:], pos_table) is True:
                    return True
    return False
def search(board, row, col, word, pos_table):
    #base case
    if len(word) == 0:
        #found whole word
        return True
    npos = {key:item for key, item in pos_table.items()}
    npos[str(row)+str(col)] = True
    
    cur_l = word[0]
    #Find available search positions
    available_positions = []
    if row > 0:
        available_positions.append([row-1, col])
        if col > 0:
            available_positions.append([row-1, col-1])
        if col < len(board[0])-1:
            available_positions.append([row-1, col+1])
    if col < len(board[0])-1:
        available_positions.append([row, col+1])
    if col > 0:
        available_positions.append([row, col-1])
    if row < len(board)-1:
        available_positions.append([row+1, col])
        if col > 0:
            available_positions.append([row+1, col-1])
        if col < len(board[0])-1:
            available_positions.append([row+1, col+1])
    
    for nxt_row, nxt_col in available_positions:
        if board[nxt_row][nxt_col] == cur_l and not (str(nxt_row) + str(nxt_col) in npos):
            # pos_table[str(nxt_row)+str(nxt_col)] = True
            if search(board, nxt_row, nxt_col, word[1:], npos) == True:
                return True
    
    return False

if __name__ == "__main__":
    b = ['com',
    'rpl',
    'cit',
    'oae',
    'fod',
    'zrb',
    'gia',
    'oag',
    'fsz',
    'tei',
    'twd']
    board = [[l for l in st] for st in b]
    print(board)
    words = ['cr',
             'oc',
             'ml',
             'iao', 
             'opo', 
             'zrb',
             'big',
             'fs',
             'ogiagao',
             'dwd',
             'twt'
             ]

    found = boggleBoard(board, words)
    print(found)


#treat letters on board as nodes
#similar to rivers example
#if letter found and last letter return True
#if not last letter 
# cur node = -1
# node = new_position 
# and repeat 
#else if not found
# go to next node on origional board 



#board is 2d matrix can be non square
# word is list of words to find

#treat letters on board as nodes
#similar to rivers example
#search all valid areas around the current node for nxt letter
#if letter found and last letter return True
#if not last letter 
# cur node = -1
# node = new_position 
# and repeat 
#else if not found
# go to next node on origional board 







