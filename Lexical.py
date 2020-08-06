def giveMeLexo(s):
    if len(s) > 2:
        result = []
        for p in range(len(s)): # p is pivot
            for i in [s[p] + x for x in giveMeLexo(s[:p] + s[p+1:])]:
                result.append(i)
        return result
    else: # base case
        return [s, s[1] + s[0]]

def getLexical(s):
    s = ''.join(sorted(list(s))) # Converting intial string in lexical order.
    return list(set(giveMeLexo(s))) # To remove duplicates

print(getLexical('PRAVAKAR'))

