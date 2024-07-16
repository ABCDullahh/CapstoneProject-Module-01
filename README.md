# CapstoneProject-Module-01
Aplikasi CRUD Python (Manajemen Data Karyawan)
# Aplikasi Manajemen Karyawan

## Gambaran Umum

Aplikasi Manajemen Karyawan adalah aplikasi berbasis konsol yang dirancang untuk mengelola data karyawan secara efisien. Aplikasi ini menyediakan fitur lengkap untuk administrator dan karyawan, memungkinkan pengelolaan data karyawan mulai dari penambahan, pembaruan, hingga penghapusan data.

## Fitur

### Fitur untuk Admin
1. **Lihat Data Karyawan**
   - Menampilkan semua data karyawan dalam format tabel yang rapi.
   - ![image](https://github.com/user-attachments/assets/60a0faec-b600-48ce-99d0-5844d0fd4691)
   - Mencari data karyawan berdasarkan ID.
   - ![image](https://github.com/user-attachments/assets/fc0adb6e-fb11-4d9b-bbb2-7b5571904455)
   - Mencari data karyawan berdasarkan kata kunci (Nama, Jabatan, Departemen, Tempat Tinggal, atau Nomor Telepon).
   - ![image](https://github.com/user-attachments/assets/8a995902-baf2-4edc-8962-78707f367364)

2. **Tambah Akun Karyawan**
   - Menambahkan akun karyawan baru dengan informasi lengkap seperti nama, gender, tanggal lahir, alamat, departemen, jabatan, nomor telepon, dan status.
   - ![image](https://github.com/user-attachments/assets/e9ecb7f0-5537-4d18-a9c6-df1ef8972e65)

3. **Perbarui Akun Karyawan**
   - Memperbarui informasi karyawan termasuk nama, gender, tanggal lahir, alamat, departemen, jabatan, nomor telepon, status, dan kata sandi.
   - ![image](https://github.com/user-attachments/assets/630a4e42-8008-4cb3-9872-c4796b12ded3)

4. **Hapus Akun Karyawan**
   - Menghapus akun karyawan berdasarkan ID.
   - ![image](https://github.com/user-attachments/assets/9c7b9b0d-ffb4-45ca-a180-51c42f43bc59)
   - Menghapus karyawan berdasarkan departemen.
   - ![image](https://github.com/user-attachments/assets/b0310f4b-31c0-4a60-a3ba-6aa27589dc8a)


5. **Logout**
   - Keluar dari akun admin.
   - ![image](https://github.com/user-attachments/assets/f31e4913-4cb0-4d08-972f-db3de50264fa)

6. **Keluar Aplikasi**
   - Menutup aplikasi.
   - ![image](https://github.com/user-attachments/assets/96a9e5ee-ac25-4858-aaa7-5dbd94aa84a9)

### Fitur untuk Karyawan
1. **Lihat Data Diri**
   - Menampilkan data diri karyawan yang sedang login.
   - ![image](https://github.com/user-attachments/assets/8e4a1dd7-fa5b-4329-90c9-9db65999f2c9)

2. **Perbarui Data Diri**
   - Memperbarui nomor telepon dan alamat tempat tinggal.
   - ![image](https://github.com/user-attachments/assets/74f73245-f5ae-4b5b-a5a5-b88335026ab5)

3. **Logout**
   - Keluar dari akun yang sedang login.
   - ![image](https://github.com/user-attachments/assets/6dbd38a0-ee51-4bb4-b662-4d292ee1493c)

4. **Keluar Aplikasi**
   - Menutup aplikasi.
   - ![image](https://github.com/user-attachments/assets/91c589ce-4509-4e4c-9334-dd943fee709d)

## Cara Penggunaan

### Login
1. Pengguna diminta memasukkan username dan password.
2. Jika login berhasil, pengguna akan diarahkan ke menu utama sesuai dengan peran mereka (Admin atau Karyawan).

### Menu Admin
1. **Data Karyawan**
   - Menampilkan submenu untuk melihat data karyawan, mencari berdasarkan ID, atau mencari dengan kata kunci.

2. **Tambah Akun Karyawan**
   - Meminta input untuk menambahkan karyawan baru, termasuk informasi seperti nama, gender, tanggal lahir, alamat, departemen, jabatan, nomor telepon, dan status.

3. **Perbarui Akun Karyawan**
   - Memperbarui data karyawan berdasarkan ID yang dimasukkan.

4. **Hapus Akun Karyawan**
   - Menghapus data karyawan berdasarkan ID atau departemen.

5. **Logout**
   - Keluar dari akun admin.

6. **Keluar Aplikasi**
   - Menutup aplikasi.

### Menu Karyawan
1. **Data Diri**
   - Menampilkan data diri karyawan yang sedang login.

2. **Perbarui Data Diri**
   - Memperbarui nomor telepon dan alamat tempat tinggal.

3. **Logout**
   - Keluar dari akun karyawan.

4. **Keluar Aplikasi**
   - Menutup aplikasi.

## Validasi Input
- **Username dan Password**: Harus memiliki panjang minimal 4 karakter.
- **Nama**: Tidak boleh mengandung angka atau simbol dan harus memiliki panjang minimal 3 karakter.
- **Tanggal Lahir**: Harus dalam format dd-mm-yyyy dan valid.
- **Gender**: Hanya menerima input "L" untuk Laki-laki dan "P" untuk Perempuan.
- **Nomor Telepon**: Harus memiliki panjang minimal 10 dan maksimal 14 digit, tanpa spasi atau tanda hubung.
- **Status**: Hanya menerima input "Aktif" atau "Tidak Aktif".
- **Departemen dan Jabatan**: Hanya menerima input yang sesuai dengan daftar yang tersedia.

## Instalasi dan Penggunaan
1. Clone repository ini ke lokal Anda.
2. pip install prettytable 
3. pip install maskpass
