from data import database, list_add_menu, list_contact_menu, list_delete_menu, list_replace_menu, list_main_menu

def menu_utama():  
    while True:
        print_menu(list_main_menu)
        perintah = int(input('Silahkan Pilih Menu [1 - 5]: '))
        if 0 < perintah < 5:
            return submenu(perintah)
        elif perintah == 5:
            break
        else:
            print('\n\nxxxxx Pilihan Anda Tidak Ditemukan Dalam Program xxxxx\n\n')

def print_menu(menu):
    for key, val in menu.items():
        if key == "0":
            print(val)
        else:
            print(f"{key}. {val}")

def submenu(value):
    if value == 1:
        submenu_contact()  
    elif value == 2:
        submenu_add()
    elif value == 3:
        submenu_replace()
    elif value == 4:
        submenu_delete()

def submenu_contact():
    while True:
        print_menu(list_contact_menu)
        perintahh = int(input('Silahkan Pilih Menu [1 - 3]: '))
        # Code untuk menjalankan "Tampilkan Kontak Seluruh Petugas"
        if perintahh == 1:
            if len(database) > 0:
                for i, j in enumerate(database):
                    print(i+1, f". ID: {j['ID']}, nama: {j['nama']}, lantai: {j['lantai']}, jabatan: {j['jabatan']}, no tlpn: {j['telepon']}")
            else:
                print('\nooooo Tidak Ada Data Kontak Petugas ooooo')
        # Code untuk menjalankan "Tampilkan Kontak Petugas di lantai tertentu"
        elif perintahh == 2:
            if len(database) != 0:
                input_id = int(input('Masukkan Nomor Lantai: '))
                for i, j in enumerate(database):
                    if j['lantai'] == input_id:
                        print(f'''Berikut Adalah Kontak Petugas Di Lantai {input_id}: ID: {j['ID']}, nama: {j['nama']}, lantai: {j['lantai']}, jabatan: {j['jabatan']}, no tlpn: {j['telepon']}''')
                    else:
                        print(f'\nooooo Tidak Ada Data Kontak Petugas Di Lantai {input_id} atau Lantai {input_id} Tidak Ada ooooo')
                        break
            else:
                print('\nooooo Tidak Ada Data Kontak Petugas ooooo')
        elif perintahh == 3:
            return menu_utama()

def submenu_add():
    while True:
        print_menu(list_add_menu)
        perintah = input('Silahkan Pilih Menu [1 - 2]: ')
        # Code untuk menjalankan "Tambah Data Petugas"
        if perintah == '1':
            input_id = input('Masukkan ID (*harus 4 digit, 2 digit pertama menunjukkan lantai): ')
            jumlah = 0
            for i in database:
                if i['ID'] == input_id:
                    jumlah += 1
            if jumlah == 0:
                database.append({})
                for i in database:
                    if len(i) == 0:
                        i['ID'] = input_id
                        i['nama'] = input('Masukkan Nama: ')
                        i['jabatan'] = input('Masukkan Jabatan: ')
                        i['telepon'] = input('Masukkan Nomor Telepon: ')
                        if input_id[0] == '0':
                            i['lantai'] = int(input_id[1])
                        else:
                            i['lantai'] = int(input_id[:2])
                while True:
                    konfirmasi_simpan = input('Simpan Data [Y/N]: ')
                    if konfirmasi_simpan == 'N':
                        print('ooooo Data Tidak di Simpan ooooo')
                        database.pop()
                        break
                    elif konfirmasi_simpan == 'Y':
                        print('+++++ Data Tersimpan +++++')
                        break
    
            else:
                print('===== ID Sudah Ada Dalam Database =====')
        # Code untuk menjalankan "Kembali Ke Menu Utama"
        elif perintah == '2':
            return menu_utama()

def submenu_replace():
    while True:
        print_menu(list_replace_menu)
        perintah = input('Silahkan Pilih Menu [1 - 2]: ')
        # Code untuk menjalankan "Ubah Data Petugas"
        if perintah == '1':
            input_id = input('Masukkan ID: ')
            jumlah = 0
            for j in database:
                if j['ID'] == input_id:
                    jumlah += 1
                    print(f"ID: {j['ID']}, nama: {j['nama']}, jabatan: {j['jabatan']}, nomor telepon: {j['telepon']}")
                    while True:
                        konfirmasi_rubah_awal = input('Rubah Data [Y / N]: ')
                        if konfirmasi_rubah_awal == 'Y':
                            while True:
                                field_rubah = input('Masukkan Field Yang Akan Dirubah (nama, jabatan, atau telepon): ')
                                if field_rubah == 'nama' or field_rubah == 'jabatan' or field_rubah == 'telepon':
                                    perubahan = input(f'Masukkan {field_rubah} Baru: ')
                                    while True:
                                        konfirmasi_rubah = input('Rubah Data [Y / N]: ')
                                        if konfirmasi_rubah == 'Y':
                                            j[f'{field_rubah}'] = perubahan
                                            break
                                        elif konfirmasi_rubah == 'N':
                                            break
                                    break
                                else:
                                    print('Field Yang Anda Masukkan Salah')
                            break
                        elif konfirmasi_rubah_awal == 'N':
                            break
            if jumlah == 0:
                print(f'xxxxx Data Untuk ID {input_id} Tidak Ada xxxxx')
        # Code untuk menjalankan "Kembali Ke Menu Utama"
        elif perintah == '2':
            return menu_utama()

def submenu_delete():
    while True:
        print_menu(list_delete_menu)
        perintah = input('Silahkan Pilih Menu [1 - 2]: ')
        # Code untuk menjalankan "Hapus Data Kontak Petugas"
        if perintah == '1':
            input_id = input('Masukkan ID Yang Ingin Dihapus: ')
            if len(database) > 0:
                jumlah = 0
                for j in database:
                    if j['ID'] == input_id:
                        jumlah += 1
                        while True:
                            konfirmasi_hapus = input('Hapus Data [Y / N]: ')
                            if konfirmasi_hapus == 'Y':
                                database.remove(j)
                                print('xxxxx Data Berhasil Terhapus xxxxx')
                                break
                            elif konfirmasi_hapus == 'N':
                                print('===== Data Tidak Jadi Dihapus =====')
                                break
                if jumlah == 0:
                    print(f'xxxxx Data untuk ID {input_id} Tidak Ditemukan Di Database xxxxx')
            else:
                print(f'xxxxx Data untuk ID {input_id} Tidak Ditemukan Di Database xxxxx')
                    
        # Code untuk menjalankan "Kembali Ke Menu Utama"
        elif perintah == '2':
            return menu_utama()

menu_utama()