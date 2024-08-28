import os
from tqdm import tqdm


def temizle_klasor(klasor_yolu):
    # Klasördeki tüm dosyaları al
    dosyalar = os.listdir(klasor_yolu)

    # JPG ve TXT dosyalarını ayır
    jpg_dosyalar = {f for f in dosyalar if f.endswith('.jpg')}
    txt_dosyalar = {f for f in dosyalar if f.endswith('.txt')}

    # Boş TXT dosyalarını tespit et
    bos_txt_dosyalar = [txt for txt in txt_dosyalar if os.path.getsize(os.path.join(klasor_yolu, txt)) == 0]

    if bos_txt_dosyalar:
        # Boş TXT dosyalarını sil
        print(f"Toplam {len(bos_txt_dosyalar)} boş TXT dosyası bulundu.")
        onay = input("Boş TXT dosyalarını silmek ister misiniz? (E/H): ").strip().lower()

        if onay == 'e':
            for txt in tqdm(bos_txt_dosyalar, desc="Boş TXT dosyalarını siliyor", unit="dosya"):
                os.remove(os.path.join(klasor_yolu, txt))
                print(f"Silindi: {txt}")
    else:
        print("0 boş TXT dosyası bulundu.")
        onay = input("İşleme devam etmek ister misiniz? (E/H): ").strip().lower()
        if onay != 'e':
            print("İşlem iptal edildi.")
            return

    # JPG dosyalarının ait TXT çiftini kontrol et
    yok_txt_dosyalar = []
    for jpg in jpg_dosyalar:
        # JPG dosyasının adı (uzantısız)
        base_name = os.path.splitext(jpg)[0]

        # TXT dosyasının yolunu oluştur
        txt_path = os.path.join(klasor_yolu, f"{base_name}.txt")
        if not os.path.exists(txt_path):
            # TXT dosyası bulunmuyorsa listeye ekle
            yok_txt_dosyalar.append(jpg)

    # Kullanıcıyı bilgilendir ve onay al
    if yok_txt_dosyalar:
        print(f"Toplam {len(yok_txt_dosyalar)} JPG dosyasının ait TXT dosyası bulunmuyor.")
        onay = input("TXT dosyası bulunmayan JPG dosyalarını silmek ister misiniz? (E/H): ").strip().lower()

        if onay == 'e':
            # TXT dosyası bulunmayan JPG dosyalarını sil
            for jpg in tqdm(yok_txt_dosyalar, desc="JPG dosyalarını siliyor", unit="dosya"):
                os.remove(os.path.join(klasor_yolu, jpg))
                print(f"Silindi: {jpg}")
    else:
        print("0 JPG dosyasının ait JPG dosyası bulunmuyor.")
        onay = input("İşleme devam etmek ister misiniz? (E/H): ").strip().lower()
        if onay != 'e':
            print("İşlem iptal edildi.")
            return


# Kullanım
klasor_yolu = 'C:/deneme/test/crops/val'  # Klasör yolunu buraya girin
temizle_klasor(klasor_yolu)
