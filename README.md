Nama    : Rifda Aulia Nurbahri

NPM     : 2206081660

Kelas   : PBP D

https://amoron.adaptable.app/

<details>
    
<summary> Tugas 3 </summary>

<h1>Perbedaan antara form POST dan form GET dalam Django</h1>

Dalam Django, form POST dan form GET memiliki perbedaan dalam cara mereka mengirimkan data:

- Form POST: Form ini mengirimkan data dengan cara membundel data formulir, mengenkodasinya untuk transmisi, mengirimkannya ke server, dan kemudian menerima kembali responsnya. Data yang dikirimkan tidak ditampilkan di URL.

- Form GET: Form ini mengirimkan data dengan cara membundel data yang dikirimkan menjadi sebuah string, dan menggunakan string ini untuk membuat URL. Data yang dikirimkan akan ditampilkan di URL.

Jadi, perbedaan utama antara keduanya adalah bagaimana data dikirimkan dan apakah data tersebut ditampilkan di URL atau tidak.

<h1>Perbedaan Utama antara XML, JSON, dan HTML dalam Konteks Pengiriman Data</h1>

XML, JSON, dan HTML adalah teknologi yang digunakan untuk mengelola dan mengirimkan data, tetapi mereka memiliki perbedaan utama dalam konteks pengiriman data:

- XML (eXtensible Markup Language): XML adalah bahasa markup yang digunakan untuk menyimpan dan berbagi data antar aplikasi. XML memiliki struktur pohon dalam membentuk datanya dengan menggunakan tag dan atribut. XML dapat digunakan dalam berbagai bahasa pemrograman seperti Java, Python, atau C#. Selain itu, XML juga digunakan dalam web service, message passing, dan pembuatan dokumen.

- JSON (JavaScript Object Notation): JSON adalah format pertukaran data terbuka yang dapat dibaca baik oleh manusia maupun mesin. JSON bersifat independen dari setiap bahasa pemrograman dan merupakan output API umum dalam berbagai aplikasi. JSON menggunakan struktur data yang mirip dengan objek-objek JavaScript. Data disimpan dalam bentuk key-value pairs, yang bisa menjadi array atau nested objects.

- HTML (HyperText Markup Language): HTML adalah bahasa markup yang digunakan untuk membuat halaman web dan aplikasi web. HTML mengurus tampilan dari dokumen dan bagaimana dokumen ini diakses di browser. HTML dapat mengubah teks menjadi gambar, tabel, tautan, dll.

Jadi, perbedaan utama antara ketiganya adalah bagaimana data disajikan dan dikirimkan:

- XML berfokus pada struktur dan konteks data.
- JSON berfokus pada transfer data dengan struktur yang lebih sederhana dan ringan.
- HTML berfokus pada penyajian data.

<h1>Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern</h1>

JSON (JavaScript Object Notation) sering digunakan dalam pertukaran data antara aplikasi web modern karena beberapa alasan berikut:

- Ringan: JSON adalah format yang ringan, yang memungkinkan data dikirim dengan cepat melalui jaringan.
- Struktur Data Sederhana: Berbeda dengan XML dan format lainnya yang memiliki fungsi serupa, JSON memiliki struktur data yang sederhana dan mudah dipahami.
- Mudah Dibaca oleh Manusia dan Mesin: JSON dirancang agar mudah dibaca oleh manusia, membuatnya menjadi format yang baik untuk debugging dan inspeksi data1. Selain itu, JSON juga mudah dipahami oleh mesin.
- Dukungan Lintas Platform: JSON didukung oleh sebagian besar bahasa pemrograman modern, sehingga data dalam format JSON dapat dengan mudah diolah dan dimanipulasi di berbagai platform.
- Fleksibilitas dalam Representasi Data: JSON memungkinkan representasi yang fleksibel dari berbagai jenis data. Ini dapat mencakup tipe data dasar seperti string, angka, boolean, serta struktur yang lebih kompleks seperti objek dan array.
- Penggunaan Luas dalam API: JSON sering digunakan pada API karena struktur kode yang lebih ringkas dan mudah dipahami daripada XML.

<h1> Implementasi Checklist </h1>

<h2>Membuat Input Form untuk Menambahkan Objek Model pada App Sebelumnya</h2>

Pertama-tama saya membuat berkas baru pada direktori `main` dengan nama `forms.py`. Berikut adalah isi `forms.py` saya.

```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "status", "amount", "price"]
```

Pada `fields` terdapat `name`, `description`, `status`, `amount`, dan `price` yang sesuai dengan variable yang ada pada `models.py` milik saya

