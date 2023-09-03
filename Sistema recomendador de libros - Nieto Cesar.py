class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

#Remover tildes
def quitar_tildes(s):
    tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u', 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U', 'Ü': 'U'}
    return ''.join(tildes.get(c, c) for c in s)

# agregar libros
def  agregar_libro(lista_libros):
    titulo = input("Ingrese el título del libro:").capitalize()
    autor = input("Ingrese el autor del libro:").capitalize()
    genero = input("Ingrese el género libro:").capitalize()
    puntuacion = ""
    while not puntuacion.isnumeric() :
        puntuacion = (input("Ingrese puntuación del libro:"))
    puntuacion = float (puntuacion)
    nuevo_libro = Libro (titulo, autor, genero, puntuacion)
    lista_libros.append (nuevo_libro)
    print (f"Libro {Libro} agregado")

# buscar libro por genero
def buscar_libro(lista_libros, genero_busqueda):
    genero_busqueda = genero_busqueda.capitalize()
    libros_genero = [libro.titulo for libro in lista_libros if quitar_tildes(libro.genero) == genero_busqueda]
    if libros_genero:
        print(f"Libros en el género {genero_busqueda} :")
        for titulo_libro in libros_genero:
            print(f"- {titulo_libro}")
    else:
        print(f"No existen libros para el género {genero_busqueda}")
        
#recomendar libro
def recomendar_libro (lista_libros, genero_recomendacion):
    genero_recomendacion = genero_recomendacion.capitalize()
    libros_de_genero = [libro for libro in lista_libros if quitar_tildes(libro.genero) == genero_recomendacion]
    if libros_de_genero:
        libro_recomendado = max (libros_de_genero, key=lambda libro: libro.puntuacion)  
        print (f"Se recomienda {libro_recomendado.titulo}")
    else:
        print(f"No hay libros para el género {genero_recomendacion}")   

#lista libros
lista_libros = [
    Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5),
    Libro("1984", "George Orwell", "Ciencia Ficción", 4.3),
    Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7),
    Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2),
    Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4),
    Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6),
    Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8),
    Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4),
    Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)
]

while True:
    menu = input (f"""¿Qué acción desea realizar?
                  1 - Agregar libro
                  2 - Buscar libros por género
                  3 - Recomendar libro
                  S - Salir
                  Ingrese a continuación su opción elegida: """).upper()
    if menu == "S":
        print (f"Adiós")
        exit()
    match menu:
        case "1":
            agregar_libro (lista_libros)
        
        case "2":
            genero_busqueda = input (f"Ingrese el género: ").capitalize()
            buscar_libro (lista_libros, genero_busqueda)
        
        case "3":
            genero_recomendacion = input (f"Ingresa el género para recibir recomendación: ").capitalize()
            recomendar_libro (lista_libros, genero_recomendacion)
    menu=""


