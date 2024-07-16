from prettytable import PrettyTable  # library untuk membuat tabel dengan tampilan yang menarik dan menyesuaikan panjang karakter data
import maskpass                      # library untuk masking password

# Inisialisasi data karyawan sebagai dictionary dalam list
data_karyawan = [
    {"ID": "HR001", "Nama": "Chika Yulianti", "Gender": "P", "Tanggal Lahir": "15-01-1993", "Tempat Tinggal": "JL JEMB 3, PENJARINGAN, JAKARTA UTARA", "Departemen": "HR", "Jabatan": "MANAGER", "Telepon": "0812-8768-3214", "Status": "Aktif"},
    {"ID": "IT001", "Nama": "Faizal Lutfi Yoga Triadi", "Gender": "L", "Tanggal Lahir": "22-04-1998", "Tempat Tinggal": "JL DURIAN UTARA, BANYUMANIK, SEMARANG", "Departemen": "IT", "Jabatan": "SENIOR", "Telepon": "0812-1575-8979", "Status": "Tidak Aktif"},
    {"ID": "FI001", "Nama": "Yusuf Firmansyah", "Gender": "L", "Tanggal Lahir": "09-07-1995", "Tempat Tinggal": "JL DAAN MOGOT, KALIDERES, JAKARTA BARAT", "Departemen": "FINANCE", "Jabatan": "ASSISTANT", "Telepon": "0813-1500-9757", "Status": "Aktif"},
    {"ID": "MA001", "Nama": "Lina Permata", "Gender": "P", "Tanggal Lahir": "25-03-1990", "Tempat Tinggal": "JL KEMBANGAN 2, KEMBANGAN, JAKARTA BARAT", "Departemen": "MARKETING", "Jabatan": "MANAGER", "Telepon": "0812-1234-5678", "Status": "Aktif"},
    {"ID": "MA002", "Nama": "Budi Santoso", "Gender": "L", "Tanggal Lahir": "30-08-1985", "Tempat Tinggal": "JL CEMPAKA PUTIH, CEMPAKA PUTIH, JAKARTA PUSAT", "Departemen": "MARKETING", "Jabatan": "SENIOR", "Telepon": "0812-8765-4321", "Status": "Aktif"},
    {"ID": "HR002", "Nama": "Dewi Anggraeni", "Gender": "P", "Tanggal Lahir": "12-12-1992", "Tempat Tinggal": "JL GADING SERPONG, TANGERANG", "Departemen": "HR", "Jabatan": "ASSISTANT", "Telepon": "0813-6789-1234", "Status": "Aktif"},
    {"ID": "IT002", "Nama": "Arif Rahman", "Gender": "L", "Tanggal Lahir": "05-05-1997", "Tempat Tinggal": "JL KARANG ANYAR, KARANG ANYAR, SEMARANG", "Departemen": "IT", "Jabatan": "JUNIOR", "Telepon": "0812-8765-4322", "Status": "Aktif"},
    {"ID": "FI002", "Nama": "Rina Kartika", "Gender": "P", "Tanggal Lahir": "18-11-1994", "Tempat Tinggal": "JL SUDIRMAN, BANDUNG", "Departemen": "FINANCE", "Jabatan": "MANAGER", "Telepon": "0813-6789-5678", "Status": "Aktif"}
]

# Data login pengguna (username:password)
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "chika": {"password": "chika123", "role": "karyawan", "id": "HR001"},
    "faizal": {"password": "faizal123", "role": "karyawan", "id": "IT001"},
    "yusuf": {"password": "yusuf123", "role": "karyawan", "id": "FI001"},
    "lina": {"password": "lina123", "role": "karyawan", "id": "MA001"},
    "budi": {"password": "budi123", "role": "karyawan", "id": "MA002"},
    "dewi": {"password": "dewi123", "role": "karyawan", "id": "HR002"},
    "arif": {"password": "arif123", "role": "karyawan", "id": "IT002"},
    "rina": {"password": "rina123", "role": "karyawan", "id": "FI002"}
}

# List departemen dan jabatan untuk pembatasan input
departemen_list = ["HR", "FINANCE", "MARKETING", "IT", "CUSTOMER SERVICE", "LOGISTICS"]
jabatan_list = ["SENIOR", "JUNIOR", "ASSISTANT", "MANAGER"]

