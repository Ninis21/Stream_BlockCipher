#enkripsi ASCII dengan kode biner StreamCipher
def enkripsi_stream_ascii(teks):
    hasil_enkripsi = ""
    for karakter in teks:
        kode_ascii = ord(karakter)
        kode_biner = bin(kode_ascii)[2:]  #mengabaikan awalan "0b" pada hasil biner
        hasil_enkripsi += kode_biner + " "
    return hasil_enkripsi

#dekripsi ASCII dari kode biner StreamCipher
def deskripsi_stream_ascii(teks):
    teks_biner = teks.split()
    hasil_deskripsi = ""
    for biner in teks_biner:
        kode_ascii = int(biner, 2)
        karakter = chr(kode_ascii)
        hasil_deskripsi += karakter
    return hasil_deskripsi

#enkripsi ASCII dari kode biner BlockCipher
def enkripsi_block_ascii(teks):
    hasil_enkripsi = ""
    for karakter in teks:
        kode_ascii = ord(karakter)
        hasil_enkripsi += bin(kode_ascii)[2:].zfill(8) + " " #Mengkonversi ke biner
    return hasil_enkripsi

#dekripsi ASCII dari kode biner BlockCipher
def deskripsi_block_ascii(teks):
    teks = teks.strip() #Menghapus spasi diawal dan akhir
    teks_biner = teks.split(" ")
    hasil_deskripsi = ""
    for biner in teks_biner:
        kode_ascii = int(biner, 2)
        hasil_deskripsi += chr(kode_ascii)
    return hasil_deskripsi
    
if __name__ == '__main__':
    print ('-----------------------------------')
    print ('    Nama        : Munis Zulhusni   ')
    print ('    Nim         : A11.2021.13693   ')
    print ('    Kelas       : A11.4302         ')
    print ('-----------------------------------')   
    
    option = int (input ('1. Enkripsi\n2. Deskripsi\nPilih Option              : '))
    if option == 1:
        teks = input ('Masukan pesan (Plaintext) : ')
        hasil_enkripsi_stream = enkripsi_stream_ascii(teks)
        hasil_enkripsi_block = enkripsi_block_ascii(teks)
        print('Hasil Enkripsi SteamCipher          :',hasil_enkripsi_stream)
        print('Hasil Enkripsi BlockCipher          :',hasil_enkripsi_block)
        
    elif option == 2:
        format_type = input('Masukkan format\n(Stream Cipher/Block Cipher)      : ')
        teks = input (f'Masukan pesan ({format_type})     : ')
        
        if format_type.lower() == 'stream cipher':
            hasil_deskripsi_stream = deskripsi_stream_ascii(teks)
            print (f'Hasil Deskripsi {format_type}     :',hasil_deskripsi_stream)
            
        elif format_type.lower() == 'block cipher':    
            hasil_deskripsi_block = deskripsi_block_ascii(teks)
            print (f'Hasil Deskripsi {format_type}      :',hasil_deskripsi_block)
            
        else:
            print ('FORMAT TIDAK VALID')
    else:
        print ('TIDAK VALID! PILIH OPSI LAIN!')    

