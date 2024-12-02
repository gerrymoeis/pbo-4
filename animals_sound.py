import tkinter as tk
from playsound3 import playsound

class Animal:
    def make_sound(self):
        # playsound("kucing.mp3")
        return "Miaw Miaw Ninja!"

# Kelas turunan Bird
class Bird(Animal):
    def make_sound(self):
        return "Twiwit Twiwit"

# Kelas turunan Dog
class Dog(Animal):
    def make_sound(self):
        return "Anjengg!"

# Kelas turunan Bird
class Babi(Animal):
    def make_sound(self):
        return "Ang Eng Ang"

# Kelas turunan Monyet
class Monyet(Animal):
    def make_sound(self):
        return "U u A A"

root = tk.Tk()
root.title("Suara Binatang!")

# Label untuk menampilkan hasil suara
label_result = tk.Label(root, text="Klik salah satu tombol untuk mendengar suara hewan.", font=("Arial", 20))
label_result.pack(pady=20)

label_sound = tk.Label(root, text="...", font=("Arial", 16))
label_sound.pack(pady=20)

# Fungsi untuk menampilkan suara berdasarkan jenis hewan yang dipilih
def show_sound(animal):
    label_sound.config(text=animal.make_sound())

# Tombol untuk memilih Burung
button_bird = tk.Button(root, text="Burung", font=("Arial", 16), command=lambda: show_sound(Bird()))
button_bird.pack(pady=10)
# Tombol untuk memilih Anjing
button_dog = tk.Button(root, text="Anjing", font=("Arial", 16), command=lambda: show_sound(Dog()))
button_dog.pack(pady=10)

# Tombol untuk memilih Babi
button_pig = tk.Button(root, text="Babi", font=("Arial", 16), command=lambda: show_sound(Babi()))
button_pig.pack(pady=10)
# Tombol untuk memilih Monyet
button_monkey = tk.Button(root, text="Monyet", font=("Arial", 16), command=lambda: show_sound(Monyet()))
button_monkey.pack(pady=10)

# Tombol untuk memilih Hewan Umum
button_animal = tk.Button(root, text="Hewan Umum", font=("Arial", 16), command=lambda: show_sound (Animal()))
button_animal.pack(pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()