#Fungsi untuk login yang dijalankan sebelum masuk ke menu utama
def login():            
    while True:                                                                         # while true digunakan untuk melakukan perulangan tak terbatas dan diberhentikan ketika break 
        print("\n+---------------------+")
        print("|    KARYA MANAGER    |")
        print("+=====================+")
        print("| 1. Login            |")
        print("| 2. Keluar Aplikasi  |")
        print("+---------------------+")
        pilihan = input("Pilih menu (1-2): ").strip()
        if pilihan == '1':
            while True:
                username = input("Masukkan username: ").strip()                         # strip() digunakan untuk menghapus spasi di awal dan akhir sebuah string
                password = maskpass.askpass("Masukkan password: ", mask="*").strip()    # maskpass.askpass() digunakan untuk memunculkan tanda bintang (*) pada password yang diketik
                if username in users and users[username]["password"] == password:       # Mengecek apakah username yang diinputkan ada di dalam dictionary users dan password yang diinputkan sesuai
                    print(f"\nLogin berhasil! Selamat datang, {username}.")
                    return users[username]
                else:
                    print("\nUsername atau password salah.")
                    while True:
                        retry = input("Apakah Anda ingin mencoba lagi? (y/n): ").strip().lower() # lower() digunakan untuk mengubah semua huruf inputan menjadi huruf kecil
                        if retry == 'n':                                                # Keluar dari y/n
                            break
                        elif retry == 'y':
                            break
                        else:
                            print("Pilihan tidak valid. Silakan pilih 'y' atau 'n'.")
                    if retry == 'n':                                                    # Keluar dari input username/passowrd
                        break
        elif pilihan == '2':
            while True:
                exit_konfirmasi = input("Apakah Anda ingin keluar dari aplikasi? (y/n): ").strip().lower()
                if exit_konfirmasi == 'y':
                    print("Terima kasih! Sampai jumpa! (Keluar dari aplikasi).")
                    return "" # keluar dari aplikasi
                elif exit_konfirmasi == 'n':
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih 'y' atau 'n'.")
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Fungsi untuk mengenerate ID karyawan berdasarkan dari nama departemen
def generate_id(departemen):
    prefix_dict = {      #Deklarasi nama prefix/imbuhan berdasarkan nama departemen
        "HR": "HR",
        "FINANCE": "FI",
        "MARKETING": "MA",
        "IT": "IT",
        "CUSTOMER SERVICE": "CS",
        "LOGISTICS": "LO"
    }
    prefix = prefix_dict[departemen]
    existing_ids = [karyawan["ID"] for karyawan in data_karyawan if karyawan["ID"].startswith(prefix)]       # Mencari id yang dimulai dengan prefix
    if len(existing_ids) == 0:                                                                               # Apabila id dengan prefix yang diloop tidak ditemukan dalam list data_karyawan, maka id baru akan dibuat
        new_id = f"{prefix}001"
    else:
        last_id = max(existing_ids)                                                                          # Apabila id dengan prefix yang diloop ditemukan dalam list data_karyawan, maka id terakhir akan diambil lalu ditambahkan 1
        new_number = int(last_id[len(prefix):]) + 1
        new_id = f"{prefix}{new_number:03d}"                                                                 # Menggabungkan prefix dan penomoran baru dengan format nomor 3 digit
    return new_id

# Fungsi untuk menampilkan menu admin
def tampilkan_menu_admin():
    print("\n+---------------------------+")
    print("|         MENU ADMIN        |")
    print("+===========================+")
    print("| 1. Data Karyawan          |")
    print("| 2. Tambah Akun Karyawan   |")
    print("| 3. Perbarui Akun Karyawan |")
    print("| 4. Hapus Akun Karyawan    |")
    print("| 5. Logout                 |")
    print("| 6. Keluar Aplikasi        |")
    print("+---------------------------+")
    pilihan = input("Pilih menu (1-5): ")
    return pilihan

# Fungsi untuk menampilkan menu karyawan
def tampilkan_menu_karyawan():
    print("\n+=============================+")
    print("|         MENU KARYAWAN       |")
    print("+=============================+")
    print("|  1. Data Diri               |")
    print("|  2. Perbarui Data Diri      |")
    print("|  3. Logout                  |")
    print("|  4. Keluar Aplikasi         |")
    print("+=============================+")
    pilihan = input("Pilih menu (1-3): ")
    return pilihan

# Fungsi untuk menampilkan sub menu read
def tampilkan_sub_menu_baca():
    print("\n+--------------------------------------------+")
    print("|             MENU DATA KARYAWAN             |")
    print("+============================================+")
    print("| 1. Tampilkan Seluruh Data Karyawan         |")
    print("| 2. Cari Data Karyawan Berdasarkan ID       |")
    print("| 3. Cari Data Karyawan                      |")
    print("| 4. Kembali ke Menu Utama                   |")
    print("+--------------------------------------------+")
    pilihan = input("Pilih menu (1-4): ")
    return pilihan

# Fungsi untuk mencari username pada data users berdasarkan ID
def get_username_by_id(karyawan_id):
    for username, info in users.items():                            # Melakukan looping pada dictionary users
        if info.get('id') == karyawan_id:                           # Memeriksa apakah id yang ada pada dictionary users sama dengan ID yang diberikan oleh karyawan_id (mencari value dari key 'id')
            return username                                         # Mengembalikan username
    return ""

# Fungsi untuk mencari password pada data users berdasarkan username
def get_password_by_username(username):                             
    if username in users:
        return users[username]['password']
    return ""

# Fungsi untuk menampilkan data karyawan dalam bentuk table menggunakan PrettyTable
def tampilkan_tabel(data):
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Gender", "Tanggal Lahir", "Tempat Tinggal", "Departemen", "Jabatan", "No Handphone", "Status Karyawan", "Username", "Password"]    # Membuat header table PrettyTable
    for karyawan in data:
        gender_tampilan = "Laki-laki" if karyawan["Gender"] == "L" else "Perempuan"                          # Mengubah tampilan gender menjadi Laki-laki dan Perempuan
        username = get_username_by_id(karyawan["ID"])
        password = get_password_by_username(username)
        tabel.add_row([karyawan["ID"], karyawan["Nama"], gender_tampilan, karyawan["Tanggal Lahir"], karyawan["Tempat Tinggal"], karyawan["Departemen"], karyawan["Jabatan"], karyawan["Telepon"], karyawan["Status"], username, password])   # Mengisi baris table PrettyTable dengan data pada list data_karyawan
    print(tabel)    # print tabel dalam bentuk prettytable

