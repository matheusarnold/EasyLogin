import subprocess                                           # Untuk memasukkan subprocess library

subprocess.call('pip install selenium', shell = True)       # Untuk membuka CMD / shell, lalu jalankan command 'pip install selenium'
subprocess.call('pip3 install -U selenium', shell = True)   # Kalo gagal, program akan coba pakai command ini

username = input("\nEmail (Tanpa @binus.ac.id): ")          # Meminta user untuk memasukkan email Binusmaya
password = input("Password: ")                              # Meminta user untuk memasukkan password Binusmaya

f = open("Credential.txt", "w+")                            # Create and open file Credential.txt

f.write(username)                                           # Tulis isi variable username di Credential.txt baris pertama
f.write("\n")                                               # Kasih enter
f.write(password)                                           # Tulis isi variable password di Credential.txt baris kedua

f.close()                                                   # Close Credential.txt