def swap_case(s):
    a=list(s)
    b=list()
    for i in range(len(a)):
       if a[i].islower():
           b.append(a[i].upper())
       else:
           b.append(a[i].lower())
        
    res="".join(b)

    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
