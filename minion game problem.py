def minion_game(string):
    K=0
    S=0
    V="AEIOU"
    for i in range(len(string)):
        if string[i] in v:
            K+=len(string)-i
        else:
            S+=len(string)-i
    if K>S:
        print("Kevin",K)
    elif
        S>K print("Stuart",S)
    else: 
        print("Draw")
            
