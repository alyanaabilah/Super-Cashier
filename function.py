import pandas as pd

class Transaction():
    def __init__(self):
        self.transaksi = []
        self.produk = []
    
    def add_item(self, name, amount, priceItem, total):
        '''Fungsi tambah barang'''
        self.transaksi.append([name, amount, priceItem, total])
    
    def check_item(self):
        '''Fungsi cek data barang yang dibeli'''
        if(len(self.transaksi)==0):
            print(f"Tidak ada barang di keranjang")
        else:
            data = pd.DataFrame((self.transaksi))
            data.columns = ['Nama', 'Qty', 'Harga Item', 'Total']
            print(data.to_markdown())

    def update_name(self, name, new_name):
        '''Fungsi update nama barang'''
        self.transaksi[self.return_index(name)][0] = new_name

    def update_amount(self, name, new_amount):
        '''Fungsi update jumlah barang'''
        try:
            self.transaksi[self.return_index(name)][1]= new_amount
        except:
            print("Produk Tidak Ditemukan")

    def update_priceItem(self, name, new_priceItem):
        '''Fungsi update harga barang (satuan)'''
        try:
            self.transaksi[self.return_index(name)][2] = new_priceItem
        except:
            print("Produk Tidak Ditemukan")

    def delete_item(self, name):
        '''Fungsi menghapus item berdasarkan nama'''
        try:
            self.transaksi.pop(self.return_index(name))
        except:
            print("Produk Tidak Ditemukan")
    
    def reset_item(self):
        '''Fungsi mereset semua item'''
        self.transaksi.clear()

    def return_index(self, name):
        '''Fungsi untuk mengembalikan index'''
        for i in range(len(name)):
            if self.transaksi[i][0] == name:
                return i
            

    def total_price(self, total):
        '''Fungsi menghitung total belanja'''
        discount_1 = 0.05
        discount_2 = 0.08
        discount_3 = 0.10
        if total >= 200_000 and total <= 300_000:
            price_1 = total*discount_1
            final_price_1 = total - price_1
            return final_price_1
        elif total >= 300_000 and total <= 500_000:
            price_2 = total*discount_2
            final_price_2 = total - price_2
            return final_price_2
        elif total >= 500_000:
            price_3 = total*discount_3
            final_price_3 = total - price_3
            return final_price_3
        elif total < 200_000:
            final_price_4 = total
            return final_price_4
        


beli = Transaction()
beli.add_item('Minyak', '300', 'Rp.1000', '300_000')
# beli.add_item('Marie', '1', 'Rp.15000')
total = 300000
harga = beli.total_price(total)
print(harga)

# beli.update_name('Minyak','Cangkir')
# print(beli.check_item())