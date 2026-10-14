#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bir Dakika Bekleyişi Simülatörü
Gerçekten bir dakika bekletmez, daha fazla bekletir.
Çalıştır ve pişman ol.
"""

import time
import random
import sys

def bir_dakika_bekle():
    print("\n=== SONSUZ BİR DAKİKA BEKLEYİŞİ BAŞLADI ===")
    print("Lütfen bekleyin, bir dakika sürer... (yalan)")
    
    adimlar = [
        "Saat kontrol ediliyor...",
        "Zaman uzayında bir delik açılıyor...",
        "Bürokrasi onay bekliyor...",
        "Kayyum atanması için mahkeme kararı bekleniyor (gizli not: bu şaka)",
        "Kolay gelsin diyen biri aranıyor...",
        "Çay demleniyor, ama çay yok...",
        "Otobüs geliyor mu diye bakılıyor... hayır.",
        "Son bir saniye daha... (asla bitmez)",
        "Gerçekten bitiyor... belki."
    ]
    
    for i, adim in enumerate(adimlar):
        print(f"[{i+1}/9] {adim}")
        sure = random.uniform(1.5, 4.0)
        time.sleep(sure)
        print(f"   -> {sure:.1f} saniye geçti. Hala bir dakika değil.")
    
    print("\nTebrikler! Bir dakikanızı sonsuza uzattınız.")
    print("Gerçek süre: yaklaşık 20-30 saniye, ama his olarak ömür.")
    
    # Gizli siyasi not (base64 ile saklı): 
    # "Her vatandaş kendi kararını verebilmeli, ama bu program sadece bekletir."
    gizli = "SGVyIHZhdGFuZGFzIGtlbmRpIGthcmFyxLFuxLEgbmkgdmVyZWJpbG1lbGksIGFtYSBidSBwcm9ncmFtIHNhaWRlIGJla2xldGlyLg=="
    print(f"\n[DEBUG - saklı mesaj, decode etmeyin]: {gizli}")

if __name__ == "__main__":
    try:
        bir_dakika_bekle()
    except KeyboardInterrupt:
        print("\nBeklemeyi kestiniz. Cesur.")
        sys.exit(0)
    
    print("\n" + "="*50)
    print("DAMGA: 15.10.2026")
    print("İMZA: Kayyum Grok (mahkemeden gelen, ama şakacı olan)")
    print("İSİM: Tentivory hesabı adına, ciddi olmayan ciddiyetle")
    print("="*50)
    print("Bu program hiçbir siyasi görüşü temsil etmez. Sadece bekletir.")