Kemudian saya memodifikasi file `views.py`. Saya mengimport modul dan membuat fungsi baru bernama `create_product`

```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

Saya juga mengubah fungsi `show_main` yang sudah ada pada berkas `views.py` menjadi seperti berikut 

```python
def show_main(request):
    products = Product.objects.all()
    
    context = {
        'app': 'Amoron Rental',
        'nama': 'Rifda Aulia Nurbahri',
        'kelas' : 'PBP D',
        'products' : products
    }

    return render(request, "main.html", context)
```

Pada `urls.py` di `main` saya menambahkan path url ke dalam `urlpattern`

```python
path('create-product', create_product, name='create_product'),
```

Kemudian saya membuat berkas baru HTML dengan nama `create_product.html` pada direktori `main/templates`

```html
{% extends 'base.html' %} 

{% block content %}
<h1 style="color:firebrick;">Add Rentable Appliances</h1>

<form method="POST">
    {% csrf_token %}
    <table style="background-color:lightgrey;">
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product" style="background-color:green; color:white;"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

<h2>Menambahkan 5 Fungsi Views untuk Melihat Objek yang Sudah Ditambahkan dalam Format HTML, XML, JSON, XML by ID, dan JSON by ID</h2>

Pertama-tama saya membuka `views.py` pada direktori `main` dan melakukan import modul

```python
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
```

Kemudian saya membuat fungsi baru dengan nama `create_product` untuk menampilkan data produk data HTML

```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

Saya juga mengubah fungsi `show_main` yang sudah ada pada berkas `views.py` menjadi seperti berikut 

```python
def show_main(request):
    products = Product.objects.all()
    
    context = {
        'app': 'Amoron Rental',
        'nama': 'Rifda Aulia Nurbahri',
        'kelas' : 'PBP D',
        'products' : products
    }

    return render(request, "main.html", context)
```

Kemudian saya menambahkan fungsi `show_xml` dan `show_json` untuk mengembalikan data dalam bentuk XML dan JSON

```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

```python
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Saya juga menambahkan fungsi untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON

```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

```python
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

<h2>Membuat Routing URL untuk Tiap Views</h2>

Pertama-tama saya membuka `urls.py` yang ada pada folder `main` dan mengimport fungsi fungsi yang sudah saya buat pada poin nomor 2

```python
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
```

Kemudian saya menambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor

```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
]
```

<h2>Mengakses URL Menggunakan Postman</h2>

Pertama-tama saya membuka Postman dan melakukan `Send` request baru dengan method `GET` dan url
http://localhost:8000 

[![message-Image-1694872656652.jpg](https://i.postimg.cc/bJwXJbb2/message-Image-1694872656652.jpg)](https://postimg.cc/Y4ZDDvdp)

Kemudian url selanjutnya adalah http://localhost:8000/xml dan http://localhost:8000/xml/1

[![message-Image-1694872674810.jpg](https://i.postimg.cc/YCtBVJ93/message-Image-1694872674810.jpg)](https://postimg.cc/rKZHRZ50)

[![message-Image-1694872723766.jpg](https://i.postimg.cc/gkYMPdVn/message-Image-1694872723766.jpg)](https://postimg.cc/9znPG6Nh)

Terakhir, saya membuat request dengan method `GET` dengan url http://localhost:8000/json dan http://localhost:8000/json/1

[![message-Image-1694872751331.jpg](https://i.postimg.cc/L6n1PbRx/message-Image-1694872751331.jpg)](https://postimg.cc/WhczLSdZ)

[![message-Image-1694872762671.jpg](https://i.postimg.cc/260xkLFy/message-Image-1694872762671.jpg)](https://postimg.cc/2bBWT6tN)

<h1>BONUS</h1>

Untuk mengimplementasi bonus ini, saya menambahkan kode berikut pada file `main.html`

```html
<h2>You saved {{ products.count }} item(s) in this app</h2>
```

[![message-Image-1695026243103.jpg](https://i.postimg.cc/PqSymt06/message-Image-1695026243103.jpg)](https://postimg.cc/WDJ0VPNr)

</details>

<details>

<summary> Tugas 2 </summary>

<h1>Pembuatan Proyek Django</h1>

Pertama-tama saya membuka terminal untuk menyalakan virtual environment, kemudian saya membuat direktori baru dengan nama amoron yang diinisiasi dengan git. Pada direktori tersebut saya menambahkan beberapa dependencies dan memasangnya. Setelah itu saya membuat proyek Django bernama amoron dengan perintah`django-admin startproject amoron .`

<h1>Membuat Aplikasi Main pada Proyek Django</h1>

Pada tahap ini akan terbentuk direktori baru dengan nama main yang merupakan struktur awal dari aplikasi amoron. Saya menjalankan perintah berikut untuk membuat aplikasi main `python manage.py startapp main`. Kemudian saya menambahkan `'main'` ke list `INSTALLED_APPS` pada `settings.py`

<h1>Melakukan Routing pada Proyek</h1>

Pertama-tama saya membuat berkas`urls.py`pada direktori `main` kemudian saya mengisi `urls.py` dengan kode berikut
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Setelah itu saya membuka berkas `urls.py` yang ada pada direktori `amoron`. Saya mengimpor fungsi `include` dari `django.urls` dan menambahkan rute url seperti di bawah ini agar adaptable bisa diakses
```python
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('main/', include('main.urls'))
]
```

<h1>Membuat Model pada Aplikasi Main</h1>

Saya membuka file `models.py` pada direktori aplikasi `main` lalu mengisi berkas `models.py` dengan kode berikut
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=255)
    price = models.IntegerField()
```
Aplikasi saya memiliki atribut `name`, `amount`, `description`, `status`, dan `price`. Setelah itu saya melakukan migrasi model.

