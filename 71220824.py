def tabung(d,t):
    a = d/2
    vo = 3.14*(a**2)*t
    return vo

def kubus(sisi):
    vok = sisi**3
    return vok

def balok(p,l,t):
    vob = p*l*t
    return vob

print("="*20,"KALKULATOR CERDAS","="*20)
print("Pilihlah bangun yang ingin anda hitung(inputan angka saja): ")
print("1. Tabung")
print("2. Kubus")
print("3. Balok")
mas = int(input(">>"))
if  mas == 1:
    r = int(input("Masukan diameter(cm): "))
    t = int(input("Masukan tinggi(cm): "))
    print(f"Volume Tabung yang di inputkan: {tabung(r,t)} cm")
elif mas == 2:
    sisi = int(input("Masukan sisi: "))
    print(f"Volume Kubus yang di inputkan: {kubus(sisi)} cm")
elif mas == 3:
    p = int(input("Masukan panjang(cm): "))
    l = int(input("Masukan lebar(cm): "))
    t = int(input("Masukan tinggi(cm): "))
    print(f"Volume Balok yang di inputkan: {balok(p,l,t)} cm")
else:
    print("Salah inputan masbro!")

