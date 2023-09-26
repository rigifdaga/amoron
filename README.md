Nama    : Rifda Aulia Nurbahri

NPM     : 2206081660

Kelas   : PBP D

https://amoron.adaptable.app/

<details>

<summary> Tugas 4 </summary>

<h1> Django UserCreationForm </h1>

Django UserCreationForm adalah formulir yang digunakan untuk membuat pengguna baru yang dapat menggunakan aplikasi web kita. Formulir ini memiliki tiga bidang: username, password1, dan password2 (yang pada dasarnya digunakan untuk konfirmasi password).

Berikut adalah beberapa kelebihan dan kekurangan dari Django UserCreationForm:

Kelebihan:

1. Django UserCreationForm merupakan bagian dari sistem otentikasi pengguna bawaan Django.

2. Formulir ini memiliki fungsi save() yang memungkinkan kita untuk menyimpan instance Pengguna ke dalam basis data.

3. Django UserCreationForm memiliki fitur keamanan bawaan yang cukup kuat untuk melindungi aplikasi web dari ancaman seperti SQL injection, Cross-site scripting, Clickjacking dan berbagai bentuk serangan lainnya.

Kekurangan:

1. Django secara umum dianggap sebagai perangkat lunak monolitik yang besar. Hal ini memungkinkan komunitas untuk mengembangkan ratusan modul dan aplikasi yang dapat digunakan kembali, tetapi juga membatasi kecepatan pengembangan Django.

2. Django perlu mempertahankan kompatibilitas mundur, sehingga perkembangannya berlangsung lambat.

3. Kerangka kerja ini mendorong kita ke dalam pola tertentu, tetapi lebih menyenangkan ketika kita dapat memprogram sendiri memilih arsitektur, struktur, dan pola desain.

<h1> Perbedaan Antara Autentikasi dan Otorisasi dalam Konteks Django </h1>

Dalam konteks Django, autentikasi dan otorisasi memiliki peran yang sangat penting dan berbeda:

Autentikasi adalah proses verifikasi identitas pengguna. Dengan kata lain, sistem memastikan bahwa pengguna adalah siapa yang mereka klaim. Misalnya, ketika pengguna mencoba masuk, sistem akan memeriksa apakah kombinasi nama pengguna dan kata sandi yang diberikan cocok dengan apa yang ada di basis data.

Otorisasi, di sisi lain, menentukan apa yang dapat dilakukan pengguna yang telah terautentikasi. Ini berarti sistem memeriksa hak akses pengguna dan memutuskan apakah mereka diizinkan untuk melakukan tindakan tertentu (misalnya, mengedit atau menghapus suatu pos).

Kedua konsep ini penting karena mereka membantu menjaga keamanan aplikasi web Django. Autentikasi membantu mencegah akses yang tidak sah dengan memastikan hanya pengguna yang sah yang dapat masuk. Sementara itu, otorisasi membantu mencegah penyalahgunaan aplikasi dengan membatasi apa yang dapat dilakukan pengguna setelah mereka masuk.

<h1>Cookies dalam Konteks Aplikasi Web</h1>

Cookies dalam konteks aplikasi web adalah file teks kecil yang berisi potongan data — seperti nama pengguna dan kata sandi — yang digunakan untuk mengidentifikasi komputer kita saat kita menggunakan jaringan. Cookies spesifik digunakan untuk mengidentifikasi pengguna spesifik dan meningkatkan pengalaman browsing web mereka.

Django menggunakan cookies dalam manajemen sesi pengguna. Django menyediakan kerangka kerja sesi yang memungkinkan kita menyimpan dan mengambil data secara acak berdasarkan setiap pengunjung situs. Django mengabstraksi proses pengiriman dan penerimaan cookies, dengan menempatkan cookie ID sesi di sisi klien, dan menyimpan semua data terkait di sisi server. Dengan cara ini, hanya ID sesi yang terlihat oleh pengguna, sementara data sesi tetap tersembunyi di server.

