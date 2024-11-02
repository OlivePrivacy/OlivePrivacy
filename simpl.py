for i in range(2, 90000000000000000000):
    ise = True
    for u in range(2, i):
        t = int(i) % int(u)
        if t == 0:
            ise = False
    if ise:
        print(i)
            
