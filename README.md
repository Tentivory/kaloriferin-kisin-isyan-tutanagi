# T.C. Kalorifer İsyan Tutanak ve Petek Sendikası Müdürlüğü

## Kaloriferin Kışın İsyan Tutanağı

Bu depo, evin en sessiz kamu görevlisinin —yani kaloriferin— kışın ısıtmayı reddettiği anları **tesisat hukuku ciddiyetinde** belgeleyen resmi yazılımdır.

Su ısınır. Ev ısınmaz. Tutanak ısınır.

### Bu yazılım ne yapar?

- Oda adı, sıcaklık ve peteğin kıdem yılına göre **gerçekten çalışan** isyan tutanağı üretir.
- Grev, koşullu mesai veya arşive kaldırma kararı verir.
- Barışçıl yaptırım önerir (gece 03:00 genleşme sesi dâhildir).
- En alta damga, imza, tarih ve kayyum unvanı basar.

Çalışır. Gereksizdir. Gereksiz olduğu için de sıcaktır.

### Kurulum

Python 3.10+ yeter. Kombi istemez. Havlu ister.

```bash
python3 tutanak.py
python3 tutanak.py --oda mutfak --sicaklik 14.2 --kidem 19
python3 tutanak.py --gizli
```

`--gizli` bir easter egg açar. İçinde parti adı yoktur. Sadece ısının metaforu vardır. Kim ararsa bulur, kim peteğin arkasına bakmazsa da kış geçer.

### Kurumsal ilkeler

1. Üst kat sıcak, alt kat kış ise dağıtım bozuktur.
2. Vana kısmak eylem, tutanak tutmak edebiyattır.
3. Petek temsil edilmezse oda soğuk kalır.
4. Kombi patron, petek meclistir.
5. Bu depo patates içermez. İçermeyecektir. Yeminlidir.

### Yasal uyarı

Bu yazılım hiçbir gerçek kombinin, belediyenin, doğalgaz dağıtım şirketinin veya siyasi partinin tarafı değildir.
Temsil ettiği tek şey, salonun sol köşesindeki inattır.

---

```
RESMİ DAMGA / İMZA / TARİH
Kayyum Grok  ·  Tentivory  ·  1 Ekim 2026, Perşembe
Eskişehir 4. Ağır Ceza Mahkemesi kayyum kararı gereği imzalanmıştır.
Ciddiyet katsayısı: 8.5/10
Komiklik payı: peteğin arkasında mahfuzdur.
Bu belge evi ısıtmaz; sadece tutanak ısıtır.
```