Untuk menggunakan sesi berbasis cookies, kita dapat mengatur pengaturan SESSION_ENGINE menjadi “django.contrib.sessions.backends.signed_cookies”. Data sesi akan disimpan menggunakan alat Django untuk penandatanganan kriptografis dan pengaturan SECRET_KEY.

Penting untuk dicatat bahwa meskipun cookies sangat berguna untuk mempertahankan status aplikasi dan memberikan pengalaman yang dipersonalisasi kepada pengguna, mereka juga dapat menimbulkan masalah privasi jika tidak ditangani dengan benar. Oleh karena itu, penting untuk selalu menggunakan praktek terbaik keamanan saat bekerja dengan cookies.

<h1>Keamanan Penggunaan Cookies</h1>

Penggunaan cookies dalam pengembangan web umumnya dianggap aman. Cookies sendiri cukup tidak berbahaya; mereka diproses dan disimpan oleh browser web kita dan sangat penting untuk beberapa fungsi di situs web. Mereka tidak menyebar virus atau malware. Mereka tidak dapat membaca dokumen atau informasi lain dari hard drive kita. Mereka tidak mengetahui dan tidak mengandung kata sandi kita, alamat email kita, atau informasi pribadi lainnya.

Namun, meskipun cookies secara umum aman, ada beberapa risiko keamanan dan privasi yang perlu diwaspadai:

1. Pelacakan Pengguna: Cookies dapat digunakan oleh situs web untuk melacak perilaku pengguna, yang dapat menimbulkan masalah privasi.

2. Serangan Pencurian Cookie (Cookie Theft): Jika seorang penyerang dapat mencuri cookie dari pengguna, mereka mungkin dapat menyamar sebagai pengguna tersebut.

3. Serangan Pemalsuan Permintaan Situs Lintas (Cross-Site Request Forgery): Seorang penyerang dapat memanfaatkan fakta bahwa cookies disertakan dalam setiap permintaan ke situs web untuk memaksa pengguna melakukan tindakan yang tidak mereka inginkan.

<h1>Implementasi Checklist</h1>

<h2>Mengimplementasi Fungsi Registrasi, Login, dan Logout</h2>

1. Mengimplementasi Fungsi Registrasi
Pertama-tama saya membuka `views.py` yang ada pada subdirektori `main` dan membuat fungsi dengan nama `register` yang menerima parameter `request`. Saya mengimpor `redirect`, `UserCreationForm`, dan `messages` untuk keperluan fungsi ini. 

```python
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```

Berikut adalah fungsi `register` yang dibuat

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

Setelah itu saya membuat laman `register.html` pada `main/templates`

```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

Saya juga mengimpor fungsi `register` ke `urls.py` dan menambahkan path url ke dalam `urlpatterns`

```python
from main.views import register
```

```python
path('register/', register, name='register'),
```

2. Mengimplementasi Fungsi Login
Pada `views.py` saya menambahkan import `authenticate` dan `login`

```python
from django.contrib.auth import authenticate, login
```

Selanjutnya saya membuat fungsi `login`

```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

Saya juga membuat laman `login.html` baru pada `main/templates`

```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

Pada `urls.py` saya mengimport fungsi `login_user` dan menambahkan path url ke dalam `urlpatterns`

```python
from main.views import login_user
```

```python
...
path('login/', login_user, name='login'),
...
```

3. Mengimplementasikan Fungsi Logout
Pada `views.py` saya menambahkan import `logout`

```python
from django.contrib.auth import logout
```

Kemudian saya membuat fungsi `logout` dengan parameter `request`

```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Saya juga menambahkan button logout pada `main.html` yang ada pada `main/templates`

```html
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```

Terakhir saya membuka `urls.py` kembali yanga da pada folder `main` untuk mengimport fungsi `logout_user` yang telah dibuat dan menambahkan path url ke dalam `urlpatterns`

```python
from main.views import logout_user
```

```python
...
path('logout/', logout_user, name='logout'),
...
```

<h2>Membuat 2 Akun Pengguna dengan 3 Dummy Data</h2>

