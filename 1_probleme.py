def fileToStr(cheminFichier="/Users/wandrille/Desktop/Programation/Python/Advent of Code/5_decembre/input.txt"):
    str=""
    with open(cheminFichier, 'r') as input:
        for char in input:
            str+=char
    return str[:-1]
    
def simplification(str):
    for i in range(1, len(str)):
        if (str[i]==str[i-1].lower() and str[i-1].isupper()) or (str[i]==str[i-1].upper() and str[i-1].islower()):
            if i!=len(str):
                str=str[:i-1] + str[i+1:]
                return str
            else:
                str=str[i-1]
                return str
    return str
    
def repeatSimplification(str2):
    while simplification(str2)!=str2:
        str2=simplification(str2)
    return str2