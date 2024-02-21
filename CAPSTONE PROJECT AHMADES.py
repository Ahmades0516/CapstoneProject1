
from colorama import Fore, Back, Style # UNTUK MEMBUAT TULISAN BERWARNA
#data disimpan dalam collection data Dictionary
listPasien = {
   1: {'nama': 'Juwardi ali', 'Jenis Kelamin':'L','ID pasien': 201, 'Alamat': 'Jakarta', 'umur': 35,'riwayat Penyakit': 'Asma'},

   2: {'nama': 'Ismadia', 'Jenis Kelamin':'P','ID pasien': 202,'Alamat': 'Medan','umur': 29, 'riwayat Penyakit': 'Demam Berdarah'},

   3: {'nama': 'Kurniawan','Jenis Kelamin':'L','ID pasien': 203,'Alamat': 'Bandung','umur': 40,'riwayat Penyakit': 'Asma'},

   4: {'nama': 'Sri Ningsih','Jenis Kelamin':'p','ID pasien': 204,'Alamat': 'Bogor','umur': 50,'riwayat Penyakit': 'diabetes'},

   5:{ 'nama': 'Agus Heru','Jenis Kelamin':'L','ID pasien': 205,'Alamat': 'Semarang','umur': 35,'riwayat Penyakit': 'diabetes'},

   6: {'nama': 'Suharti','Jenis Kelamin':'P','ID pasien': 206,'Alamat': 'Jakarta','umur': 55,'riwayat Penyakit': 'Hipertensi'},

   7: {'nama': 'Hendrawan','Jenis Kelamin':'L','ID pasien': 207,'Alamat': 'Depok','umur': 28,'riwayat Penyakit': 'Asam Lambung'},

   8: {'nama': 'Ali Fikri','Jenis Kelamin':'L','ID pasien': 208,'Alamat': 'Tangerang','umur': 40,'riwayat Penyakit': 'Hipertensi'},

   9: {'nama': 'M. Rizki','Jenis Kelamin':'L','ID pasien': 209,'Alamat': 'Bandung','umur': 23,'riwayat Penyakit': 'Demam Berdarah'},
}

codeAdmin = 'AB021' #CODE ADMIN UNTUK PENGAMANAN
cart = [] # tempat penyimpanan list appointmen yang akan dilist nantinya


def menampilkanDaftarPasien() :
        print('\nDaftar Pasien\n')
        print(Fore.GREEN +'Index\t| Nama  \t| Jenis Kelamin \t| ID pasien  \t| Alamat  \t| umur     | riwayat penyakit ')
        for j in listPasien.keys() :
            print(Fore.GREEN + '{}\t| {}  \t| {} \t \t \t|{}  \t\t| {}  \t|{} tahun  | {} '.format(j,listPasien[j]['nama'],listPasien[j]['Jenis Kelamin'],listPasien[j]['ID pasien'], listPasien[j]['Alamat'],listPasien[j]['umur'],listPasien[j]['riwayat Penyakit']))

