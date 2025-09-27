import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="Okul Günü Sayacı", layout="centered")
st.title("🖤 Okul Günü Sayacı")

# Kullanıcı okul bitiş tarihini seçsin
okul_bitis = st.date_input("Okul bitiş tarihi seç:", value=date(2026, 6, 26))

# Kullanıcı özel tatilleri ekleyebilir
st.write("🎉 Ekstra tatiller ekleyin (opsiyonel):")
tatil_input = st.text_area(
    "Tatilleri YYYY-MM-DD formatında, her satıra bir tane olacak şekilde yazın:",
    value="2026-04-23\n2026-05-01\n2026-05-19\n2026-07-15\n2026-08-30\n2026-10-29"
)

# Tatilleri listeye çevir
tatiller = []
for line in tatil_input.split("\n"):
    line = line.strip()
    if line:
        try:
            yıl, ay, gün = map(int, line.split("-"))
            tatiller.append(date(yıl, ay, gün))
        except:
            st.error(f"Tarih hatalı: {line}")

# Kalan günleri hesapla
if st.button("Kalan Günleri Hesapla"):
    bugun = date.today()
    if okul_bitis < bugun:
        st.warning("Okul bitiş tarihi geçmiş!")
    else:
        gun_sayisi = 0
        gecici_tarih = bugun

        while gecici_tarih <= okul_bitis:
            if gecici_tarih.weekday() < 5 and gecici_tarih not in tatiller:
                gun_sayisi += 1
            gecici_tarih += timedelta(days=1)

        st.success(f"Okulun bitmesine {gun_sayisi} gün kaldı (hafta sonları ve tatiller hariç).")