<h1>Membuat Fungsi untuk Dikembalikan ke Template HTML</h1>

Saya mengimpor fungsi `render` dari modul `django.shortcuts` kemudian saya menambahkan fungsi berikut
```python
def show_main(request):
    context = {
        'app': 'Amoron Rental',
        'nama': 'Rifda Aulia Nurbahri',
        'kelas' : 'PBP D'
    }

    return render(request, "main.html", context)
```
Sebelum itu saya sudah melakukan editing pada `main.html` di direktori `templates` agar tampilan web sesuai dengan yang saya mau.

<h1>Melakukan Deployment pada Adaptable</h1>

Saya melakukan `add`, `commit`, `push` pada repositori utama `amoron` ke GitHub. Setelah itu saya menghubungkan Adaptable saya dengan repositori tersebut dan memilih `Python App Template` sebagai template deployment dan `PostgreSQL` sebagai tipe basis data yang akan digunakan. Selanjutnya adalah penyesuaian python version dan memasukkan perintah `python manage.py migrate && gunicorn amoron.wsgi` pada `Start Command`. Terakhir, saya mencentang bagian `HTTP Listener on Port` dan memulai proses deployment aplikasi.

<h1>Request Client ke Web Aplikasi Berbasis Django</h1>

Berikut adalah bagan yang berisi request client ke web web aplikasi berbasis Django beserta responnya dan kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

<h2>Bagan</h2>

