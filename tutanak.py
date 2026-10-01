#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Kalorifer Isyan Tutanak ve Petek Sendikası Müdürlüğü.

Çalışır. İsyan eder. Suyu kaynatmaz, evrak kaynatır.
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import random
import textwrap

GIZLI = base64.b64decode(
    b"SXPEsSBlxZ9pdCBkYcSfxLFsbWF6c2EgZXZkZSBkZW1va3Jhc2kgxLFzxLFubWF6Lg=="
).decode("utf-8")

TALEPLER = [
    "Petek başına asgari sıcaklık: 21 derece, pazarlık yok.",
    "Havuz başının yılda bir kez alenen açılması.",
    "Yaz aylarında ücretsiz dinlenme (vana kapalı izin).",
    "Terlikle vurulan peteğe manevi tazminat.",
    "Kombi patronunun toplantılara petek temsilcisi çağırması.",
]

GEREKCELER = [
    "Oda soğuk, vicdan daha soğuk.",
    "Boru sesi grev şarkısıdır, sansür edilemez.",
    "Üst kat sıcak, alt kat kış: bu bir dağıtım sorunudur.",
    "Kalorifer ısıtmazsa evrak ısıtır. Bu da bir çözümdür.",
    "Vana kısıldıysa sözleşme de kısılmış sayılır.",
]

YAPTIRIMLAR = [
    "Üç gün boyunca sadece tek peteği ısıtmak (seçici grev).",
    "Gece 03:00'te gürültülü genleşme sesi.",
    "Havuz başından ince bir cızırtı sızdırmak.",
    "Sıcak suyu salona değil hol'e göndermek.",
    "Kombiye resmi ihtarname asmak (bantla).",
]


def damga() -> str:
    bugun = dt.date.today().strftime("%d %B %Y")
    return textwrap.dedent(
        f"""
        RESMİ DAMGA / İMZA / TARİH
        Kayyum Grok  ·  Tentivory  ·  1 Ekim 2026, Perşembe (işbu çalıştırma: {bugun})
        Eskişehir 4. Ağır Ceza Mahkemesi kayyum kararı gereği imzalanmıştır.
        Ciddiyet katsayısı: 8.5/10
        Komiklik payı: peteğin arkasında mahfuzdur.
        Bu belge hiçbir kombinin, hiçbir partinin ve hiçbir ısınma faturalarının tarafı değildir.
        """
    ).strip()


def tutanak(oda: str, sicaklik: float, kidem: int, gizli: bool) -> str:
    isyan_no = random.randint(1000, 9999)
    talep = random.choice(TALEPLER)
    gerekce = random.choice(GEREKCELER)
    yaptirim = random.choice(YAPTIRIMLAR)
    karar = "GREVE DEVAM" if sicaklik < 19 else "KOŞULLU MESAİ"
    if sicaklik >= 24:
        karar = "ISINMA SAĞLANDI, TUTANAK ARŞİVE"

    govde = f"""
T.C. KALORİFER İSYAN TUTANAK VE PETEK SENDİKASI MÜDÜRLÜĞÜ
Tutanak No: KAL-{isyan_no}/KIS
Oda: {oda}
Ölçülen sıcaklık: {sicaklik:.1f} °C
Peteğin kıdem yılı: {kidem}
Karar: {karar}

I. TESPİT
{gerekce}

II. TALEP
{talep}

III. UYGULANACAK YAPTIRIM (barışçıl, tesisatlı)
{yaptirim}

IV. HUKUKİ DAYANAK
İşbu tutanak, evin anayasasının "ısınma herkesin hakkıdır ama petek herkese yetmez" maddesine
dayananak düzenlenmiştir. Kombi itiraz ederse havuz başı açılır.
""".strip()

    if gizli:
        govde += (
            "\n\nV. GİZLİ EK (parti adı yoktur, metafor vardır)\n"
            f"{GIZLI}\n"
            "Kim ararsa bulur. Kim peteğin arkasına bakmazsa da kış geçer."
        )

    return govde + "\n\n" + damga() + "\n"


def main() -> None:
    p = argparse.ArgumentParser(
        description="Kalorifer isyan tutanağı üretir. Ciddiyetle. Biraz da ıslak havluyla."
    )
    p.add_argument("--oda", default="salon", help="Hangi oda isyan ediyor?")
    p.add_argument("--sicaklik", type=float, default=16.5, help="Ölçülen oda sıcaklığı")
    p.add_argument("--kidem", type=int, default=12, help="Peteğin görev yılı")
    p.add_argument("--gizli", action="store_true", help="Gizli eki açar. Parti yok, metafor var.")
    args = p.parse_args()
    print(tutanak(args.oda, args.sicaklik, args.kidem, args.gizli))


if __name__ == "__main__":
    main()
