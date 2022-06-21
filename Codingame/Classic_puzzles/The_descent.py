while True:
    maxx=-1
    im=-1
    for i in range(8):
        mh = int(input())
        if mh>maxx:
            im=i
            maxx=mh
    print(im)
