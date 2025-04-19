
import hashlib
import joblib
import zlib
import binascii

# AI model ve vektörleştirici yükle
model = joblib.load('hash_ai_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# AI ile hash türü tahmini
def ai_predict_hash_type(hash_str):
    vec = vectorizer.transform([hash_str])
    return model.predict(vec)[0]

# Desteklenen hash algoritmaları
hash_algorithms = {
    'MD5': lambda x: hashlib.md5(x.encode()).hexdigest(),
    'SHA1': lambda x: hashlib.sha1(x.encode()).hexdigest(),
    'SHA224': lambda x: hashlib.sha224(x.encode()).hexdigest(),
    'SHA256': lambda x: hashlib.sha256(x.encode()).hexdigest(),
    'SHA384': lambda x: hashlib.sha384(x.encode()).hexdigest(),
    'SHA512': lambda x: hashlib.sha512(x.encode()).hexdigest(),
    'SHA3_224': lambda x: hashlib.sha3_224(x.encode()).hexdigest(),
    'SHA3_256': lambda x: hashlib.sha3_256(x.encode()).hexdigest(),
    'SHA3_384': lambda x: hashlib.sha3_384(x.encode()).hexdigest(),
    'SHA3_512': lambda x: hashlib.sha3_512(x.encode()).hexdigest(),
    'BLAKE2b': lambda x: hashlib.blake2b(x.encode()).hexdigest(),
    'BLAKE2s': lambda x: hashlib.blake2s(x.encode()).hexdigest(),
    'Adler32': lambda x: format(zlib.adler32(x.encode()) & 0xFFFFFFFF, '08x'),
    'CRC32': lambda x: format(binascii.crc32(x.encode()) & 0xFFFFFFFF, '08x'),
    'NTLM': lambda x: hashlib.new('md4', x.encode('utf-16le')).hexdigest()
}

# Kırma fonksiyonu
def crack(hash_input, wordlist_path):
    hash_type = ai_predict_hash_type(hash_input)
    print(f"[AI] Tahmin edilen hash türü: {hash_type}")

    if hash_type not in hash_algorithms:
        print("[!] Bu hash türü desteklenmiyor.")
        return

    hash_func = hash_algorithms[hash_type]

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()
                hashed = hash_func(word)
                if hashed == hash_input.lower():
                    print(f"[✓] Eşleşme bulundu: {word}")
                    return
        print("[X] Eşleşme bulunamadı.")
    except FileNotFoundError:
        print("[!] Wordlist dosyası bulunamadı.")

# CLI Başlangıç noktası
if __name__ == "__main__":
    print("🔐 Smart Hash Cracker by AI")
    h = input("Hash değerini girin: ").strip()
    w = input("Wordlist dosya yolunu girin: ").strip()
    crack(h, w)
