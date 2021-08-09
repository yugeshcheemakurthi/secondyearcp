# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(l):
    x=[]
    for i in range(len(l[0])):
        if (l[0][i] not in x):
            x.append(l[0][i])
        else:
            return False
    for j in range(len(l)):
        c=[]
        r=[]
        for k in range(len(l[j])):
            if l[j][k] not in x:
                return False
            else:
                if l[k][j] not in c:
                    c.append(l[k][j])
                else:
                    return False
                if l[j][k] not in r:
                    r.append(l[j][k])
                else:
                    return False
        print('row',r)
        print('col',c)
                
    return True
