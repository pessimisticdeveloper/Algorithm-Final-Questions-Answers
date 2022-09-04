m_liste = []

for u in range(1,30):
    if u > 1:
        for c in range(2,u):
            if u % c ==0:
                break
        else:
            m_liste.append(u)

print("1 ile 30 arasındaki asal sauılar =",m_liste)