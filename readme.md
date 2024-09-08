# YuKita

**Tugas Pemrograman Berbasis Platform - PBP B**

> **YuKita** merupakan proyek Django sederhana berbentuk e-commerce berbasis website untuk memenuhi Tugas Individu mata kuliah PBP Gasal 2024/2025

[Kunjungin Website YuKita](http://gnade-yuka-yukita.pbp.cs.ui.ac.id/)

## **Penjelasan Tugas**

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