#Untuk menampilkan Fungsi Read dengan menampilkan data Pasien
def tampilanPasien():
     while True:
          print( '\n ==========DATA PASIEN RUMAH SAKIT BAHAGIA=========')
          inputanKU = int(input('1. Menampilkan Semua Data \n2. Menampilkan Data Tertentu \n3. Kembali Ke Menu Utama \n\n Silahkan Masukkan Pilihan Anda : '))
          if inputanKU ==1:
               if len(listPasien) == 0:
                    print(Fore.RED + "Tidak ada Data Pasien")
                    break
               else :
                    menampilkanDaftarPasien()
          elif inputanKU == 2:
               kategori1 = int(input('\n1. Menampilkan Data Pasien Melalui Nama \n2. Menampilkan Data Pasien Melalui ID Pasien \n3. Kembali Ke Menu Utama \n\n Silahkan Masukkan Pilihan Anda : '))
               if kategori1 == 1:
                    nm = input("Masukkan Nama : ").capitalize()
                    print(f'Data Pasien Dengan Nama : {nm}')  
                    for j in listPasien.keys():
                         if nm == listPasien[j]['nama'] :
                               print(Fore.GREEN + '\n{}\t| {}  \t| {} \t \t \t|{}  \t\t| {}  \t|{} tahun  | {} '.format(j,listPasien[j]['nama'],listPasien[j]['Jenis Kelamin'],listPasien[j]['ID pasien'], listPasien[j]['Alamat'],listPasien[j]['umur'],listPasien[j]['riwayat Penyakit']))
                               break
                    else:
                          print("\n=====Tidak ada Data Pasien=====")  
                
               elif kategori1 == 2:
                    nCd = int(input('Masukkan ID Pasien: '))
                    print(f"Data Pasien Dengan ID Pasien : {nCd}")  
                    for j in listPasien.keys():
                         if nCd == listPasien[j]['ID pasien'] :
                               print(Fore.GREEN + '\n{}\t| {}  \t| {} \t \t \t|{}  \t\t| {}  \t|{} tahun  | {} '.format(j,listPasien[j]['nama'],listPasien[j]['Jenis Kelamin'],listPasien[j]['ID pasien'], listPasien[j]['Alamat'],listPasien[j]['umur'],listPasien[j]['riwayat Penyakit']))
                               break
                    else:
                     print("\n=====Tidak ada Data Pasien=====") 

               elif kategori1 == 3:
                    break
               else :
                 print("\nPilihan yang anda pilih tidak tersedia. Silahkan dicoba lagi.") 
          elif inputanKU == 3 :
               break
          else :
               print("\nPilihan yang anda pilih tidak tersedia. Silahkan dicoba lagi.")

