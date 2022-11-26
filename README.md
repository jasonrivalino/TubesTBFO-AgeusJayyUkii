# Tugas Besar Teori Bahasa Formal dan Otomata

Membuat Parser Bahasa JavaScript dengan Bahasa Pemrograman Python

## Table of Contents

* [General Information](#general-information)
* [Struktur Data](#struktur-data)
* [Cara Penggunaan](#cara-penggunaan)
* [Authors](#authors)

## General Information
Dalam proses pembuatan program yang dapat dieksekusi menjadi mesin, kita memerlukan pemeriksaan sintaks (parser) agar program dapat dijalankan dengan baik dan tidak mengalami error saat proses kompilasi (compiling) oleh komputer. Pada tugas besar ini, kami membuat parser untuk JavaScript (NODE.js) dengan menggunakan CFG sebagai grammar dan CYK sebagai alghoritma untuk melakukan parsing.

## Struktur Data

```bash
├───bin
│
├───doc
│       LaporanTubesTBFO-AgeusJayyUkii.pdf
│
├───src
│       bacagrammar.py
│       convertofGrammar.py
│       grammar.txt
│       mainprogram.py
│       parserOfGrammar.py
│       processFile.py
│
├───test
│       inputAcc.js
│       inputReject.js
│
└───README.md

```

## Cara Penggunaan

1. Clone repository ini menggunakan menggunakan command `git clone https://github.com/jasonrivalino/TubesTBFO-AgeusJayyUkii.gt`.
2. Ketik source code yang hendak di parsing pada suatu file dengan directory yang sama dengan program `mainprogram.py`, kemudian save file tersebut.
3. Jalankan program parsing menggunakan command `py mainprogram.py <source_code>`.

## Authors

* [Jason Rivalino - 13521008](https://github.com/jasonrivalino)
* [Muhhamad Syauqi Jannatan - 13521014](https://github.com/syauqijan)
* [Agsha Athalla Nurkareem - 13521027](https://github.com/agshaathalla)
