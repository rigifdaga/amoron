Apa perbedaan antara form POST dan form GET dalam Django?
Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

<h1>LINK</h1>
https://amoron.adaptable.app/
    
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