# Tampilan Menu Mengubah Data (Edit Data)                
def updatePasien():
     while True:
        print('\n \t=====Mengupdate Data Pasien====\n')
        inputanKU = int(input('\n1. Mengganti Data Pasien\n2. Kembali Ke Manu Utama \n Silahkan Masukkan Pilihan Anda :'))
        if inputanKU == 1: # akan memanggil def menampilkan daftar pasien yang telah didefinisikan sebelumnya
             menampilkanDaftarPasien()
             idPasien = int(input('Masukkan ID Pasien : '))
             for j in listPasien.keys():
               if idPasien == listPasien[j]['ID pasien']:
                        print(('\n{}\t| {}  \t| {} \t \t \t|{}  \t\t| {}  \t|{} tahun  | {} '.format(j,listPasien[j]['nama'],listPasien[j]['Jenis Kelamin'],listPasien[j]['ID pasien'], listPasien[j]['Alamat'],listPasien[j]['umur'],listPasien[j]['riwayat Penyakit'])))
                        while True:
                             
                             inputan2 = (int(input('1. Mengganti Nama Pasien \n2. Mengganti Jenis Kelamin Pasien \n3. Mengganti Alamat Pasien \n4. Mengganti Umur Pasien \n5. Mengganti Riwayat Penyakit \n6. Kembali Ke Manu sebelumnya \n Silahkan Masukkan Pilihan Anda :')))
                             if inputan2 == 1:
                                  while True:
                                    check = input('\nApakah Anda ingin Lanjut Mengganti Data Pasien (Ya/Tidak) : ').lower()
                                    if check == 'ya':
                                        dataBaru = input('Masukkan Nama Baru : ') # User input nama data yang akan diganti
                                        while True:
                                             Check2 = input('\nApakah Data Akan Diganti? (Ya/Tidak) : ').lower()
                                             if Check2 == 'ya' : # memastikan tindakan perubahan
                                                  listPasien[j]['nama'] = dataBaru
                                                  print(Fore.BLUE +'\n =====Data Telah Diganti=====')
                                                  break
                                             else :
                                                  print('\n Data Tidak Diganti') #apabila jawaban selain ya maka data tidak akan diganti
                                                  break
                                        break
                                    else:
                                        print('\n Data Tidak Terganti\n')
                                        break
                             
                             elif inputan2 == 2 :
                                 while True:
                                   check = input('\nApakah Anda ingin Lanjut Mengganti Data Pasien (Ya/Tidak) : ').lower() #apabila input yang dimasukkan huruf kecil semuanya akan tetap terbaca pada program
                                   if check == 'ya':
                                        #memasukkan data baru yang nantinya akan disimpan sebagai data pasien
                                        dataBaru = input('Masukkan Jenis Kelamin Baru (L/P) : ')
                                        while True:
                                             Check2 = input('\nApakah Data Akan Diganti? (Ya/Tidak) : ').lower()
                                             if Check2 == 'ya' :
                                                  listPasien[j]['Jenis Kelamin'] = dataBaru
                                                  print(Fore.BLUE +'\n =====Data Telah Diganti=====')
                                                  break
                                             elif Check2 == 'TIDAK':
                                                  print('Data Tidak Diganti')
                                                  break
                                        break
                                   elif check == 'tidak':
                                        print('Data Tidak Terganti')
                                        break
                             elif inputan2 == 3:
                                  while True:
                                   check = input('Apakah Anda ingin Lanjut Mengganti Data Pasien (Ya/Tidak) : ').lower()
                                   if check == 'ya':
                                        dataBaru = input('Masukkan Alamat : ')
                                        while True:
                                             Check2 = input('Apakah Data Akan Diganti? (Ya/Tidak) : ').lower()
                                             if Check2 == 'ya' :
                                                  listPasien[j]['Alamat'] = dataBaru
                                                  print(Fore.BLUE +'\n =====Data Telah Diganti=====')
                                                  break
                                             elif Check2 == 'tidak':
                                                  print('Data Tidak Diganti')
                                                  break
                                        break
                                   elif check == 'tidak':
                                        print('Data Tidak Terganti')
                                        break
                             elif inputan2 == 4:
                                  while True:
                                   check = input('Apakah Anda ingin Lanjut Mengganti Data Pasien (Ya/Tidak) : ').lower()
                                   if check == 'ya':
                                        dataBaru = int(input('Masukkan Umur Pasien : '))
                                        while True:
                                             Check2 = input('Apakah Data Akan Diganti? (Ya/Tidak) : ').lower()
                                             if Check2 == 'ya' :
                                                  listPasien[j]['umur'] = dataBaru
                                                  print(Fore.BLUE +'\n =====Data Telah Diganti=====')
                                                  break
                                             elif Check2 == 'tidak':
                                                  print('Data Tidak Diganti')
                                                  break
                                        
                                        break
                                   elif check == 'tidak':
                                        print('Data Tidak Terganti')
                                        break
                             elif inputan2 == 5:
                                  while True:
                                   check = input('Apakah Anda ingin Lanjut Mengganti Data Pasien (Ya/Tidak) : ').lower()
                                   if check == 'ya':
                                        dataBaru = input('Masukkan Riwayat Penyakit Baru : ')
                                        while True:
                                             Check2 = input('Apakah Data Akan Diganti? (Ya/Tidak) : ').lower()
                                             if Check2 == 'ya' :
                                                  listPasien[j]['riwayat Penaykit'] = dataBaru
                                                  print(Fore.BLUE + '\n =====Data Telah Diganti=====')
                                                  break
                                             elif Check2 == 'tidak':
                                                  print('Data Tidak Diganti')
                                                  break
                                        
                                        break
                                   else:
                                        print('\nData Tidak Terganti\n')
                                        break
                             elif inputan2 == 6:
                                  break
                             else :
                                  print('\nPilihan Tidak Tersedia\n')
                                  
                                  
                        break
             else:
                print("\nData Tidak Ditemukan\n")

        elif inputanKU == 2:
             break
        else:
             print('\nPilihan yang anda masukkan tidak tersedia\n')
                  
# Tampil Menu Menambahkan Data (Tambah Data)
def menambahPasien():
       while True:
          inputan_3 = int(input('''
          Menambahkan Data Pasien Rumah Sakit Bahagia
          1. Tambah Data Pasien
          2. Kembali ke Menu Sebelumnya

          Masukkan Input : ''')) 
          if inputan_3 == 1 :
              newnama=str(input('\nNama Pasien: '))
              newJenisKelamin=str(input('Jenis Kelamin (L/P) : '))
              newIDpasien=int(input('ID Pasien : '))
              if newIDpasien in [data['ID pasien'] for data in listPasien.values()]: #apabila ID pasien telah ada maka akan diminta memasukkan ID pasien kembali
                print('\nID PASIEN TELAH ADA, SILAHKAN MASUKKAN ID LAIN\n')
              else:
               newAlamat=str(input('Alamat : '))
               newUmur=int(input('umur : '))
               newRiwayatPenyakit=str(input('Riwayat Penyakit : '))
               newPasienId= maxPasienID +1
               listPasien[newPasienId]={'nama' : newnama, 'Jenis Kelamin' : newJenisKelamin, 'ID pasien' : newIDpasien, 'Alamat' : newAlamat, 'umur' : newUmur, 'riwayat Penyakit' :newRiwayatPenyakit }
               print(Fore.BLUE + '\n DATA PASIEN TELAH DITAMBAHKAN\n')
          elif inputan_3 == 2 :
               break
          else:
               print('\nPilihan yang anda masukkan tidak tersedia\n')
                 
                    
                
 #Fitur Menu untuk menghapus Data            
