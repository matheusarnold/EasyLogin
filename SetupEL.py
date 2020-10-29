import subprocess

subprocess.call('pip install selenium', shell = True)

username = input("\nEmail (Tanpa @binus.ac.id): ")
password = input("Password: ")

f = open("Credential.txt", "w+")

f.write(username)
f.write("\n")
f.write(password)

f.close()