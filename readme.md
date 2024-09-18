# YuKita

**Tugas Pemrograman Berbasis Platform - PBP B**

> **YuKita** merupakan proyek Django sederhana berbentuk e-commerce berbasis website untuk memenuhi Tugas Individu mata kuliah PBP Gasal 2024/2025

[ 🏠 Kunjungi Website YuKita 🏠 ](http://gnade-yuka-yukita.pbp.cs.ui.ac.id/)

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

Template untuk merender pada file `views.py` berisikan

```
from django.shortcuts import render

def show_main(request):
    context = {
        'product_name': 'BLAHAJ Soft Toy',
        'product_price': 'IDR 299,000',
        'product_description': 'A large and soft cuddly shark. It\'s perfect to hug, use as a pillow, or play with. This toy will bring comfort and joy to any child.',
        'product_quantity': 1,
        'product_location': 'Jakarta, Surabaya, Bali',
        'name' : "Gnade Yuka",
        'kelas' : "PBP-B"
    }

    return render(request, "main.html", context)

```

dan template pada file `html.main` berisi 

```
<h1>YuKita</h1>

<h5>Nama: </h5>
<p>{{ name }}</p>

<h5>Kelas: </h5>
<p>{{ kelas }}</p>

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

<details>
<summary> <b> Tugas 3: Implementasi Form dan Data Delivery pada Django</b> </summary>

## **Jawaban Tugas 3**

* ### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
**Data delivery** dalam pengimplementasian sebuah platform diperlukan karena bertujuan untuk memastikan bahwa data yang dikirim antar bagian sistem (misalnya, antara frontend dan backend atau antar microservices) dapat ditukar dengan cara yang efisien, aman, dan konsisten. Tanpa mekanisme pengiriman data yang efektif, aplikasi tidak akan dapat menyajikan informasi yang tepat kepada pengguna secara real-time, menyebabkan pengalaman pengguna yang buruk. Selain itu, data delivery memungkinkan platform untuk beroperasi secara terdistribusi, mendukung skala besar, serta memfasilitasi komunikasi antar komponen yang berbeda secara seamless.

* ### Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Antara **XML** dan **JSON**, **JSON** lebih baik dan populer untuk pengiriman data dalam aplikasi modern. Hal ini karena JSON lebih ringan dan lebih mudah dibaca oleh manusia maupun mesin dibandingkan XML, yang menggunakan tag berlapis dan lebih verbose. JSON juga lebih mudah diolah dengan JavaScript, yang merupakan bahasa umum di web development. Sementara XML memiliki kemampuan untuk mendeskripsikan struktur data yang lebih kompleks (seperti metadata dan skema yang dapat divalidasi), JSON tetap lebih disukai untuk API modern karena kecepatan dan kesederhanaannya. Oleh karena itu, JSON lebih populer karena performanya yang lebih efisien dalam konteks pengiriman data di web.

* ### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Dalam **Django**, method **`is_valid()`** digunakan pada objek form untuk memeriksa apakah data yang dikirimkan oleh pengguna sesuai dengan aturan validasi yang telah ditentukan dalam form tersebut. Method ini akan mengembalikan nilai `True` jika semua data valid dan `False` jika terdapat kesalahan dalam input pengguna. Kita membutuhkan method ini agar data yang diterima dari pengguna dapat diproses dengan benar atau menampilkan pesan kesalahan jika data yang dimasukkan tidak sesuai dengan ketentuan (misalnya format email salah atau ada field yang tidak diisi). Tanpa validasi ini, aplikasi rentan menerima data yang tidak lengkap atau tidak valid.

* ### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan **`csrf_token`** saat membuat form di Django untuk melindungi aplikasi dari serangan **Cross-Site Request Forgery (CSRF)**, yaitu jenis serangan di mana penyerang dapat membuat pengguna yang sudah login di aplikasi mengirimkan permintaan yang tidak diinginkan tanpa sepengetahuan mereka. Jika form Django tidak memiliki **`csrf_token`**, penyerang dapat memanfaatkan celah ini untuk melakukan tindakan berbahaya, seperti mengirimkan permintaan palsu atas nama pengguna tanpa izin, yang bisa berdampak pada perubahan data atau eksploitasi lain. **`csrf_token`** membantu mencegah hal ini dengan memastikan bahwa permintaan yang dikirim ke server berasal dari sumber yang sah.

## **Implementasi Checklist**

* ### Membuat input form

Membuat `form` untuk menerima input, sehingga nantinya data baru bisa ditampilkan dengan membuat file `forms.py` pada main yang berisikan kode

```
from django.forms import ModelForm
from main.models import ShopEntry

class ShopEntryForm(ModelForm):
    class Meta:
        model = ShopEntry 
        fields = ["product_name", "price", "quantity", "location", "description"]
```

Selain itu, saya juga mengubah `show_main` pada `views.py` menjadi

```
def show_main(request):
    shop_entries = ShopEntry.objects.all()
    
    context = {
        # 'product_name': 'Sofa Ruang Tamu',
        # 'product_price': 'IDR 1,500,000',
        # 'product_description': 'A sofa-bed with small, neat dimensions which is easy to furnish with, even when space is limited. You can make the sofa more comfortable and personal by completing with pillows in different colours and patterns.',
        # 'stock': 1,
        # 'product_location': 'Jakarta, Surabaya, Bali',
        'name' : "Gnade Yuka",
        'kelas' : "PBP-B",
        'shop_entries' : shop_entries
    }

    return render(request, "main.html", context)
```

* ### Menambahkan fungsi pada `views.py`

Sehingga kita bisa melihat data yang sudah diinput

1. Membuat fungsi baru `create_shop_entry` pada `views.py` agar bisa menerima data yang berisikan

```
def create_shop_entry(request):
    form = ShopEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_shop_entry.html", context)
```

2. Lalu membuat template baru untuk tampilan ketika menambahkan pembelian baru dengan nama `create_shop_entry` pada direktori `main/templates` yang berisikan

```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Mood Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Shop Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

3. Lalu menampilkan data pembelian dalam bentuk tabel dan menambahkan tombol `Add New Shop Entry` pada `main.html` ketika ingin menambahkan pembelian

```
<div class="shop-entries">
    <h3>Shop Entries</h3>
    
    {% if not shop_entries %}
    <p>Belum ada pesanan yang masuk</p>
    {% else %}
    <table>
      <tr>
        <th>Nama</th>
        <th>Harga</th>
        <th>Jumlah Kamar</th>
        <th>Lokasi</th>
        <th>Deskripsi</th>
      </tr>
      
      <!-- Display each shop entry -->
      {% for shop_entry in shop_entries %}
      <tr>
        <td>{{ shop_entry.product_name }}</td>
        <td>{{ shop_entry.price }}</td>
        <td>{{ shop_entry.quantity }}</td>
        <td>{{ shop_entry.location }}</td>
        <td>{{ shop_entry.description }}</td>
      </tr>
      {% endfor %}
    </table>
    {% endif %}
</div>

<br />

<a href="{% url 'main:create_shop_entry' %}">
  <button>Add New Shop Entry</button>
</a>
```

* ### Menambahkan format XML dan JSON 

Untuk melihat data dalam format XML dan JSON, pada `views.py` di foler `main` kita menambahkan 
```
from django.http import HttpResponse
from django.core import serializers
```

1. Menambahkan fungsi `show_xml` dan `show_xml_by_id` (untuk melihat bedasarkan filter ID) yang akan mengembalikan `HttpResponse` berisi data yang sudah menjadi XML

```
def show_xml(request):
    data = ShopEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = ShopEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

2. Menambahkan fungsi `show_json` dan `show_json_by_id` (untuk melihat bedasarkan filter ID) yang akan mengembalikan `HttpResponse` berisi data yang sudah menjadi JSON

```
def show_json(request):
    data = ShopEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = ShopEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

```

3. Merouting URL
Tidak lupa juga untuk menambahkan `path_url` fungsi yang sudah kita tambhkan ke `urlpatterns` pada `main/urls.py` dan mengimport dari `views.py`. Sehingga isi dari `main/urls.py` akan berisi :

```
from django.urls import path
from main.views import show_main, create_shop_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-shop-entry', create_shop_entry, name='create_shop_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

Sehingga, input `form` sudah bisa digunakan dengan menjalankan command `python3 manage.py runserver` dan mengunjungi <http://localhost:8000>.

## Postman *Screenshot*
1. XML
![XML](image/postman_xml.png)
2. JSON
![JSON](image/postman_json.png)
3. XML *by* ID
![XML *by* ID](image/postman_xml_id.png)
4. JSON *by* ID
![JSON *by* ID](image/postman_json_id.png)

</details>