def menghapusPasien() :
        while True:
               inputan = int(input('''
          Menghapus Data Pasien
          1. Hapus Data
          2. Kembali ke Menu Utama

          Input Menu Option : '''))
               if inputan == 1:
                    menampilkanDaftarPasien()     
                    print('\nPilih no index pasien yang akan di hapus\n') #Data yang dihapus berdasarkan nomor indexnya
                    delPasien = int(input('No. Pilihan : '))
                    if delPasien in listPasien :
                         del listPasien[delPasien]
                         print(Fore.BLUE + '\n DATA TELAH BERHASIL DIHAPUS')
                    else :
                         print('Pilihan tidak tersedia\n')
                    menampilkanDaftarPasien() #check
               elif inputan == 2 :
                    break
               else:
                    print('\nPilihan yang anda masukkan tidak tersedia\n')
#pembuatan suatu fungsi program yang memudahkan pasien untuk membuat list appointmen, nantinya list data tersebut akan disimpan dalam cart
def appointmentPasien():
     while True:
          inputan = int(input('''
     ===SELAMAT DATANG DI RUMAH SAKIT BAHAGIA===
     
     LIST PROGRAM:
     1. MEMBUAT APPOINTMENT DARI DATABASE PASIEN
     2. MEMBUAT APPOINTMENT MANUAL
     3. KEMBALI KE MENU UTAMA
                              
     SILAHKAN MASUKKAN PILIHAN : ''')) 
          if inputan == 1:
                    menampilkanDaftarPasien()
                    newIDpasien=int(input('ID Pasien : '))
                    for j in listPasien.keys():
                         if newIDpasien == listPasien[j]['ID pasien']:
                              inputan1 = str(input('\n Masukkan Nomor Handphone :'))
                              Jam = (input('\n Masukkan Jam Kunjungan : '))
                         else:
                              continue
                #list yang dibuat disimpan dalam cart         
                         cart.append({
                                             'nama': listPasien[j]['nama'], 
                                             'ID pasien': listPasien[j]['ID pasien'], 
                                             'Nomor Handphone': inputan1,
                                             'Jam': Jam
                                   })
                         
                         print('\n\tLIST APPOINTMENT :')
                         print(Fore.GREEN +'Nama \t\t | ID Pasien\t | Nomor Handphone \t | Waktu Kedatangan')
                         for item in cart :
                                   print(Fore.GREEN + '{}\t | {}\t\t | {}\t \t  | {}'.format(item['nama'], item['ID pasien'], item['Nomor Handphone'], item['Jam']))
     #Pasien Memasukkan data secara manual, hal ini dikarenakan tidak semua pasien yang datang sudah tersimpan di database               
          elif inputan == 2:
                    newNama = input('Masukkan nama Anda : ')
                    newID = int(input('Masukkan ID Pasien Anda : '))
                    newHP = int(input('Masukkan Nomor Handphone Anda : '))
                    newJam = input('Masukkan Jam Kunjungan : ')
                    cart.append({
                         'nama': newNama,
                         'ID pasien' : newID,
                         'Nomor Handphone' : newHP,
                         'Jam' : newJam
                    
                    })
                    print('\n\tLIST APPOINTMENT :')
                    print(Fore.GREEN +'Nama \t\t | ID Pasien\t | Nomor Handphone \t | Waktu Kedatangan')
                    for item in cart :
                     print(Fore.GREEN +'{}\t | {}\t\t | {}\t \t  | {}'.format(item['nama'], item['ID pasien'], item['Nomor Handphone'], item['Jam']))
                    
          elif inputan == 3:
                    break
          else :
                    print(Fore.RED + '\nPilihan yang anda masukkan tidak tersedia\n')
                    
