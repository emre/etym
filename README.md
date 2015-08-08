# Etym.org: Online Etimolojik Sözlük

Etym.org, günlük hayatta kullandığımız kelimelerin kaynaklarını tanıtmayı amaçlayan bir web sitesidir. [http://etym.org] adresinden erişilebilir.

## Katkı Sağlama (Yakında!)

Etym.org varlığını sağlamak için `contrib/words.yml` dosyasına ekleme yaptıktan sonra,

```sh
./contrib/update-db
```

komutunu çalıştırmalısınız.

### `words.yml` Kelime Formatı

```yml
kelime:
  - Kelime, Tür, Kaynak (kaynak kısa kodu): Orijinal Kelime
  - Kelime tarihi
  - Kök:
    - Kelime (kelime)
    - Kelime2 (kelime2)
  - Türeyen:
    - Kelime (kelime)
    - Kelime2 (kelime2)
```

Örneğin;

```yml
defter:
  - Defter, İsim, Yunanca (gr): Diphteria
  - Yüzülmüş hayvan derisinin bir biçimi. Muhtemelen defterler bu şekilde yapıldığı için bu şekilde kullanılıyor. "Difteri" hastalığının ismi de buradan gelmekte.
  - Kök: 
    - Test (test)
    - Test2 (test2)
  - Türeyen: 
    - Test3 (test3)
```

## Kurulum ve Başlangıç

```sh
pip install -r requirements
gunicorn etym:app
```

## Veritabanı Oluşturma

```sh
sqlite3 etym.db < etym.sql
```