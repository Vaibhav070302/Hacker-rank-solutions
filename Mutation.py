def mutate_string(string, position, character):
    snew= s[:position] + character + s[position+1:]
    
    return snew

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