# fungsi untuk menampilkan isi didalam cart
def tampilanCart():
     if len(cart)==0:
        print(Fore.RED + "\n\tTidak ada List yang tersedia")
        while True:
          inputan = int(input("masukkan angka 0 untuk kembali ke Menu Semula : "))
          if inputan == 0:
           break
     else:
          print('\n\tLIST APPOINTMENT :')
          print('Nama \t\t | ID Pasien\t | Nomor Handphone \t | Waktu Kedatangan')
          for item in cart :
               print('{}\t | {}\t\t | {}\t \t  | {}'.format(item['nama'], item['ID pasien'], item['Nomor Handphone'], item['Jam']))
# fungsi untuk mendefinisikan admin
def khususAdmin():
     while True :
         
          pilihanMenu = input('''
               =====Selamat Datang Admin=====
                              
                =====ADMIN====

               List Program :
               1. Menampilkan Daftar Pasien
               2. Mengupdate Pasien
               3. Menghapus Pasien
               4. Melihat List Appointment
               5. Kembali Ke Menu Utama

               Masukkan angka program yang ingin dijalankan : ''')

          if(pilihanMenu == '1') :
               tampilanPasien()
               
          elif(pilihanMenu == '2') :
                    while True:
                         inputan = int(input(''' 
           ===MENGUPDATE PASIEN===
                                             
           list Program:
           1. Mengganti Data Pasien
           2. Menambahkan Data Pasien
           3. Kembali Ke menu utama
                                        
           Masukkan angka program yang ingin dijalankan: ''' ))
                         if inputan == 1:
                              updatePasien()
                         elif inputan == 2 :
                              menambahPasien()
                         elif inputan == 3:
                              break
                         else:
                              print('\nPilihan yang anda masukkan tidak tersedia\n')
          elif(pilihanMenu == '3') :
                    menghapusPasien()
          elif(pilihanMenu == '4'):
               tampilanCart()
          elif(pilihanMenu == '5'):
               print('\nTERIMA KASIH DAN SAMPAI JUMPA LAGI\n')
               break
          else:
               print('\nPilihan yang anda masukkan tidak tersedia\n')
# fungsi untuk mendefinisikan pasien
def khususPasien(): 
     while True :
          pilihanMenu = input('''
               =====Selamat Datang Pasien=====
                              
               =====PASIEN====
                              
               List Program :
               1. Menampilkan Daftar Pasien
               2. Membuat List Appointment
               3. Kembali Ke Menu Utama


               Masukkan angka program yang ingin dijalankan : ''')
          if(pilihanMenu == '1') :
               tampilanPasien()
          elif(pilihanMenu =='2'):
               appointmentPasien()
          elif(pilihanMenu == '3'):
               break
          else:
               print('\nPilihan yang anda masukkan tidak tersedia\n')
#Menjalankan Program dengan 2 kondsisi Admin atau Pasien
while True : # looping untuk menjalankan program dengan memanggil semua fungsi yang telah didefinisikan
     maxPasienID=(max(listPasien))
     pilihanMenu = input('''
               =====Selamat Datang Pasien di Rumah Sakit Bahagia=====
                              
               List Program :
               1. Program Khusus Admin
               2. Program Khusus Pasien
               3. Exit Program


               Masukkan angka program yang ingin dijalankan : ''')
     if (pilihanMenu == '1'): 
          #akan ditanyakaan code untuk admin
          input1 = str(input('\nMasukkan Code Admin :'))
          if input1 == codeAdmin:
               khususAdmin()
          else:
               print('Anda Bukan Admin')
               
          #menu untuk pasien tidak memerlukan code
     elif(pilihanMenu == '2'):
          khususPasien()
     elif(pilihanMenu == '3'):
          print('\nTERIMA KASIH DAN SAMPAI JUMPA LAGI\n')
          break
     else:
               print(Fore.RED + '\nPilihan yang anda masukkan tidak tersedia\n')