# Fungsi untuk menampilkan data departemenn dalam bentuk table menggunakan PrettyTable
def tampilkan_tabel_departemen():
    tabel = PrettyTable()
    tabel.field_names = ["Departemen"]
    for departemen in departemen_list:
        tabel.add_row([departemen])
    print(tabel)

# Fungsi untuk menampilkan data jabatan dalam bentuk table menggunakan PrettyTable
def tampilkan_tabel_jabatan():
    tabel = PrettyTable()
    tabel.field_names = ["Jabatan"]
    for jabatan in jabatan_list:
        tabel.add_row([jabatan])
    print(tabel)

# Fungsi untuk menformat nomor telepon agar dipisah menjadi tiga bagian dengan masing masing bagian berisi 4 digit
def format_telepon(telepon):
    return f"{telepon[:4]}-{telepon[4:8]}-{telepon[8:]}"

# Fungsi untuk memvalidasi tanggal lahir
def validasi_tanggal(tanggal):
    bagian = tanggal.split('-')                                # Memisahkan tanggal menggunakan tanda hubung "-" dengan fungsi split()
    if len(bagian) != 3:
        print("\nMasukkan tanggal lahir yang valid (dd-mm-yyyy).")
        return False
    
    hari, bulan, tahun = bagian                                # Tanggal yang sudah terpisah harus terbagi menjadi 3 bagian
    
    if tahun.isdigit() and bulan.isdigit() and hari.isdigit(): # Memastikan setiap bagian harus berupa angka dan melakukan casting ke integer agar dapat dilakukan perhitungan
        hari = int(hari)                                       # isdigit() digunakan untuk memeriksa apakah setiap bagian berupa angka
        bulan = int(bulan)
        tahun = int(tahun)
    else:
        print("\nMasukkan tanggal lahir yang valid (dd-mm-yyyy).")
        return False

    # Validasi rentang tahun
    if 1900 <= tahun <= 2024:
        # Validasi bulan
        if 1 <= bulan <= 12:
            if bulan == 2:
                if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0): # Mencari apakah tahun kabisat untuk bulan februari
                    if hari <= 29:
                        return True
                    else:
                        print("\nTanggal tidak valid (maksimal tanggal 29).")
                        return False
                else:
                    if hari <= 28:
                        return True
                    else:
                        print("\nTanggal tidak valid (maksimal tanggal 28).")
                        return False
            elif bulan in [4, 6, 9, 11]:        # bulan yang memiliki tanggal 30
                if hari <= 30:
                    return True
                else:
                    print(f"\nTanggal tidak valid (maksimal tanggal 30).")
                    return False
            else:
                if hari <= 31:
                    return True
                else:
                    print(f"\nTanggal tidak valid (maksimal tanggal 31).")
                    return False
        else:
            print("\nMasukkan bulan yang valid (1-12).")
            return False
    else:
        print("\nMasukkan tahun yang valid.")
        return False

# Fungsi untuk memvalidasi gender (membatasi inputan, gender harus L/P)
def validasi_gender(gender):
    if gender in ["L", "P"]: 
        return True         # Mengembalikan True jika parameter gender sesuai
    print("\nMasukkan gender yang valid (L untuk Laki-laki, P untuk Perempuan).")
    return False

# Fungsi untuk memvalidasi nama (membatasi inputan, nama harus minimal 3 karakter dan tidak boleh mengandung simbol atau angka)
def validasi_nama(nama):
    if len(nama.replace(' ', '')) < 3:       # replace digunakan untuk menghilangkan spasi, menggantikan space dengan string kosong dan menghitung apakah panjang nama sudah 3 digit 
        print("\nNama harus memiliki panjang minimal 3 karakter.")
        return False
    if nama.replace(' ', '').isalpha():      # isalpha digunakan untuk mengecek apakah setiap inputan adalah a-z
        return True
    print("\nNama tidak boleh mengandung simbol atau angka.")
    return False

# Fungsi untuk memvalidasi status (membatasi inputan, status harus aktif/tidak aktif)
def validasi_status(status):
    if status in ["Aktif", "Tidak Aktif"]:
        return True
    print("\nMasukkan status yang valid (Aktif atau Tidak Aktif).")
    return False

# Fungsi untuk memvalidasi departemen (membatasi inputan, departemen harus sesuai pada list departemen_list)
def validasi_departemen(departemen):
    if departemen in departemen_list:
        return True
    print("\nMasukkan departemen yang valid (ketik sesuai pada daftar departemen)")
    return False

# Fungsi untuk memvalidasi jabatan (membatasi inputan, jabatan harus sesuai pada list jabatan_list)
def validasi_jabatan(jabatan):
    if jabatan in jabatan_list:
        return True
    print("\nMasukkan jabatan yang valid (ketik sesuai pada daftar jabatan)")
    return False

# Fungsi untuk mencari data karyawan berdasarkan ID pada list data_karyawan
def cari_karyawan_by_id(id_karyawan):
    for karyawan in data_karyawan:
        if karyawan["ID"] == id_karyawan:
            return karyawan
    return "Data tidak ditemukan"

# Fungsi untuk mencari username berdasarkan id pada dictionary users
def cari_username_by_id(id_karyawan):
    for username, user_data in users.items():
        if user_data.get("id") == id_karyawan:
            return username
    return ""

# Fungsi untuk memvalidasi inputan create dan update username dan password agar tidak kosong dan panjangnya minimal 4
def validasi_username_password(username_password):
    if len(username_password) < 4:
        print("\nUsername dan password harus memiliki panjang minimal 4 karakter.")
        return False
    return True

