GIDIS_UCRETI=1.5
DONUS_UCRETI=1.4
GUNSAYISI=22

def AylikYolMasrafi(gidisUcreti,donusUcreti,gunSayisi):
    masraf=(gidisUcreti+donusUcreti)*gunSayisi
    return masraf


def YillikYolMasrafi(gidisUcreti,donusUcreti,gunSayisi):
    YillikMasraf=AylikYolMasrafi(gidisUcreti,donusUcreti,gunSayisi)*12
    return YillikMasraf



aylikMasraf=AylikYolMasrafi(GIDIS_UCRETI,DONUS_UCRETI,GUNSAYISI)
yillikMasraf=int(YillikYolMasrafi(GIDIS_UCRETI,DONUS_UCRETI,GUNSAYISI))
print("Aylık Yol masrafı: {}",aylikMasraf)
print("Yıllık Yol masrafı: {}",yillikMasraf)

