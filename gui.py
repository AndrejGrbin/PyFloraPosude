import tkinter as tk
from tkinter import messagebox
from repo import connect_to_database, close_database_connection, get_user_data, update_user_data

class MainWindow(tk.Tk):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.title("PyPosude - Popis posuda")
        self.geometry("600x400")

        # Gornji traka (navbar)
        navbar_frame = tk.Frame(self)
        navbar_frame.pack(side=tk.TOP, fill=tk.X)

        # Naziv aplikacije
        app_name_label = tk.Label(navbar_frame, text="PyFlora Posude", font=("Arial", 14, "bold"))
        app_name_label.pack(side=tk.LEFT, padx=10, pady=5)

        # Gumbi Biljke i Moj Profil
        plants_button = tk.Button(navbar_frame, text="Biljke", command=self.open_plants_window)
        plants_button.pack(side=tk.LEFT, padx=10, pady=5)

        profile_button = tk.Button(navbar_frame, text="Moj Profil", command=self.open_update_window)
        profile_button.pack(side=tk.LEFT, padx=10, pady=5)

        # User_name prijavljenog korisnika
        user_data = get_user_data(self.conn)
        user_name_label = tk.Label(navbar_frame, text="Korisnik: {}".format(user_data[1]))
        user_name_label.pack(side=tk.RIGHT, padx=10, pady=5)

        # Implementirajte prikaz popisa posuda

    def open_plants_window(self):
        plants_window = PlantsWindow(self.conn)
        plants_window.mainloop()

    def open_update_window(self):
        update_window = UpdateUserWindow(self.conn)
        update_window.mainloop()

    def __del__(self):
        close_database_connection(self.conn)

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.conn = connect_to_database()
        self.title("Prijava")
        self.geometry("300x150")

        # Labela i unos za korisničko ime
        username_label = tk.Label(self, text="Korisničko ime:")
        username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        # Labela i unos za lozinku
        password_label = tk.Label(self, text="Lozinka:")
        password_label.pack()
        self.password_entry = tk.Entry(self, show="*")  # Skrivanje prikaza unosa lozinke
        self.password_entry.pack()

        # Gumb za prijavu
        login_button = tk.Button(self, text="Prijavi se", command=self.login)
        login_button.pack()

    def login(self):
        # Uneseni korisnički podaci
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Provjera korisničkih podataka u bazi
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            # Prijava uspješna, prikaži poruku i otvori glavni prozor
            messagebox.showinfo("Prijavljeno", "Uspješna prijava!")
            main_window = MainWindow(self.conn)
            self.destroy()
            main_window.mainloop()
        else:
            # Prijava nije uspjela, prikaži poruku o pogrešnim podacima
            messagebox.showerror("Pogrešna prijava", "Uneseni korisnički podaci nisu ispravni.")

        cursor.close()

    def __del__(self):
        close_database_connection(self.conn)

class UpdateUserWindow(tk.Tk):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.title("Ažuriranje korisnika")
        self.geometry("300x150")

        # Implementirajte prozor za ažuriranje korisnika

    def __del__(self):
        close_database_connection(self.conn)

class PlantsWindow(tk.Tk):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.title("PyPosude - Popis biljaka")
        self.geometry("600x400")

        # Gornji traka (navbar)
        navbar_frame = tk.Frame(self)
        navbar_frame.pack(side=tk.TOP, fill=tk.X)

        # Naziv aplikacije
        app_name_label = tk.Label(navbar_frame, text="PyFlora Posude", font=("Arial", 14, "bold"))
        app_name_label.pack(side=tk.LEFT, padx=10, pady=5)

        # Gumbi Biljke i Moj Profil
        plants_button = tk.Button(navbar_frame, text="Biljke", state=tk.DISABLED)
        plants_button.pack(side=tk.LEFT, padx=10, pady=5)

        profile_button = tk.Button(navbar_frame, text="Moj Profil", command=self.open_update_window)
        profile_button.pack(side=tk.LEFT, padx=10, pady=5)

        # User_name prijavljenog korisnika
        user_data = get_user_data(self.conn)
        user_name_label = tk.Label(navbar_frame, text="Korisnik: {}".format(user_data[1]))
        user_name_label.pack(side=tk.RIGHT, padx=10, pady=5)

        # Implementirajte prikaz popisa biljaka

    def open_update_window(self):
        update_window = UpdateUserWindow(self.conn)
        update_window.mainloop()

    def __del__(self):
        close_database_connection(self.conn)