# Fungsi untuk menambahkan akun karyawan
def tambah_akun_karyawan():
    while True:
        
        print("\n+===============================+")
        print("|    TAMBAH AKUN KARYAWAN       |")
        print("+===============================+")
        print("| 1. Tambah Akun Karyawan       |")
        print("| 2. Kembali ke Menu Utama      |")
        print("+===============================+")
        pilihan = input("Pilih menu (1-2): ")
        if pilihan == "1":
            while True:
                nama = input("Masukkan Nama Karyawan: ").strip().title() 
                if len(nama) != 0 and validasi_nama(nama):          # Validasi inputan nama
                    break
                else:
                    print("Nama tidak boleh kosong dan tidak boleh mengandung angka dan simbol.")
                
            
            while True:
                gender = input("Masukkan Gender Karyawan (L/P): ").strip().upper() # upper digunakan untuk mengubah semua inputan huruf menjadi huruf kapital
                if validasi_gender(gender):
                    break

            while True:
                tanggal_lahir = input("Masukkan Tanggal Lahir Karyawan (dd-mm-yyyy): ").strip()
                if validasi_tanggal(tanggal_lahir):
                    break

            while True:
                tempat_tinggal = input("Masukkan Tempat Tinggal Karyawan: ").strip().upper()
                if 3 < len(tempat_tinggal) != 0:
                    break
                print("\nTempat tinggal tidak boleh kosong atau kurang dari 3 karakter.")
            
            while True:
                print("\nDaftar Departemen:")
                tampilkan_tabel_departemen()
                departemen = input("Masukkan Departemen Karyawan: ").strip().upper()
                if validasi_departemen(departemen):
                    break
            
            while True:
                print("\nDaftar Jabatan:")
                tampilkan_tabel_jabatan()
                jabatan = input("Masukkan Jabatan Karyawan: ").strip().upper()
                if validasi_jabatan(jabatan):
                    break

            while True:
                telepon = input("Masukkan Nomor Handphone Karyawan (Tanpa spasi atau tanda hubung): ").strip()
                if 10 <= len(telepon) <= 14 and telepon.isdigit():
                    telepon = format_telepon(telepon)
                    break
                print("\nMasukkan Nomor Handphone yang valid (Panjang minimal 10 dan maksimal 14 digit, tanpa spasi atau tanda hubung).")

            while True:
                status = input("Masukkan Status Karyawan (Aktif/Tidak Aktif): ").strip().title()
                if validasi_status(status):
                    break

            id_karyawan = generate_id(departemen)
            print(f"\nID Karyawan baru: {id_karyawan}")

            # Validasi pemembuatan username dan password
            while True:
                username = input("Masukkan username baru: ").strip()
                if username in users:
                    print("\nUsername sudah ada, coba username lain.")
                elif 4 < len(username) == 0 and len(username) < 4:
                    print("\nUsername tidak boleh kosong atau kurang dari 4 karakter.")
                elif validasi_username_password(username):
                    break
            while True:
                password = input("Masukkan password: ").strip()
                if len(password) == 0 and len(password) < 4:
                    print("\nPassword tidak boleh kosong atau kurang dari 4 karakter.")
                elif validasi_username_password(password):
                    break
            
            # Menambahkan data karyawan dan akun
            while True:
                penambahan_konfirmasi = input("Apakah Anda ingin menambahkan akun karyawan dan data karyawan? (y/n): ").strip().lower()
                if penambahan_konfirmasi == 'y':                                                            # Menambahkan data kedalam list data_karyawan menggunakan append
                    data_karyawan.append({
                        "ID": id_karyawan,
                        "Nama": nama,
                        "Gender": gender,
                        "Tanggal Lahir": tanggal_lahir,
                        "Tempat Tinggal": tempat_tinggal,
                        "Departemen": departemen,
                        "Jabatan": jabatan,
                        "Telepon": telepon,
                        "Status": status
                    })
                    users[username] = {"password": password, "role": "karyawan", "id": id_karyawan}         # Menambahkan username, password, dan id ke dictionary users 
                    print("\nAkun karyawan dan data karyawan berhasil ditambahkan.")
                    break
                elif penambahan_konfirmasi == 'n':
                    print("\nAkun karyawan dan data karyawan tidak ditambahkan.")
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Fungsi untuk menampilkan data karyawan
def baca_data_karyawan():
    while True:
        pilihan = tampilkan_sub_menu_baca()
        if pilihan == '1':
            print("\nData seluruh karyawan:")
            if len(data_karyawan) == 0:              # Cek apakah list data_karyawan kosong
                print("\nTidak ada data karyawan.")
            else:
                tampilkan_tabel(data_karyawan)
        elif pilihan == '2':
            if len(data_karyawan) == 0:
                print("\nTidak ada data karyawan.")
                continue
            else:
                print("\n+=================================+")
                print("|     CARI DATA AKUN KARYAWAN     |")
                print("|          BERDASARKAN ID         |")
                print("+=================================+")
                id_karyawan = input("Masukkan ID Karyawan: ").strip().upper()
                karyawan = cari_karyawan_by_id(id_karyawan)
                
                if karyawan == "Data tidak ditemukan":
                    print(karyawan)
                else:
                    tampilkan_tabel([karyawan])
        elif pilihan == '3':
            if len(data_karyawan) == 0:
                print("\nTidak ada data karyawan.")
                continue
            else:
                print("\n+==================================+")
                print("|     CARI DATA AKUN KARYAWAN      |")
                print("+==================================+")
                keyword = input("Masukkan kata kunci pencarian (Nama, Jabatan, Departemen, Tempat Tinggal atau Telepon): ").strip().lower()
                if len(keyword) == 0:
                    print("\nKata kunci pencarian tidak boleh kosong.")
                    continue
                hasil_cari = []                     # List untuk menyimpan hasil pencarian
                for karyawan in data_karyawan:      # Looping untuk mencari karyawan dalam list data_karyawan berdasarkan kata kunci
                    if keyword in karyawan['Nama'].lower() or keyword in karyawan['Jabatan'].lower() or keyword in karyawan['Departemen'].lower()or keyword in karyawan['Tempat Tinggal'].lower() or keyword in karyawan['Telepon'].lower():
                        hasil_cari.append(karyawan)

                if len(hasil_cari) == 0:
                    print("\nData karyawan tidak ditemukan.")
                else:
                    tampilkan_tabel(hasil_cari)
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Fungsi untuk memperbarui data karyawan dalam list data_karyawan dan dictionary users
def perbarui_data_karyawan(user): 
    if user["role"] == "karyawan":                          # Menampilkan menu perbarui data karyawan pada tampilan karyawan 
        karyawan = cari_karyawan_by_id(user["id"])          # Menyesuaikan data karyawan berdasarkan ID yang sudah login
        while True:
            print("\n+===============================+")
            print("|      PERBARUI DATA DIRI       |")
            print("+===============================+")
            print("| 1. Perbarui Nomor Handphone   |")
            print("| 2. Perbarui Tempat Tinggal    |")
            print("| 3. Kembali ke Menu Utama      |")
            print("+===============================+")
            pilihan = input("Pilih menu (1-3): ")

            if pilihan == '1':
                while True:
                    telepon_baru = input("Masukkan Nomor Handphone Baru Karyawan (Tanpa spasi atau tanda hubung): ").strip()
                    if 10 <= len(telepon_baru) <= 14 and telepon_baru.isdigit():
                        while True:
                            perubahan_konfirmasi = input(f"Apakah Anda yakin ingin mengubah Nomor Handphone menjadi '{telepon_baru}'? (y/n): ").strip().lower()
                            if perubahan_konfirmasi == 'y':
                                karyawan['Telepon'] = format_telepon(telepon_baru)              # Mengganti 'Telepon' pada list data_karyawan isi dari variabel telepon_baru
                                print("\nData karyawan berhasil diperbarui.")
                                break
                            elif perubahan_konfirmasi == 'n':
                                print("\nPengubahan Nomor Handphone dibatalkan.")
                                break
                            else:
                                print("\nPilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                        break
                    else:
                        print("\nMasukkan Nomor Handphone yang valid (Panjang minimal 10 dan maksimal 14 digit, tanpa spasi atau tanda hubung).")
                
            elif pilihan == '2':
                while True:
                    tempat_tinggal_baru = input("Masukkan Tempat Tinggal Baru Karyawan: ").strip().upper()
                    if 3 < len(tempat_tinggal_baru) != 0:
                        while True:
                            perubahan_konfirmasi = input(f"Apakah Anda yakin ingin mengubah Tempat Tinggal menjadi '{tempat_tinggal_baru}'? (y/n): ").strip().lower()
                            if perubahan_konfirmasi == 'y':
                                karyawan['Tempat Tinggal'] = tempat_tinggal_baru            # Mengganti 'Tempat Tinggal' pada list data_karyawan dengan isi dari variabel tempat_tinggal_baru
                                print("\nData karyawan berhasil diperbarui.")
                                break
                            elif perubahan_konfirmasi == 'n':
                                print("\nPengubahan Tempat Tinggal dibatalkan.")
                                break
                            else:
                                print("\nPilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                        break
                    else:
                        print("\nTempat tinggal tidak boleh kosong atau kurang dari 3 karakter.")
                
            elif pilihan == '3':
                return
            else:
                print("\nPilihan tidak valid.")
    else:
        while True:                             # Menampilkan menu perbarui data karyawan pada tampilan admin
            print("\n+===================================+")
            print("|    PERBARUI DATA AKUN KARYAWAN    |")
            print("+===================================+")
            print("| 1. Perbarui Data Karyawan         |")
            print("| 2. Kembali ke Menu Utama          |")
            print("+===================================+")
            pilihan = input("Pilih menu (1-2): ")
            
            if pilihan == '1':
                id_karyawan = input("Masukkan ID Karyawan yang ingin diperbarui: ").strip().upper()
                karyawan = cari_karyawan_by_id(id_karyawan)
                
                if karyawan == "Data tidak ditemukan":
                    print(karyawan)
                    continue
                print("\nBerikut merupakan data karyawan yang ingin diubah : ")
                tampilkan_tabel([karyawan])
                while True:
                    konfirmasi = input("Apakah Anda yakin ingin memperbarui data ini? (y/n): ").strip().lower()
                    if konfirmasi == 'y':
                        while True:
                            # Menampilkan kolom yang ingin diubah (sub sub menu perbarui data karyawan)
                            print("\nPilih kolom yang ingin diubah:")
                            print("1. Nama")
                            print("2. Gender")
                            print("3. Tanggal Lahir")
                            print("4. Tempat Tinggal")
                            print("5. Departemen")
                            print("6. Jabatan")
                            print("7. Nomor Handphone")
                            print("8. Status Karyawan")
                            print("9. Password")
                            print("10. Kembali")
                            pilihan = input("Masukkan pilihan (1-10): ").strip()

                            if pilihan == '1':
                                while True:
                                    nama_baru = input("Masukkan Nama Baru Karyawan: ").strip().title()
                                    if len(nama_baru) != 0 and validasi_nama(nama_baru):
                                        while True:
                                            perubahan_konfirmasi = input(f"Apakah Anda yakin ingin mengubah Nama menjadi '{nama_baru}'? (y/n): ").strip().lower()
                                            if perubahan_konfirmasi == 'y': 
                                                karyawan['Nama'] = nama_baru            # Mengganti 'Nama' pada list data_karyawan dengan isi nama_baru
                                                print("\nData Karyawan yang Diperbarui:")
                                                tampilkan_tabel([karyawan])
                                                print("Data karyawan berhasil diperbarui.")
                                                break
                                            elif perubahan_konfirmasi == 'n':
                                                print("Pengubahan Nama dibatalkan.")
                                                break
                                            else:
                                                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                                        if perubahan_konfirmasi == 'y' or perubahan_konfirmasi == 'n':
                                            break
                                    else:
                                        print("Nama tidak boleh kosong dan tidak boleh mengandung angka dan simbol.")
                                break

                            elif pilihan == '2':
                                while True:
                                    gender_baru = input("Masukkan Gender Baru Karyawan (L/P): ").strip().upper()
                                    if validasi_gender(gender_baru):
                                        while True:
                                            perubahan_konfirmasi = input(f"Apakah Anda yakin ingin mengubah Gender menjadi '{gender_baru}'? (y/n): ").strip().lower()
                                            if perubahan_konfirmasi == 'y':
                                                karyawan['Gender'] = gender_baru          # Mengganti 'Gender' pada list data_karyawan dengan isi gender_baru
                                                print("Data karyawan berhasil diperbarui.")
                                                break
                                            elif perubahan_konfirmasi == 'n':
                                                print("Pengubahan Gender dibatalkan.")
                                                break
                                            else:
                                                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                                        if perubahan_konfirmasi == 'y' or perubahan_konfirmasi == 'n':
                                            break
                                    else:
                                        print("Gender tidak valid.")
                                break
                            
                            elif pilihan == '3':
                                while True:
                                    tanggal_lahir_baru = input("Masukkan Tanggal Lahir Baru Karyawan (dd-mm-yyyy): ").strip()
                                    if validasi_tanggal(tanggal_lahir_baru):
                                        while True:
                                            perubahan_konfirmasi = input(f"Apakah Anda yakin ingin mengubah Tanggal Lahir menjadi '{tanggal_lahir_baru}'? (y/n): ").strip().lower()
                                            if perubahan_konfirmasi == 'y':
                                                karyawan['Tanggal Lahir'] = tanggal_lahir_baru          # Mengganti 'Tanggal Lahir' pada list data_karyawan dengan isi tanggal_lahir_baru
                                                print("Data karyawan berhasil diperbarui.")
                                                break
                                            elif perubahan_konfirmasi == 'n':
                                                print("Pengubahan Tanggal Lahir dibatalkan.")
                                                break
                                            else:
                                                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                                        if perubahan_konfirmasi == 'y' or perubahan_konfirmasi == 'n':
                                            break
                                    else:
                                        print("Tanggal tidak valid.")
                                break

                            elif pilihan == '4':
                                while True:
                                    tempat_tinggal_baru = input("Masukkan Tempat Tinggal Baru Karyawan: ").strip().upper()
                                    if 3 < len(tempat_tinggal_baru) != 0:
                                        while True:
                                            perubahan_konfirmasi = input(f"Apakah Anda yakin ingin mengubah Tempat Tinggal menjadi '{tempat_tinggal_baru}'? (y/n): ").strip().lower()
                                            if perubahan_konfirmasi == 'y':
                                                karyawan['Tempat Tinggal'] = tempat_tinggal_baru          # Mengganti 'Tempat Tinggal' pada list data_karyawan dengan isi tempat_tinggal_baru
                                                print("Data karyawan berhasil diperbarui.")
                                                break
                                            elif perubahan_konfirmasi == 'n':
                                                print("Pengubahan Tempat Tinggal dibatalkan.")
                                                break
                                            else:
                                                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                                        if perubahan_konfirmasi == 'y' or perubahan_konfirmasi == 'n':
                                            break
                                    else:
                                        print("Tempat tinggal tidak boleh kosong atau kurang dari 3 karakter.")
                                break
                            elif pilihan == '5':
                                while True:
                                    print("\nDaftar Departemen:")
                                    tampilkan_tabel_departemen()
                                    departemen_baru = input("Masukkan Departemen Baru Karyawan: ").strip().upper()
                                    if validasi_departemen(departemen_baru):
                                        while True:
                                            perubahan_konfirmasi = input(f"Apakah Anda yakin ingin mengubah Departemen menjadi '{departemen_baru}'? (y/n): ").strip().lower()
                                            if perubahan_konfirmasi == 'y':
                                                karyawan['Departemen'] = departemen_baru          # Mengganti 'Departemen' pada list data_karyawan dengan isi departemen_baru
                                                print("Data karyawan berhasil diperbarui.")
                                                break
                                            elif perubahan_konfirmasi == 'n':
                                                print("Pengubahan Departemen dibatalkan.")
                                                break
                                            else:
                                                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                                        if perubahan_konfirmasi == 'y' or perubahan_konfirmasi == 'n':
                                            break
                                    else:
                                        print("Departemen tidak valid.")
                                break
                            elif pilihan == '6':
                                while True:
                                    print("\nDaftar Jabatan:")
                                    tampilkan_tabel_jabatan()
                                    jabatan_baru = input("Masukkan Jabatan Baru Karyawan: ").strip().upper()
                                    if validasi_jabatan(jabatan_baru):
                                        while True:
                                            perubahan_konfirmasi = input(f"Apakah Anda yakin ingin mengubah Jabatan menjadi '{jabatan_baru}'? (y/n): ").strip().lower()
                                            if perubahan_konfirmasi == 'y':
                                                karyawan['Jabatan'] = jabatan_baru          # Mengganti 'Jabatan' pada list data_karyawan dengan isi jabatan_baru
                                                print("Data karyawan berhasil diperbarui.")
                                                break
                                            elif perubahan_konfirmasi == 'n':
                                                print("Pengubahan Jabatan dibatalkan.")
                                                break
                                            else:
                                                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                                        if perubahan_konfirmasi == 'y' or perubahan_konfirmasi == 'n':
                                            break
                                    else:
                                        print("Jabatan tidak valid.")
                                break
                            elif pilihan == '7':
                                while True:
                                    telepon_baru = input("Masukkan Nomor Handphone Baru Karyawan (Tanpa spasi atau tanda hubung): ").strip()
                                    if 10 <= len(telepon_baru) <= 14 and telepon_baru.isdigit():
                                        while True: 
                                            perubahan_konfirmasi = input(f"Apakah Anda yakin ingin mengubah Nomor Handphone menjadi '{telepon_baru}'? (y/n): ").strip().lower()
                                            if perubahan_konfirmasi == 'y':
                                                karyawan['Telepon'] = format_telepon(telepon_baru)              # Mengganti 'Telepon' pada list data_karyawan isi dari variabel telepon_baru
                                                print("Data karyawan berhasil diperbarui.")
                                                break
                                            elif perubahan_konfirmasi == 'n':
                                                print("Pengubahan Nomor Handphone dibatalkan.")
                                                break
                                            else:
                                                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                                        if perubahan_konfirmasi == 'y' or perubahan_konfirmasi == 'n':
                                            break
                                    else:
                                        print("\nMasukkan Nomor Handphone yang valid (Panjang minimal 10 dan maksimal 14 digit, tanpa spasi atau tanda hubung).")
                                break
                            elif pilihan == '8':
                                while True:
                                    status_baru = input("Masukkan Status Baru Karyawan (Aktif/Tidak Aktif): ").strip().title()
                                    if validasi_status(status_baru):
                                        while True:
                                            perubahan_konfirmasi = input(f"Apakah Anda yakin ingin mengubah Status menjadi '{status_baru}'? (y/n): ").strip().lower()
                                            if perubahan_konfirmasi == 'y':
                                                karyawan['Status'] = status_baru              # Mengganti 'Status' pada list data_karyawan dengan isi status_baru
                                                print("Data karyawan berhasil diperbarui.")
                                                break
                                            elif perubahan_konfirmasi == 'n':
                                                print("Pengubahan Status dibatalkan.")
                                                break
                                            else:
                                                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                                        if perubahan_konfirmasi == 'y' or perubahan_konfirmasi == 'n':
                                            break
                                    else:
                                        print("Status tidak valid.")
                                break
                            elif pilihan == '9':
                                while True:
                                    password_baru = input("Masukkan Password Baru Karyawan: ").strip()
                                    if len(password_baru) >= 4:
                                        while True:
                                            perubahan_konfirmasi = input(f"Apakah Anda yakin ingin mengubah Password menjadi '{password_baru}'? (y/n): ").strip().lower()
                                            if perubahan_konfirmasi == 'y':
                                                username = get_username_by_id(karyawan["ID"])
                                                users[username]['password'] = password_baru  # Mengganti 'password' pada data users dengan isi password_baru
                                                print("Password berhasil diperbarui.")
                                                break
                                            elif perubahan_konfirmasi == 'n':
                                                print("Pengubahan Password dibatalkan.")
                                                break
                                            else:
                                                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                                        if perubahan_konfirmasi == 'y' or perubahan_konfirmasi == 'n':
                                            break
                                    else:
                                        print("Password tidak boleh kosong atau kurang dari 4 karakter.")
                                break
                            elif pilihan == '10':
                                break
                        
                            else:
                                print("Pilihan tidak valid.")
                        # Kembali ke menu sebelumnya setelah perubahan data
                        break
                    elif konfirmasi == 'n':
                        print("Pengubahan data dibatalkan.")
                        break
                    else:
                        print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            elif pilihan == '2':
                return 
            
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

def hapus_data_karyawan():
    while True:
        print("\n+==========================================+")
        print("|             HAPUS DATA KARYAWAN          |")
        print("+==========================================+")
        print("| 1. Hapus Akun Karyawan                   |")
        print("| 2. Hapus Karyawan Berdasarkan Departemen |")
        print("| 3. Kembali ke Menu Utama                 |")
        print("+==========================================+")
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == '1':
            id_karyawan = input("Masukkan ID Karyawan yang ingin dihapus: ").strip().upper()
            if id_karyawan == "":               # Cek apakah inputan kosong
                print("ID tidak boleh kosong.")
                continue
            
            karyawan_to_delete = ""
            
            # Mencari karyawan yang ingin dihapus berdasarkan ID pada list data_karyawan
            for karyawan in data_karyawan:
                if karyawan["ID"] == id_karyawan:
                    karyawan_to_delete = karyawan
                    break
            
            if karyawan_to_delete == "":        # Apabila karyawan yang ingin di hapus tidak ditemukan
                print("Data tidak ditemukan")
            else:                               # Apabila karyawan yang ingin di hapus ditemukan
                # Tampilkan data karyawan yang akan dihapus
                print("\nData Karyawan:")
                tampilkan_tabel([karyawan_to_delete])
                
                # Konfirmasi penghapusan
                while True:
                    konfirmasi = input("Apakah Anda yakin ingin menghapus data karyawan ini? (y/n): ").strip().lower()
                    if konfirmasi == 'y':
                        # Hapus data karyawan menggunakan remnove
                        data_karyawan.remove(karyawan_to_delete)
                        
                        # Hapus akun karyawan menggunakan pop
                        username = cari_username_by_id(id_karyawan)  # Mencari username berdasarkan id pada dictionary users
                        users.pop(username)                          # Menghapus username pada dictionary users menggunakan pop
                        
                        print("Data karyawan dan akun pengguna berhasil dihapus.")
                        break
                    elif konfirmasi == 'n':
                        print("Penghapusan data karyawan dibatalkan.")
                        break
                    else:
                        print("Pilihan tidak valid. Silakan pilih 'y' atau 'n'.")
        
        elif pilihan == '2':
            print("\nBerikut merupakan daftar departemen yang tersedia:")
            tampilkan_tabel_departemen()
            departemen = input("Masukkan nama departemen: ").strip().upper()
            karyawan_to_delete = [karyawan for karyawan in data_karyawan if karyawan["Departemen"] == departemen]  # Mencari kayawan yang berdepartemen sama dengan inputan, (pada list data_karyawan)

            if len(karyawan_to_delete) == 0:
                print("Tidak ada karyawan dalam departemen ini.")
            else:
                # Tampilkan data karyawan yang akan dihapus sesuai dengan data yang didapatkan dari karyawan_to_delete
                print("\nData Karyawan:")
                tampilkan_tabel(karyawan_to_delete)
                
                # Konfirmasi penghapusan
                while True:
                    konfirmasi = input(f"Apakah Anda yakin ingin menghapus data seluruh karyawan dalam departemen {departemen}? (y/n): ").strip().lower()
                    if konfirmasi == 'y':                               
                        for karyawan in karyawan_to_delete:
                            data_karyawan.remove(karyawan)                  # Menghapus seluruh data karyawan yang masuk ke karyawan_to_delete
                            username = cari_username_by_id(karyawan["ID"])  # Mencari username berdasarkan ID 
                            users.pop(username)                             # Menghapus username pada dictionary users menggunakan pop
                        print("Data karyawan dan akun pengguna berhasil dihapus.")
                        break
                    elif konfirmasi == 'n':
                        print("Penghapusan data karyawan dibatalkan.")
                        break
                    else:
                        print("Pilihan tidak valid. Silakan pilih 'y' atau 'n'.")

        elif pilihan == '3':
            return
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Fungsi menu utama 
def main():
    while True:
        user = login()
        if user == "":
            break
        if user["role"] == "admin":                 # Apabila user adalah admin
            while True:
                pilihan = tampilkan_menu_admin()
                if pilihan == '1':
                    baca_data_karyawan()
                elif pilihan == '2':
                    tambah_akun_karyawan()
                elif pilihan == '3':
                    perbarui_data_karyawan(user)
                elif pilihan == '4':
                    hapus_data_karyawan()
                elif pilihan == '5':
                    while True:
                        konfirmasi_logout = input("Apakah Anda yakin ingin logout? (y/n): ").strip().lower()
                        if konfirmasi_logout == 'y':
                            print("Logout berhasil.")
                            break
                        elif konfirmasi_logout == 'n':
                            break
                        else:
                            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                    if konfirmasi_logout == 'y':
                        break
                elif pilihan == '6':
                    while True:
                        konfirmasi_keluar = input("Apakah Anda yakin ingin keluar dari aplikasi? (y/n): ").strip().lower()
                        if konfirmasi_keluar == 'y':
                            print("Terima kasih! Sampai jumpa! (Keluar dari aplikasi).")
                            return
                        elif konfirmasi_keluar == 'n':
                            break
                        else:
                            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                else:
                    print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
        elif user["role"] == "karyawan":             # Apabila user adalah karyawan
            while True:
                pilihan = tampilkan_menu_karyawan()
                if pilihan == '1':
                    karyawan = cari_karyawan_by_id(user["id"])
                    tampilkan_tabel([karyawan])
                elif pilihan == '2':
                    perbarui_data_karyawan(user)
                elif pilihan == '3':
                    while True:
                        konfirmasi_logout = input("Apakah Anda yakin ingin logout? (y/n): ").strip().lower()
                        if konfirmasi_logout == 'y':
                            print("Logout berhasil.")
                            break
                        elif konfirmasi_logout == 'n':
                            break
                        else:
                            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                    if konfirmasi_logout == 'y':
                        break
                elif pilihan == '4':
                    while True:
                        konfirmasi_keluar = input("Apakah Anda yakin ingin keluar dari aplikasi? (y/n): ").strip().lower()
                        if konfirmasi_keluar == 'y':
                            print("Terima kasih! Sampai jumpa! (Keluar dari aplikasi).")
                            return # Keluar dari aplikasi
                        elif konfirmasi_keluar == 'n':
                            break
                        else:
                            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                else:
                    print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")


if __name__ == '__main__': #Berfungsi agar program tidak berjalan secara langsung apabila dijalankan dalam bentuk skrip
    main()