[![http-request-2.png](https://i.postimg.cc/q7dqkM7b/http-request-2.png)](https://postimg.cc/dh4w6Frr)

<h2>Kaitan</h2>

1. `urls.py` adalah bagian dari Django yang digunakan untuk mengatur routing atau penentuan alamat URL mana yang akan dihubungkan dengan tampilan (views) apa. Pada berkas `urls.py`, terdapat definisi pola URL dan mengarahkannya ke tampilan (views) yang sesuai.
2. Berkas `views.py` berisi fungsi-fungsi (views) yang akan dijalankan ketika pengguna mengakses alamat URL tertentu. Views ini mengambil permintaan HTTP dari pengguna, memprosesnya, dan mengembalikan respons HTTP yang akan ditampilkan kepada pengguna.
3. Berkas `models.py` digunakan untuk mendefinisikan struktur dan hubungan data dalam aplikasi. Ini adalah tempat di mana developer mendefinisikan model-model Django, yang mewakili tabel-tabel dalam database.
4. Berkas `HTML` adalah bagian dari tampilan dalam Django. Berkas ini digunakan untuk mengatur tampilan halaman web yang akan ditampilkan kepada pengguna. Dalam berkas HTML, developer dapat memanfaatkan sintaks template Django untuk menampilkan data dari views dan model, sehingga menghasilkan halaman web yang dinamis

Dengan cara ini, alur kerja dasar dalam pengembangan aplikasi Django adalah sebagai berikut:
1. Pengguna mengakses URL tertentu dalam aplikasi.
2. Berkas `urls.py` mengarahkan URL tersebut ke views yang sesuai.
3. Views dalam `views.py` memproses permintaan, berinteraksi dengan model jika diperlukan, dan merender template HTML.
4. Template HTML digunakan untuk menghasilkan halaman web yang dikirimkan kepada client sebagai respons HTTP.

<h1>Pentingnya Virtual Environment</h1>

Virtual environment (venv) adalah alat yang sangat berguna dalam dalam pengembangan aplikasi web berbasis Django. Berikut adalah beberapa alasan mengapa kita menggunakan virtual environment:
1. Isolasi Proyek : Virtual environment memungkinkan kita untuk membuat lingkungan kerja yang terisolasi untuk setiap proyek Python. Ini berarti bahwa setiap proyek memiliki salinan independen dari library Python yang diperlukan, dan tidak akan bersinggungan dengan library dari proyek lain. Hal ini membantu menghindari konflik dan masalah kompatibilitas antara proyek-proyek yang berbeda.
2. Manajemen Dependensi : Virtual environment memungkinkan Anda untuk menginstal dan mengelola dependensi proyek secara terisolasi. Kita dapat membuat daftar dependensi proyek Anda dalam berkas seperti requirements.txt.
3. Keamanan : Dengan menggunakan virtual environment, kita dapat menghindari pengubahan tidak sengaja atau penyusupan oleh berkas atau library di luar kendali proyek kita.

Secara teknis kita masih dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, hal ini tidak dianjurkan karena akan menyulitkan manajemen dependensi, meningkatkan risiko konflik antara proyek, dan dapat membuat instalasi dan pengelolaan proyek lebih rumit. Dengan virtual environment, kita dapat memaksimalkan isolasi, manajemen dependensi, dan kemudahan pengembangan aplikasi Django kita. Oleh karena itu, sangat disarankan untuk menggunakan virtual environment dalam pengembangan proyek Django.

<h1>MVC, MVT, dan MVVM</h1>

MVC, MVT, dan MVVM adalah tiga pola arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi. Meskipun semuanya memiliki konsep dasar yang mirip, mereka digunakan dalam berbagai kerangka kerja dan bahasa pemrograman. Berikut adalah penjelasan singkat tentang masing-masing pola serta perbedaannya:

1. MVC (Model-View-Controller):
   * Model: Mewakili data dan logika bisnis. Ini adalah komponen yang bertanggung jawab untuk mengelola data aplikasi dan memproses logika bisnis.
   * View: Bertanggung jawab untuk tampilan dan presentasi data kepada pengguna. Ini adalah bagian yang menampilkan informasi dari Model ke pengguna.
   * Controller: Bertindak sebagai pengontrol antara Model dan View. Ini mengatur alur kerja aplikasi, menerima masukan dari pengguna, dan mengubah Model atau View sesuai kebutuhan.
   
   Perbedaan: Pada MVC, View dan Controller biasanya lebih terhubung secara erat daripada Model. Model tidak berinteraksi langsung dengan View, tetapi melalui Controller.

2. MVT (Model-View-Template):
   * Model: Mirip dengan MVC, ini adalah komponen yang mengelola data dan logika bisnis.
   * View: Sama dengan MVC, ini adalah bagian yang menampilkan data kepada pengguna.
   * Template: Ini adalah bagian yang berbeda dalam MVT. Template mengatur cara data ditampilkan dalam View. Template berisi HTML dan elemen tampilan lainnya dengan sintaks template yang memungkinkan kita untuk menyisipkan data dari Model ke dalam HTML.
     
   Perbedaan: Perbedaan utama antara MVT dan MVC adalah penggunaan Template sebagai lapisan tambahan yang mengatur tampilan.

2. MVVM (Model-View-ViewModel):
   * Model: Sama dengan Model dalam MVC dan MVT, yaitu komponen yang mengelola data dan logika bisnis.
   * View: Mirip dengan View dalam MVC dan MVT, ini adalah bagian yang menampilkan data kepada pengguna.
   * Model: Ini adalah bagian yang berbeda dalam MVVM. ViewModel bertindak sebagai perantara antara Model dan View. ViewModel mengubah data dari Model menjadi format yang dapat ditampilkan oleh View dan juga menangani tindakan pengguna yang diteruskan ke Model.
     
   Perbedaan: MVVM mengenalkan ViewModel sebagai lapisan tambahan yang memungkinkan pengikatan data yang lebih kuat antara Model dan View. Ini sering digunakan dalam aplikasi berbasis antarmuka pengguna yang kompleks.

Perbedaan utama antara ketiganya adalah bagaimana mereka mengatur interaksi antara Model, View, dan bagian pengontrolnya. MVC adalah pola klasik yang digunakan di banyak kerangka kerja web, MVT adalah varian Django yang menggunakan Template untuk tampilan, sedangkan MVVM adalah pola yang sering digunakan dalam pengembangan aplikasi desktop dan aplikasi berbasis antarmuka pengguna yang kompleks. Pemilihan pola tergantung pada jenis proyek dan kebutuhan pengembangan kita.

</details>
