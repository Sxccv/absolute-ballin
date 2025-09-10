### Website: https://randuichi-touya-absoluteballin.pbp.cs.ui.ac.id/
### Repo: https://github.com/Sxccv/absolute-ballin/

# Checklist

## 1. Membuat sebuah proyek Django baru.
Pertama, buatlah folder baru untuk direktori utama, yaitu absolute-ballin. Selanjutnya, saya menginisialisasi venv python serta requirements yang saya butuhkan untuk proyek dengan ```requirements.txt```, setup ```.env``` dan ```.env.prod```. Langkah terakhir, saya menjalankan ```django-admin startproject absolute_ballin .``` untuk membuat project Django.

## 2. Membuat aplikasi dengan nama main pada proyek tersebut.
Jalankan command ```python manage.py startapp main``` dalam direktori utama dengan console

command ini akan membuat applikasi baru pada project ```absolute_ballin```

## 3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Tambahkan ```'main'``` pada ```INSTALLED_APPS``` pada ```settings.py``` dalam project folder

## 4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
Buatlah class baru bernama Product dengan argumen ```models.Model``` pada ```models.py``` yang berisi atribut wajib seperti yang diminta pada berkas tugas

## 5.  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Membuat fungsi ```home(request)``` pada ```views.py``` yang berisi sebuah dictionary bernama ```data``` yang berisi data nama dan kelas saya. Lalu, fungsi tersebut akan return sebuah httpresponse menggunakan template ```home.html``` dan data pada dictionary ```data```

## 6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
membuat pattern pada ```urls.py``` sebagai ```path('',views.home,name='main_home')``` yang berada pada aplikasi, dan juga menambahkan pattern ```path('', include('main.urls'))``` pada ```urls.py``` yang berada pada project Django

## 7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
melakukan command secara berurut, ```git add .```, ```git commit -m "Finished tugas 2"```, ```git push pws master```

## 8. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
ini sedang dibuat :D

## 9. Bagan yang berisi request client berserta respons
![thisthegraph](Bagan.jpeg)
1. Client mengirim request ke aplilkasi django
2. Aplikasi akan menghandle request dan menyesuaikan path dengan ```urls.py```
3. ```urls.py``` akan menjalankan fungsi yang ada pada ```views.py``` 
4. ```views.py``` akan melakukan komunikasi dengan ```models.py``` yang melakukan komunikasi dengan database untuk retrieve dan store relevant data
5. ```views.py``` akan menyesuaikan data ke dalam template html pada direktori templates pada aplikasi sesuai dengan request
6. ```views.py``` akan menghasilkan ```httpresponse``` dan mengirimkannya kembali kepada client

## 10. Jelaskan ```settings.py```
```settings.py``` berperan sebagai penyimpanan seluruh atribut dan pengaturan penting bagi fungsi dan operasional aplikasi dan project Django. Segala informasi yang menunjuk kepada data yang dibutuhkan untuk menjalankan project terdapat disitu seperti daftar aplikasi, template, database, password, dll.

## 11. Jelaskan migrasi database di Django
Migrasi adalah proses untuk menerapkan perubahan pada models ke dalam schema database secara automatis. 

command ```makemigrations``` digunakan untuk membuat migrations baru berdasarkan perubahan pada models
command ```migrate``` digunakan untuk me-manage (applying and unapplying) migrations yang ada

## 12. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django berguna sebagai titik introduksi pada yang belum sebelumnya mempelajari web development karena Django mostly menggunakan bahasa yang sudah kami gunakan pada DDP1, sehingga fokus pada pembelajaran dapat lebih tersudut kepada cara kerjanya web development. Selain itu, Django memiliki banyak "shortcut" yang mengakibatkan banyak automasi terjadi, dan menurut saya hal tersebut dapat disebut lebih "beginner friendly"

## 13. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
tidak, terimakasih asdos semangat!
