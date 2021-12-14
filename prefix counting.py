a = [3, 14, 25, 26, 32, 40, 45, 52, 60, 69, 72, 77, 80, 84, 90, 93]  #DEFINE THE ARRAY IN HERE
q = int(input("Enter your integer "))


def pre_(q):
    n = len(a)
    L = 0
    R = n - 1
    if q == 0:
        print("Bye！")  #ENTER 0 TO TERMINATE THE PROGRAM
        return -1
    if q < a[0]:
        print('No prefix and predecessor')
        exit(0)
    elif q > a[R]:
        return R
    while L <= R:
        m = (L+R)//2
        if a[m] == q:
            return m
        elif a[m] > q:
            R = m-1
        else:
            L = m+1
    return m-1



while pre_(q) != -1:
    m = pre_(q)
    print('There are : {} prefixes.'.format(m+1))
    print('The predecessor is : {} '.format(a[m]))
    q = int(input("Enter your integer "))
