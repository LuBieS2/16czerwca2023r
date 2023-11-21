def sorting(s, T):
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if czy_mniejszy(s, T[i] - 1, T[j] - 1)==False:
               T[j], T[i]=T[i], T[j]
def loaddata(text):
    file=open(text, "r")
    data=list(map(str.strip, file.readlines()))
    return data
def czy_mniejszy(s, k1, k2):
    n=len(s)-1
    i=k1
    j=k2
    while i<=n and j<=n:
        if s[i]==s[j]:
            i+=1
            j+=1

        else:
            if s[i]<s[j]:
                return True
            else:
                return False
    if j<=n:
        return True
    else:
        return False
def zad2_2():
    words=loaddata("slowa3.txt")
    words[2]=words[2].split(" ")
    print(words)
    s=words[1]
    k1=int(words[2][0])
    k2=int(words[2][1])
    print(czy_mniejszy(s, k1, k2))
def zad2_3():
    T=[]
    s="kalafiorowa"
    sl=[]
    for i in range(1,len(s)+1):
        T.append(i)
    for i in s:
        sl.append(i)
    m=[]
    for l1 in range(len(s)-2):
        for l2 in range(len(s)-l1-1):
            if l2 ==l1:
                continue
            if czy_mniejszy(sl, l1, l2):
                k1 = T[l1]
                T[l1] = T[l2]
                T[l2] = k1
                k1=sl[l1]
                sl[l1]=sl[l2]
                sl[l2]=k1
            print(T)
    print(T)
    print(sl)
def zad23XD():
    T=[]
    s="kalafiorowa"
    for i in range(1,len(s)+1):
        T.append(i)
    print(T)

    sorting(s, T)
    print(T)
def zad2_4():
    words=loaddata("slowa4.txt")
    words=[item.split(" ") for item in words]
    print(words)
    p=[]
    for word in words:
        s=[]
        for i in word[1]:
            s.append(i)
        T = []
        for i in range(1, len(s) + 1):
            T.append(i)
        sorting(s, T)
        p.append(T[0])
    for index, postition in enumerate(p):
        print(words[index][1][postition-1:])

#zad2_4()
def zad3_1():
    binary=loaddata("anagram.txt")
    print(binary)
    nearlybalanced=[]
    balanced=[]
    for number in binary:
        one=0
        zero=0
        for i in number:
            if int(i)==0:
                one+=1
            else:
                zero+=1
        if one==zero:
            balanced.append(number)
        if one+1==zero or zero+1==one:
            nearlybalanced.append(number)
    print(len(balanced), len(nearlybalanced))
def zad3_2():
    binary=loaddata("anagram.txt")
    a=[]
    for number in binary:
        if len(number)==8:
            a.append(number)
    longestlist=[[0]]
    for n, number in enumerate(a):
        lst=[]
        one=0
        zero=0
        lst.append(number)
        for d in number:
            if int(d)==0:
                zero+=1
            else:
                one+=1
        bins=[]
        for i in range(128,256):
            b=bin(i)[2:]
            bins.append(b)
        lst=[]
        lst.append(number)
        for b in bins:
            if str(b)==str(number):
                pass
            else:
                zero1=0
                one1=0

                for d in b:
                    if int(d)==0:
                        zero1+=1
                    else:
                        one1+=1
                if one1==one and zero==zero1:

                    lst.append(b)
        if len(lst)>len(longestlist[0]):
            longestlist=[]
            longestlist.append(lst)
        elif len(lst)==len(longestlist[0]):
            longestlist.append(lst)
    for i in longestlist:
        print(i[0])
def zad3_3():
    binary=loaddata("anagram.txt")
    t=[]
    for i in binary:
        t.append(int(i,2))
    print(t)
    highestvalue=0
    for i in range(1, len(t)-1):
        r1=abs(t[i]-t[i-1])
        r2=abs(t[i]-t[i+1])
        r=0
        if r1>r2:
           r=r1
        else:
            r=r2
        if r>highestvalue:
            highestvalue=r
    print(bin(highestvalue)[2:])
def zad3_4():
    binary=loaddata("anagram.txt")
    t=[]
    tl=[]
    for i in binary:
        t.append(str(int(i,2)))
    for number in t:
        m=[]
        for d in number:
            m.append(int(d))
        tl.append(m)
    nozero=[]
    for number in tl:
        zero=0
        for i in number:
            if i==0:
              zero+=1
        if zero==0:
            nozero.append(number)
    print(len(nozero))
    hs=0
    hn=0
    for n, number in enumerate(tl):
        number=set(number)

        s=0
        for i in number:
            s+=i
        if s>hs:
            hs=s
            hn=t[n]
zad3_4()