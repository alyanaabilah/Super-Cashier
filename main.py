from function import Transaction


def header():
    '''Membuat Fungsi Header'''
    print(f"{'-'*40:^40}")
    print(f"{'SELAMAT DATANG DI PACSTORE':^40}")
    print(f"{'SILAHKAN BERBELANJA SESUAI KEBUTUHAN ANDA':^40}")
    print(f"{'-'*40:^40}")


while True:
    header()
    pilihan=int(input("1.Tambah Produk\n2.Check Produk\n3.Update Nama Barang\n4.Update Jumlah Barang\n5.Update Harga Barang (satuan)\n6.Cek Harga\n7.Hapus Item\n8.Reset Belanjaan\n9.Keluar\nPilih Menu Yang diinginkan: "))
    if pilihan == 1:
       '''Input Data Belanja Dari User'''
       print(f"{'-'*40:^40}")
       print(f"{'TAMBAH BELANJAAN':^40}")
       print(f"{'-'*40:^40}")
       total = 0
       choice = Transaction()
       while True:
        try:
         name = input("Nama Produk: ")
         if name.isalpha() and (len(name)!=0):
            amount = int(input("Jumlah Barang: "))
            priceItem = int(input("Harga: Rp. "))
            total = amount*priceItem
            choice.add_item(name, amount, priceItem, total)
         else:
            print("Masukkan nama produk")
         done = input("Apakah mau menambah barang lagi?(y/n): ")
         if done == 'n' or done == 'N':
            print("Produk Berhasil Ditambahkan ke Keranjang Anda")
            choice.check_item()
            break
        except:
             print("Masukkan Data Yang Benar")
    elif pilihan == 2:
        '''Pilihan Untuk Cek Barang Yang Sudah Dibeli'''
        print(f"{'-'*40:^40}")
        print(f"{'CEK KERANJANG':^40}")
        print(f"{'-'*40:^40}")
        try:
         choice.check_item()
        except:
           NameError = print("Silahkan belanja dulu kak!")
    elif pilihan == 3:
       '''Pilihan Untuk Update Nama Item'''
       print(f"{'-'*40:^40}")
       print(f"{'UPDATE NAMA ITEM':^40}")
       print(f"{'-'*40:^40}")
       try:
         old_name = input("Nama Produk Lama: ")
         new_name = input("Update Nama Produk: ")
         n_update = choice.update_name(old_name, new_name)
         print(f"Data Nama Barang Anda Telah Diubah! {choice.check_item()}")
       except:
          TypeError = print(f"Ulangi pemesanan, nama produk tidak ada")
    elif pilihan == 4:
       '''Pilihan Untuk Update Jumlah Item'''
       print(f"{'-'*40:^40}")
       print(f"{'UPDATE JUMLAH ITEM':^40}")
       print(f"{'-'*40:^40}")
       name = input("Nama Produk: ")
       new_amount = input("Update Jumlah Produk: ")
       n_update = choice.update_amount(name, new_amount)
       print(f"Data Jumlah Barang Anda Telah Diubah! {choice.check_item()}")
    elif pilihan == 5:
       '''Pilihan Update Harga Produk'''
       print(f"{'-'*40:^40}")
       print(f"{'UPDATE HARGA PRODUK':^40}")
       print(f"{'-'*40:^40}")
       name = input("Nama Produk: ")
       new_price = input("Update Harga Produk (satuan): Rp. ")
       n_update = choice.update_priceItem(name, new_price)
       print(f"Data Harga Barang Anda Telah Diubah! {choice.check_item()}")
    elif pilihan == 6:
       '''Pilihan Untuk Melihat Total Belanja User'''
       print(f"{'-'*40:^40}")
       print(f"{'TOTAL BELANJA':^40}")
       print(f"{'-'*40:^40}")
       final_price = choice.total_price(total)
       print(f"Total belanja anda: Rp.{final_price}")
       choice.check_item()
    elif pilihan == 7:
        '''Pilihan Menghapus Data Produk'''
        print(f"{'-'*40:^40}")
        print(f"{'MENGHAPUS DATA ITEM':^40}")
        print(f"{'-'*40:^40}")
        name = input("Nama Produk: ")
        is_sure = input("Apakah anda yakin ingin menghapus produk ini?(y/n): ")
        if is_sure == 'y' or is_sure == 'Y':
          choice.delete_item(name)
          choice.check_item()
          print(f"Produk Berhasil Di Hapus!")
    elif pilihan == 8:
       '''Pilihan Menghapus Semua Data Produk'''
       print(f"{'-'*40:^40}")
       print(f"{'MENGHAPUS SEMUA BELANJAAN':^40}")
       print(f"{'-'*40:^40}")
       is_sure_ = input("Apakah anda yakin ingin menghapus semua belanjaan anda?(y/n): ")
       if is_sure_ == 'y' or is_sure_ == 'Y':
          choice.reset_item()
          choice.check_item()
          print(f"Produk Berhasil Di Hapus!")
    elif pilihan == 9:
       break
        

    is_done = input("Apakah Anda Sudah Selesai?(y/n): ")
    if is_done == 'y' or is_done == 'Y':
        break


print(f"Terima kasih sudah berbelanja di tempat kami")