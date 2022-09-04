mucahityilmazmy = {"m":1,"u":2,"c":3,"a":4,"h":5,"i":6,"t":7,
                   "y":8,"i":9,"l":10,"m":11,"a":12,"z":13,
                   "m":14,"y":15}

m = [[1, 2, -1], [2, 5, 2], [-1, -2, 2]]

def sifre(isim):
    u = []
    for c in isim:
        u.append(c)
    a = []
    for h in isim:
        a.append(mucahityilmazmy.get(h))
    istanbul = a[0:3]   #değişkenim kalmadı bende yaşadığım şehirleri yazdım hocam :D
    kocaeli = a[3:6]
    diyarbakir = a[6:9]
    izmir = a[9:12]
    amasya = a[12:15]
    t = [istanbul,kocaeli,diyarbakir,izmir,amasya]
    y = []
    for l in t:
        for z in m:
            print("makris çarpımı",l,z)
            my = z[0]*l[0],z[1]*l[1],z[2]*l[2]
            print(my)
            tokat = 0
            for niksar in my:
                tokat += niksar
            print(tokat)
            y.append(tokat)
        print("şifre:",y)

tokat60 = sifre("mucahityilmazmy")