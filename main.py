import string
from tkinter import *

#####LISTA DE TAREAS#####
###Corto Plazo
# Interfaz grafica
# Eliminar avisos de contraseña e usuario invalido
###Largo plazo
# Añadir base de datos

# Apertura de ficheros
users_file_write = open("users.txt", "a")
password_file_write = open("passwords.txt", "a")
users_file_read = open("users.txt", "r")
password_file_read = open("passwords.txt", "r")

# Obtencion de datos de los ficheros
users = users_file_read.readlines()
passwords = password_file_read.readlines()


# Funciones
def valid_char(i):
    valid = True
    if not i.isalnum() and i != '_':
        valid = False

    return valid


def complicated_password(password):
    number = False
    alpha = False
    complicated = False

    for i in password:
        if i.isalpha():
            alpha = True
        elif i.isnumeric():
            number = True
        if number and alpha:
            complicated = True
            break

    return complicated


def valid_user(user_id):
    valid = True
    if len(user_id) < 5 or len(user_id) > 12:
        valid = False

    for i in user_id:
        if not valid_char(i):
            valid = False
            break

    return valid


def valid_password(password_id):
    valid = True
    if len(password_id) < 8:
        valid = False

    return valid


def check_login(user_id, password_id):
    user_founded = False
    correct_password = False
    for line in users:
        line_user = line.split()[0]
        line_code_user = line.split()[1]
        if line_user == user_id:
            user_founded = True
            break

    if not user_founded:
        user_not_founded_label = Label(text="Usuario no encontrado")
        user_not_founded_label.place(relx=0.5, rely=0.2, anchor=CENTER)
    else:
        for line in passwords:
            line_code_password = line.split()[0]
            line_password = line.split()[1]
            if line_code_password == line_code_user:
                if password_id == line_password:
                    correct_password = True
                break

        if correct_password:
            print("Entra al sistema")
        else:
            incorrect_password_label = Label(text="La contraseña no es correcta")
            incorrect_password_label.place(relx=0.5, rely=0.2, anchor=CENTER)


def check_register(user_id, password1_id, password2_id):
    user_founded = False
    for line in users:
        line_user = line.split()[0]
        if line_user == user_id:
            user_founded = True
            break

    if user_founded:
        user_founded_label = Label(text="El nombre de usuario esta en uso")
        user_founded_label.place(relx=0.5, rely=0.2, anchor=CENTER)
    else:
        if not valid_user(user_id):
            not_valid_user = Label(text="El usuario no es valido")
            not_valid_user.place(relx=0.5, rely=0.2, anchor=CENTER)
        elif not valid_password(password1_id):
            not_valid_password = Label(text="La constraseña no es valida")
            not_valid_password.place(relx=0.5, rely=0.2, anchor=CENTER)
        elif password1_id != password2_id:
            not_same_password_label = Label(text="Las contraseñas no coinciden")
            not_same_password_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        else:
            user_code = str(len(users))
            users_file_write.write(user_id + ' ' + user_code + '\n')
            password_file_write.write(user_code + ' ' + password1_id + '\n')
            success_label = Label(text="Usuario registrado correctamente")
            success_label.place(relx=0.5, rely=0.2, anchor=CENTER)


def register(components_main, components):
    hide(components_main)
    show_register(components)


def login(components_main, components):
    hide(components_main)
    show_login(components)


def go_back_main(components, components_main):
    hide(components)
    show_main(components_main)


def show_main(components):
    components[0].place(relx=0.5, rely=0.45, anchor=CENTER)
    components[1].place(relx=0.5, rely=0.55, anchor=CENTER)
    components[2].place(relx=0.5, rely=0.85, anchor=CENTER)


def show_login(components):
    components[0].place(relx=0.5, rely=0.3, anchor=CENTER)
    components[1].place(relx=0.5, rely=0.35, anchor=CENTER)
    components[2].place(relx=0.5, rely=0.4, anchor=CENTER)
    components[3].place(relx=0.5, rely=0.45, anchor=CENTER)
    components[4].place(relx=0.5, rely=0.65, anchor=CENTER)
    components[5].place(relx=0.5, rely=0.85, anchor=CENTER)
    components[6].place(relx=0.9, rely=0.85, anchor=E)
    components[7].place(relx=0.1, rely=0.85, anchor=W)


def show_register(components):
    components[0].place(relx=0.5, rely=0.3, anchor=CENTER)
    components[1].place(relx=0.5, rely=0.35, anchor=CENTER)
    components[2].place(relx=0.5, rely=0.4, anchor=CENTER)
    components[3].place(relx=0.5, rely=0.45, anchor=CENTER)
    components[4].place(relx=0.5, rely=0.5, anchor=CENTER)
    components[5].place(relx=0.5, rely=0.55, anchor=CENTER)
    components[6].place(relx=0.5, rely=0.65, anchor=CENTER)
    components[7].place(relx=0.5, rely=0.85, anchor=CENTER)
    components[8].place(relx=0.9, rely=0.85, anchor=E)
    components[9].place(relx=0.1, rely=0.85, anchor=W)


def hide(components):
    for component in components:
        component.place_forget()


def main():
    # Ventana principal
    main_window = Tk()

    # Obtencion del tamaño de la ventana para centrarlo
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    size = tuple(int(_) for _ in main_window.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2

    # Configuración de la ventana principal
    main_window.title("Inicio de sesion")
    main_window.geometry("+%d+%d" % (x - 300, y - 250))
    main_window.configure(bg='#09795f')
    main_window.geometry("600x500")

    components_main = []
    components_login = []
    components_register = []

    # Componentes de main
    login_button = Button(text="Login", width=8, height=1, command=lambda: login(components_main, components_login))
    register_button = Button(text="Registrate", width=8, height=1,
                             command=lambda: register(components_main, components_register))
    exit_button = Button(text="Salir", width=8, height=1, command=main_window.quit)

    # Componentes de login y register
    user_label = Label(text="Nombre de usuario")
    user_entry = Entry()
    password1_label = Label(text="Contraseña")
    password1_entry = Entry(show="*")
    password2_label = Label(text="Contraseña de nuevo")
    password2_entry = Entry(show="*")
    send_login_button = Button(text="Enviar", width=8, height=1,
                               command=lambda: check_login(user_entry.get(), password1_entry.get()))
    send_register_button = Button(text="Enviar", width=8, height=1,
                                  command=lambda: check_register(user_entry.get(), password1_entry.get(),
                                                                 password2_entry.get()))
    go_back_from_login_button = Button(text="Atras", width=8, height=1,
                                       command=lambda: go_back_main(components_login, components_main))
    go_back_from_register_button = Button(text="Atras", width=8, height=1,
                                          command=lambda: go_back_main(components_register, components_main))
    go_from_login_to_register_button = Button(text="Registrate", width=8, height=1,
                                              command=lambda: register(components_login, components_register))
    go_from_register_to_login_button = Button(text="Logeate", width=8, height=1,
                                              command=lambda: login(components_register, components_login))

    components_main = [login_button, register_button, exit_button]
    components_login = [user_label, user_entry, password1_label, password1_entry, send_login_button, exit_button,
                        go_back_from_login_button, go_from_login_to_register_button]
    components_register = [user_label, user_entry, password1_label, password1_entry, password2_label, password2_entry,
                           send_register_button, exit_button, go_back_from_register_button,
                           go_from_register_to_login_button]

    show_main(components_main)

    main_window.mainloop()


main()

users_file_read.close()
password_file_read.close()
users_file_write.close()
password_file_write.close()