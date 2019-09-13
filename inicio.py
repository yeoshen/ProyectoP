# proyecto_final
# creamos el string con los nombres de los clientes
clients = 'Rogelio, Paco, Sebastian, Adrian'


def _print_welcome():  # funcion para dar el mensaje de bienvenida
    print('Welcome to Monares POS')
    print('what would you like to do today?')
    print('*' * 52)  # imprimimos el caracter "*" 52 veces
    # Mostramos el menu al usuario
    print('[C]reate client')
    print('[R]ead client\'s list ')
    print('[U]pdate client')
    print('[D]elete client')


def verify_client(client_name):
    """
    Esta funcion sirve para verificar si un cliente se encuentra en el string o no.
    Recibe un parametro, el nombre del cliente y devuelve un valor positivo si el nombre
    se encuentra en el string y viceversa
    """
    global clients
    if client_name in clients:
        return True
    else:
        return False


def _client_not_found_tollgate():
    """
    Esta funcion sirve para mostrar un mensaje preestablecido si un cliente no se encuentra 
    en el string de los clientes
    """
    print("Client is not in client\'s list")


def create_client(client_name):
    """
    Esta función sirve para agregar un cliente al string de la lista
    """
    global clients  # Utilizamos global para definir que la variable es la global, es decir la que definimos con pablo y ricardo
    # Ejecutamos la funcion verify client, si la cadena del nombre del cliente está en el string etonces...
    if (verify_client(client_name)):
        print('Client already exists')  # Mostramos un mensaje al usuario
    else:
        _add_coma()  # Si no, ejecutamos la funcion _add_coma para agregar una coma y un espacio al último nombre
        clients += client_name  # adicionamos el nuevo string pero con la funcion capitalize para poner el primer caractér en mayuscula y seguir con el formato


def read_client_list():
    """
    función que imprime la lista de clientes
    """
    global clients
    print(clients)  # imprimimos el string clientes, es decir la lista de clientes


def update_client(client_name):
    """
    Función que sirve para actualizar el nombre de un cliente, 
    recibe un parametro que es el string del nombre del cliente a editar
    """
    global clients  # Utilizamos global para definir que la variable es la globarl, es decir la que definimos con pablo y ricardo
    # Si el cliente se encuentra registrado entonces...
    if (verify_client(client_name)):
        # Pedimos al usuario que ingrese el nuevo nombre de cliente
        updated_client_name = input(
            'What is the updated client name?').capitalize()
        # Ejecutamos la funcion replace, la cual recibe dos parametros, el string a reemplazar
        clients = clients.replace(client_name, updated_client_name)
        # y el string con el cual se remplazara al anterior
    else:
        # sino, ejecutamos la funcion _client_not_found_tollgate() para mostrar el mensaje que no se ha encontrado el cliente (string)
        _client_not_found_tollgate()


def delete_client(client_name):
    """
    Función para borrar el cliente (Remplazar por una cadena vacía)
    """
    global clients
    # Si el cliente está registrado, entonces...
    if (verify_client(client_name)):
        # Remplazamos el nombre concatenado con una , y un espacio y lo remplazamos por una cadena vacía
        clients = clients.replace(client_name + ', ', '')
    else:
        # sino, ejecutamos la funcion _client_not_found_tollgate() para mostrar el mensaje que no se ha encontrado el cliente (string)
        _client_not_found_tollgate()


def _add_coma():  # el nombre de la función comienza con un guión bajo para establecer que será una funcion privada
    """
    Función que sirve para agregar una coma y un espacio para separar los substrings
    """
    global clients
    clients += ", "  # se agrega una coma y un espacio al string para separar los nuevos valores


def _get_client_name():
    """
    Función que sierve para obtener el nombre del cliente con el formato capitalizado
    """
    return input('What is the client name?').capitalize()  # guardamos en la variable client_name el valor de los caracteres que ingresa el usuario hasta recibir un enter


if __name__ == '__main__':  # funcion main
    _print_welcome()  # ejecutamos la funcion que da el mensaje de bienvenida
    command = input().lower()  # guardamos el valor del dato ingresado en la variable command pero lo convertimos a miunsculas para realizar la accion si presiona "C" o "c"
    if command == 'c':  # si el comando es igual al caracter "c" procedemos a realizar los pasos de create/crear
        # Ejecutamos la función para obtener el nombre del cliente
        client_name = _get_client_name()
        # Ejecutamos la funcion crear cliente y enviamos como parametro el valor de la variable que almacena lo que digitó el usuario
        create_client(client_name)
        read_client_list()  # Ejecutamos la funcion listar clientes
    elif command == 'r':  # si el comando es igual al caracter "r" procedemos a realizar los pasos de read/leer
        read_client_list()  # Ejecutamos la funcion listar clientes
    elif command == 'u':  # si el comando es igual al caracter "u", procedemos a realizar los pasos de update/actualizar
        # Ejecutamos la función para obtener el nombre del cliente
        client_name = _get_client_name()
        update_client(client_name)
        read_client_list()  # Ejecutamos la funcion listar clientes
    elif command == 'd':  # si el dato ignresado por el usuario es "d" procedemos a realizar los pasos de delete/eliminar
        # Ejecutamos la función para obtener el nombre del cliente
        client_name = _get_client_name()
        delete_client(client_name)
        read_client_list()  # Ejecutamos la funcion listar clientes
    else:
        # Si el usuario no digita alguna de nuestras opciones entonces mostramos un mensaje de error
        print('ERROR: Invalid command')
input()  # Escribimos un input para que el programa haga una pausa y no cierre la ventana hasta recibir un enter
