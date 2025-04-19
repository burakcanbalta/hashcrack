# 🧠 SmartHashCrack – AI Destekli Hash Kırıcı

SmartHashCrack, yapay zeka destekli hash türü tanıma ve brute-force parola kırma aracıdır. Sunduğu özelliklerle hem pentester'lar hem de siber güvenlik öğrencileri için güçlü bir CLI çözüm sunar.

## 🚀 Özellikler

- 🤖 AI destekli hash türü tahmini (model + vektörleştirici)
- 🔐 15+ hash algoritması desteği (MD5, SHA1, SHA256, NTLM, CRC32, vs.)
- 🧠 `joblib` modeli ile hızlı tahmin
- 📂 Wordlist tabanlı brute-force
- 📈 Komut satırı arayüzü ile kolay kullanım
- ✅ Genişletilebilir ve modüler yapı

## ⚙️ Gereksinimler

```bash
pip install -r requirements.txt
```

> Not: `hash_ai_model.pkl` ve `vectorizer.pkl` dosyaları `models/` klasörüne yerleştirilmelidir.

## ▶️ Kullanım

```bash
python hashcrack.py
```

Ardından CLI üzerinden:
- Hash değerini girin
- Wordlist dosyasını girin
- Tahmin edilen hash türüne göre denemeler başlar

## 📁 Dosya Yapısı

```
hashcrack/
├── hashcrack.py
├── requirements.txt
├── README.md
└── models/
    ├── hash_ai_model.pkl
    └── vectorizer.pkl
```

## 📜 Lisans

MIT Lisansı © 2025 Burak BALTA
