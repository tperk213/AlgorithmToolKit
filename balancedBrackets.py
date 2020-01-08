def balancedBrackets(string):
# Write your code here.
    brackets = []
    opening = ['[','(','{'] # make hash table for constant look up
    closing = [']',')','}']
    pairs = {
        '[':']',
        '{':'}',
        '(':')'
        }
    for symbol in string:
        if symbol in opening:
            brackets.append(pairs[symbol])
        if symbol in closing:
            if not len(brackets):
                return False
            if brackets[-1] is not symbol:
                return False
            else:
                brackets.pop()
    if not len(brackets):
        return True
    else:
        return False

if __name__ == "__main__":
    a = balancedBrackets("()[]{}{")
    print(a)