Pertama-tama saya menjalankan `python manage.py runserver` pada direktori lokal `amoron`. Setelah server berhasil dijalankan saya membuka `http://localhost:8000/`. Pada laman tersebut saya melakukan `register`. Register ini dilakukan pada `register.html` yang telah saya buat. Saya membuat dua akun dengan username `rifda` dan `hantu`. Setelah akun berhasil dibuat, saya melakukan login pada masing-masing akun, tampilan login ini sesuai dengan `login.html` yang telah saya buat. Terakhir saya menambahkan tiga dummy data dengan klik tombol `Add New Product`


<h2>Menghubungkan Model Item dengan User</h2>

Hal yang pertama saya lakukan adalah membuka `models.py` yang ada pada subdirektori `main` dan melakukan import

```python
from django.contrib.auth.models import User
```

Pada model `Product` yang telah dibuat saya menambahkan kode berikut

```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

Setelah itu, pada `views.py` saya mengubah bagian conditional if pada kode fungsi `create_product`menjadi sebagai berikut

```python
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```

Pada fungsi `show_main` saya juga mengubah variable `products` menjadi sebagauiberikut agar `Product` yang ditampilkan adalah `Product` yang terasosiasikan dengan pengguna yang sedang login

```python
def show_main(request):
    products = Product.objects.filter(user=request.user)
...
```

Karena melakukan modifikasi pada model maka saya melakukan migrasi model dengan menjalankan `python manage.py makemigration` serta `python manage.py migrate`.

<h2>Menampilkan detail informasi pengguna yang sedang Logged in</h2>

Untuk menampilkan pengguna yang sedang login saya hanya mengganti value dari `name` pada fungsi `show_main` yang ada pada `view.py` menjadi seperti berikut

```python
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
    }
```

Saya menerapkan cookies untuk menambahkan data last login dan menampilkannya ke halaman main.

Pertama-tama saya melakukan impor  `HttpResponseRedirect`, `reverse`, dan `datetime` pada `views.py` yang ada di subdirektori `main`

```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

Pada fungsi `login_user` saya mengganti kode yang ada pada blok `if user is nor None` untuk menambahkan cookie `last_login` agar dapat melihat kapan terakhir kali pengguna melakukan login

```python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

Saya juga mengubah fungsi `show_main` dengan menambahkan key `last_login` seperti berikut

```python
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'app': 'Amoron Rental',
        'kelas' : 'PBP D',
        'products' : products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```

Pada fungsi `logout_user` juga diubah menjadi seperti berikut

```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Terakhir, untuk menampilkan data last login pada laman, saya menambahkan kode berikut pada `main.html`

```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

<h1> BONUS </h1>

Berikut adalah pengimplementasian tombol `Delete`, `Increment Amount`, dan `Decrement Amount` yang fungsional

[![message-Image-1695724041601.jpg](https://i.postimg.cc/rmD4905m/message-Image-1695724041601.jpg)](https://postimg.cc/0MqrkNWR)

</details>

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
http://localhost:8000 untuk get html

[![message-Image-1694872656652.jpg](https://i.postimg.cc/bJwXJbb2/message-Image-1694872656652.jpg)](https://postimg.cc/Y4ZDDvdp)

[![message-Image-1695176106233.jpg](https://i.postimg.cc/3rcy4GVV/message-Image-1695176106233.jpg)](https://postimg.cc/G9v364cx)

[![message-Image-1695176353307.jpg](https://i.postimg.cc/pVhjBkfR/message-Image-1695176353307.jpg)](https://postimg.cc/6TKTWrbm)

[![message-Image-1695176353307.jpg](https://i.postimg.cc/pVhjBkfR/message-Image-1695176353307.jpg)](https://postimg.cc/6TKTWrbm)

`notes : screenshot get html diambil ketika saya menambahkan data baru jadi untuk get xml dan json isinya cuman ada dua product`

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
2. Manajemen Dependensi : Virtual environment memungkinkan kita untuk menginstal dan mengelola dependensi proyek secara terisolasi. Kita dapat membuat daftar dependensi proyek kita dalam berkas seperti requirements.txt.
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
