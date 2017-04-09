# -*- coding: utf-8 -*-
from tkinter import *

#ilk iki satır Program başlığı
pencere = Tk()
pencere.title("Ceasar Şifreleme Yöntemi")
#şifreleme algoritması
def Sifreleme():
    # İlk olarak şifreli metinde yazımız varsa temizliyelim
    sifrelimetin.delete(0.0, END)
    # Alfabemizi tanımıyoruz kullanmak istediğimiz alfabeye göre değişiklik yapabiliriz istersek
    alfabe = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r",
             "s",
             "ş", "t", "u", "ü", "v", "y", "z"]
    harfsayisi =len(alfabe)
    # Metni aldırıyoruz baştan sona kadar diyor kısaca
    metin = list(sifresizmetin.get(0.0, END))
    # Metindeki harf sayısı kadar işlem yapıcağı için uzunluğunu aldık ve for döngüsü ile işleme alıcaz
    metinuzunlugu = int(len(metin))
    for i in range(metinuzunlugu):
        # metin string olduğu için char(karakter) dizisi olarak alabiliyoruz bu sayede metine dizi olarak bakıyoruz
        # metin dizisindeki i. harfi buluyoruz
        harf = str(metin[i])
        #try ile harf dışındaki karakterleri kontrol ettiriyoruz
        try:
            #eğer harfin sırası belli ise 3 sonrasını aldırıp yeni harfi elde ediyoruz
            harfbulma = int(alfabe.index(harf)) + 3
            # Eğer listemizin uzunluğuna aşarsa en başa dönmesi için yeniden belirlemeliyiz
            if harfbulma>harfsayisi:
                harfbulma=harfbulma-harfsayisi
            # yeni harfi alıyoruz
                yeniharf= str(alfabe[harfbulma])
                #metindeki yeni harfin yerine yazıdırıyoruz
                metin[i] = yeniharf
            #eğer bir hata alırsak ne yapması gerektiğini söyliyelim şimdi
        except:
            #alfabe de olmadığı için herhangi bir değişikliğe uğramadan aynı yerine yazdırmış oluyoruz
            metin[i] = harf
            # Son olarakta dizimizi döngü ile texte yazdırıyoruz
    for karakterler in metin:
        sifrelimetin.insert(INSERT,karakterler)

#şifre çözme algoritması
def SifreCoz():
    # şifreli metinde yazımız varsa temizliyelim ilk olarak
    sifresizmetin.delete(0.0, END)
    # Alfabemizi tanımıyoruz kullanmak istediğimiz alfabeye göre değişiklik yapabiliriz istersek
    alfabe = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r",
              "s",
              "ş", "t", "u", "ü", "v", "y", "z"]
    # Metni aldırıyoruz baştan sona kadar diyor kısaca
    metin = list(sifrelimetin.get(0.0, END))
    # Metindeki harf sayısı kadar işlem yapıcağı için uzunluğunu aldık ve for döngüsü ile işleme alıcaz
    metinuzunlugu = int(len(metin))
    for i in range(metinuzunlugu):
        # metin string olduğu için char(karakter) dizisi olarak alabiliyoruz bu sayede metine dizi olarak bakıyoruz
        # metin dizisindeki i. harfi buluyoruz
        harf = str(metin[i])
        # try ile harf dışındaki karakterleri kontrol ettiriyoruz
        try:
            # eğer harfin sırası belli ise 3 sonrasını aldırıp yeni harfi elde ediyoruz
            harfbulma = int(alfabe.index(harf)) -3
            # yeni harfi alıyoruz
            yeniharf = str(alfabe[harfbulma])
            # metindeki yeni harfin yerine yazıdırıyoruz
            metin[i] = yeniharf
            # eğer bir hata alırsak ne yapması gerektiğini söyliyelim şimdi
        except:
            # alfabe de olmadığı için herhangi bir değişikliğe uğramadan aynı yerine yazdırmış oluyoruz
            metin[i] = harf
            # Son olarakta dizimizi döngü ile texte yazdırıyoruz
    for karakterler in metin:
        sifresizmetin.insert(INSERT, karakterler)

etiket = Label(text="Metni Giriniz : ")
etiket.pack()
#Girilecek metin ve ayarları
sifresizmetin = Text()
sifresizmetin.config(width=30, height=5, font="arial 12")
sifresizmetin.pack()

etiket = Label(text="Şifreli Metin: ")
etiket.pack()
# Şifreli metinin yeri ve ayarları
sifrelimetin = Text()
sifrelimetin.config(width=30, height=5, font="arial 12")
sifrelimetin.pack()
# Şifrelettirme butonu ve ayarları
sifreleme = Button(text=" Şifrele ", command=Sifreleme)
sifreleme.pack()
# Şifre Çözdürme butonu ve ayarları
sifrecozme= Button(text="Şifre çöz", command=SifreCoz)
sifrecozme.pack()

mainloop()