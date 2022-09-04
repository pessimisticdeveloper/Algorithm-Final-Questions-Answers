m_sayi = int(input("bir sayi giriniz: "))

def f(m_Sayi):
    if 9 <= m_sayi < 16:
        return m_sayi*2
    elif 9 > m_sayi >= 0:
        carpim = 1

        for u in range(m_sayi):
            carpim *= u + 1

        print(carpim*3)
    elif m_sayi <= 0:
        return "negatif sayı girdiniz..."
    else:
        return "16'dan büyük sayı girdiniz..."

print(f(m_sayi))