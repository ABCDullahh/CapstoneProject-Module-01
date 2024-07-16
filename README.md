# CapstoneProject-Module-01
Aplikasi CRUD Python (Manajemen Data Karyawan)
# Aplikasi Manajemen Karyawan

## Gambaran Umum

Aplikasi Manajemen Karyawan adalah aplikasi berbasis konsol yang dirancang untuk mengelola data karyawan secara efisien. Aplikasi ini menyediakan fitur lengkap untuk administrator dan karyawan, memungkinkan pengelolaan data karyawan mulai dari penambahan, pembaruan, hingga penghapusan data.

## Fitur

### Fitur untuk Admin
1. **Lihat Data Karyawan**
   - Menampilkan semua data karyawan dalam format tabel yang rapi.
   - Mencari data karyawan berdasarkan ID.
   - Mencari data karyawan berdasarkan kata kunci (Nama, Jabatan, Departemen, Tempat Tinggal, atau Nomor Telepon).

2. **Tambah Akun Karyawan**
   - Menambahkan akun karyawan baru dengan informasi lengkap seperti nama, gender, tanggal lahir, alamat, departemen, jabatan, nomor telepon, dan status.

3. **Perbarui Akun Karyawan**
   - Memperbarui informasi karyawan termasuk nama, gender, tanggal lahir, alamat, departemen, jabatan, nomor telepon, status, dan kata sandi.

4. **Hapus Akun Karyawan**
   - Menghapus akun karyawan berdasarkan ID.
   - Menghapus karyawan berdasarkan departemen.

5. **Logout**
   - Keluar dari akun admin.

6. **Keluar Aplikasi**
   - Menutup aplikasi.

### Fitur untuk Karyawan
1. **Lihat Data Diri**
   - Menampilkan data diri karyawan yang sedang login.

2. **Perbarui Data Diri**
   - Memperbarui nomor telepon dan alamat tempat tinggal.

3. **Logout**
   - Keluar dari akun yang sedang login.

4. **Keluar Aplikasi**
   - Menutup aplikasi.

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
