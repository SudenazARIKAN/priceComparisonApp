import tkinter as tk #frame için tkinter çağırdım (tkinter gui penceresinde frame oldu.)
from tkinter import simpledialog, messagebox #tkinterin alt modülü simple dialog kullanıcan basit girdiler alıyor,yine tkinterın alt modülü olan message box kullanıcıya mesajları gösteriyor.

# Mağaza bilgilerini içeren liste 
magazalar = [
    {"ad": "Magaza1", "urunler": {"Laptop": 4500, "Telefon": 2500, "Tablet": 1200, "Kamera": 1800, "Kulaklık": 150}},#Magazadaki ürünler ve fiyatlarını sözlük veri yapısı kullanarak tuttum
    {"ad": "Magaza2", "urunler": {"Laptop": 4200, "Telefon": 2600, "Tablet": 1100, "Kamera": 1900, "Kulaklık": 130}},
    {"ad": "Magaza3", "urunler": {"Laptop": 4800, "Telefon": 2400, "Tablet": 1250, "Kamera": 1700, "Kulaklık": 160}}
]

def urun_ekle():
    magaza_adi = simpledialog.askstring("Mağaza Ekle", "Mağaza adını girin:")#simpledialogla aldığım cevaplar string veri tipinde tutuluyor.
    urun_adi = simpledialog.askstring("Ürün Ekle", "Ürün adını girin:")
    urun_fiyati = float(simpledialog.askstring("Ürün Ekle", "Ürün fiyatını girin:"))

    magaza = next((m for m in magazalar if m["ad"] == magaza_adi), None)

    if magaza:
        if urun_adi in magaza["urunler"]:
            messagebox.showinfo("Hata", f"{magaza_adi} mağazasında {urun_adi} ürünü zaten bulunuyor.")
        else:
            magaza["urunler"][urun_adi] = urun_fiyati
            messagebox.showinfo("Başarı", f"{magaza_adi} mağazasına {urun_adi} ürünü eklendi. Fiyat: {urun_fiyati} TL.")
    else:
        messagebox.showinfo("Hata", f"{magaza_adi} mağazası bulunamadı.")

def fiyat_guncelle():
    magaza_adi = simpledialog.askstring("Fiyat Güncelle", "Mağaza adını girin:")
    urun_adi = simpledialog.askstring("Fiyat Güncelle", "Güncellenecek ürün adını girin:")
    yeni_fiyat = float(simpledialog.askstring("Fiyat Güncelle", "Yeni fiyatı girin:"))

    magaza = next((m for m in magazalar if m["ad"] == magaza_adi), None)

    if magaza and urun_adi in magaza["urunler"]:
        magaza["urunler"][urun_adi] = yeni_fiyat
        messagebox.showinfo("Başarı", f"{magaza_adi} mağazasındaki {urun_adi} ürününün fiyatı güncellendi. Yeni fiyat: {yeni_fiyat} TL.")
    else:
        messagebox.showinfo("Hata", f"{magaza_adi} mağazası veya {urun_adi} ürünü bulunamadı.")

def urun_sil():
    magaza_adi = simpledialog.askstring("Ürün Sil", "Mağaza adını girin:")
    urun_adi = simpledialog.askstring("Ürün Sil", "Silinecek ürün adını girin:")

    magaza = next((m for m in magazalar if m["ad"] == magaza_adi), None)

    if magaza and urun_adi in magaza["urunler"]:
        del magaza["urunler"][urun_adi]
        messagebox.showinfo("Başarı", f"{magaza_adi} mağazasındaki {urun_adi} ürünü silindi.")
    else:
        messagebox.showinfo("Hata", f"{magaza_adi} mağazası veya {urun_adi} ürünü bulunamadı.")

def min_fiyati_bul():
    urun_adi = simpledialog.askstring("Min Fiyatı Bul", "Karşılaştırmak istediğiniz ürünü girin:")

    fiyatlar = {m["ad"]: m["urunler"][urun_adi] for m in magazalar if urun_adi in m["urunler"]}

    if fiyatlar:
        en_ucuz_magaza = min(fiyatlar, key=fiyatlar.get)
        en_ucuz_fiyat = fiyatlar[en_ucuz_magaza]
        messagebox.showinfo("Sonuç", f"{urun_adi} en uygun fiyatla {en_ucuz_magaza}'dan alınabilir. Fiyat: {en_ucuz_fiyat} TL.")
    else:
        messagebox.showinfo("Hata", f"{urun_adi} ürünü hiçbir mağazada bulunamadı.")

# Tkinter uygulamasını başlatıyor
        #Ana frame i oluşturuyor ve başlığı ekliyoruz.
root = tk.Tk()
root.title("Mağaza Programı")

# Butonları içeren bir frame oluşturuyoruz
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Butonları oluşturup  frame'e ekliyoruz
tk.Button(button_frame, text="Ürün Ekle", command=urun_ekle).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Fiyat Güncelle", command=fiyat_guncelle).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Ürün Sil", command=urun_sil).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Min Fiyatı Bul", command=min_fiyati_bul).pack(side=tk.LEFT, padx=5)

# Tkinter uygulamasını çalıştırır ve frame'i görüntüleriz.
root.mainloop()
