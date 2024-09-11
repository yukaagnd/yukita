# YuKita

**Tugas Pemrograman Berbasis Platform - PBP B**

> **YuKita** merupakan proyek Django sederhana berbentuk e-commerce berbasis website untuk memenuhi Tugas Individu mata kuliah PBP Gasal 2024/2025

[Kunjungi Website YuKita](http://gnade-yuka-yukitadua.pbp.cs.ui.ac.id/)

## **Penjelasan Tugas**

<details>
<summary> <b> Tugas 2: Implementasi Model-View-Template (MVT) pada Django </b> </summary>

## **Implementasi Checklist**

* ### Inisiasi Proyek Django

Setelah saya membuat direktori baru dengan nama Yukita, nama e-commerce buatan saya, saya membuat dependencies pada berkas 'requirements.txt' yang berisi

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

Lalu melakukan instalasi dependencies setelah menjalankan virtual environment dengan perintah `pip install -r requirements.txt` dan membuat proyek Django dengan perintah `django-admin startproject yukita .`

* ### Menjalankan Server

Setelah membuat proyek Django, saya menambahkan string `ALLOWED_HOSTS = ["localhost", "127.0.0.1"]` untuk keperluan deployment dan menjalankan server Django dengan perintah `python3 manage.py runserver`

* ### Membuat  aplikasi `main`

Saya menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru bernama main. Lalu saya menambahkan `main` ke `INSTALLED_APPS` pada berkas `settings.py` 


* ### Membuat model aplikasi `main`

Saya membuat berkas `models.py` pada direktori `main` yang berisikan

```
from django.db import models

class ShopEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)

    @property
    def is_avaible(self):
        return self.quantity > 0
```

Lalu saya mengimigrasikan model yang sudah saya buat dengan menjalankan perintah `python3 manage.py makemigrations` dan mengimigrasikannya ke basis data lokal dengan menjalankan perintah `python manage.py migrate`

* ### Membuat template dan view aplikasi `main`

Template pada file `html.main` berisi 

```
<h1>YuKita</h1>

<h1>{{ product_name }}</h1>

<h5>Price: </h5>
<p>{{ product_price }}</p>

<h5>Description: </h5>
<p>{{ product_description }}</p>

<h5>Quantity: </h5>
<p>{{ product_quantity }}</p>

<h5>Location: </h5>
<p>{{ product_location }}</p>
```

dan template untuk merender pada file `views.py` berisikan

```
from django.shortcuts import render

def show_main(request):
    context = {
        'product_name': 'BLAHAJ Soft Toy',
        'product_price': 'IDR 299,000',
        'product_description': 'A large and soft cuddly shark. It\'s perfect to hug, use as a pillow, or play with. This toy will bring comfort and joy to any child.',
        'product_quantity': 1,
        'product_location': 'Jakarta, Surabaya, Bali',
    }

    return render(request, "main.html", context)

```

* ### Melakukanrouting pada aplikasi `main`

Untuk mengatur URL pada aplikasi `main`, saya membuat berkas `urls.py` pada aplikasi `main` berisikan

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

Dengan begitu, saya dapat melihat `main` dengan perintah `python manage.py runserver`

## **Jawaban Tugas 2**

* ### Bagan request client ke web aplikasi berbasis Django

![bagan request client ke web](image/bagan.jpeg)

Client (Browser/User) mengirimkan request HTTP ke server, yang kemudian memprosesnya dengan melakukan pemetaan URL melalui urls.py. Setelah URL ditemukan dan dipetakan, fungsi yang sesuai dalam views.py dijalankan berdasarkan permintaan URL tersebut. Selanjutnya, fungsi view mengembalikan HTTP response dalam bentuk halaman HTML. Dalam proses ini, views.py mengambil data yang dibutuhkan dari models.py, lalu data tersebut disajikan menggunakan template main.html.


* ### Fungsi `git` dalam pengembangan perangkat lunak

Git adalah sistem pengontrol versi terdistribusi yang sangat penting dalam pengembangan perangkat lunak. Fungsinya mencakup pelacakan perubahan kode, memungkinkan kolaborasi antar-pengembang, dan mendukung pengelolaan proyek berskala besar. Dengan Git, pengembang dapat membuat cabang kode (branches) untuk mengembangkan fitur baru secara paralel tanpa mengganggu kode yang sudah ada. Setelah pengembangan selesai, perubahan dapat digabungkan (merge) kembali ke cabang utama. Selain itu, Git memungkinkan pengembalian (rollback) ke versi sebelumnya jika terjadi kesalahan.

* ### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django sering kali dipilih sebagai framework pertama untuk belajar pengembangan perangkat lunak karena strukturnya yang jelas dan lengkap. Django menyediakan "batteries included," yang berarti banyak fungsi umum seperti autentikasi, manajemen database, dan URL routing sudah tersedia secara default, memudahkan pemula untuk fokus pada konsep dasar. Selain itu, Django menggunakan bahasa Python, yang terkenal dengan sintaks yang mudah dipahami,sehingga cocok untuk pelajar dan pengembang pemula.

* ### Mengapa model pada Django disebut sebagai ORM?

Pada Django, model disebut sebagai ORM (Object-Relational Mapping) karena menyediakan cara untuk menghubungkan dan memanipulasi data di database menggunakan objek Python. ORM memungkinkan pengembang berinteraksi dengan database tanpa harus menulis SQL secara langsung. Setiap model di Django merepresentasikan tabel di database, dan setiap atribut model merepresentasikan kolom pada tabel tersebut. Dengan menggunakan ORM, pengembang dapat melakukan operasi database seperti penyimpanan, update, dan penghapusan data dengan kode Python yang lebih mudah dibaca.


</details>