

def check(arra):
    j =0
    for i in range(len(arra)):
        if arra[i][j] == arra[i+1][j] == arra[i+2][j]:
            print(" ifidj")
            return True
       
    return False

print(check([[1, 1, 1],
    [0, 1, 1],
    [0, 1, 1]]))