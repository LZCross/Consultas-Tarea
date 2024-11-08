
# Ejercicio 1: Convertir números romanos a decimales
def roman_to_decimal(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_value = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_numerals[char]
        if value >= prev_value:
            decimal_value += value
        else:
            decimal_value -= value
        prev_value = value
    
    return decimal_value

# Ejercicio 2: Validar una cadena de paréntesis, llaves y corchetes
def is_valid_sequence(sequence):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    for char in sequence:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets.keys():
            if stack == [] or stack.pop() != matching_brackets[char]:
                return "Inválido"
    
    return "Válido" if not stack else "Inválido"

# Ejercicio 3: Contar números primos en una lista
def count_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return sum(1 for number in numbers if is_prime(number))

# Ejercicio 4: Convertir calificaciones a letras
def grades_to_letters(grades):
    letter_grades = []
    for grade in grades:
        if grade >= 90:
            letter_grades.append("A")
        elif grade >= 80:
            letter_grades.append("B")
        elif grade >= 70:
            letter_grades.append("C")
        elif grade >= 60:
            letter_grades.append("D")
        else:
            letter_grades.append("F")
    return letter_grades

# Ejercicio 5: Obtener palabras palíndromas de una lista
def find_palindromes(words):
    return [word for word in words if word == word[::-1]]

# Ejercicio 6: Clase para representar un triángulo rectángulo
class TrianguloRectangulo:
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2

    def area(self):
        return (self.cateto1 * self.cateto2) / 2

    def perimetro(self):
        return self.cateto1 + self.cateto2 + self.hipotenusa()

    def hipotenusa(self):
        return (self.cateto1**2 + self.cateto2**2) ** 0.5

    def angulos(self):
        import math
        angulo1 = math.degrees(math.atan(self.cateto1 / self.cateto2))
        angulo2 = 90 - angulo1
        return angulo1, angulo2

# Ejercicio 7: Clase para representar una esfera
class Esfera:
    def __init__(self, radio):
        self.radio = radio

    def area_superficie(self):
        return 4 * 3.1416 * (self.radio**2)

    def volumen(self):
        return (4 / 3) * 3.1416 * (self.radio**3)

    def diametro(self):
        return 2 * self.radio

# Ejercicio 8: Clase para representar a un empleado
class Empleado:
    def __init__(self, nombres, apellidos, cedula, fecha_nacimiento, salario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.salario = salario

    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def iniciales(self):
        return ".".join([n[0] for n in (self.nombres + " " + self.apellidos).split()]) + "."

    def edad(self):
        from datetime import datetime
        nacimiento = datetime.strptime(self.fecha_nacimiento, "%d-%m-%Y")
        hoy = datetime.now()
        return hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))

    def ganancia_anual(self):
        return self.salario * 12

# Ejercicio 9: Clase para representar una pizza
class Pizza:
    def __init__(self, nombre, ingredientes, tamaño, precio_venta, costo_produccion, tiempo_coccion):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.tamaño = tamaño
        self.precio_venta = precio_venta
        self.costo_produccion = costo_produccion
        self.tiempo_coccion = tiempo_coccion

    def ganancia_neta(self):
        return self.precio_venta - self.costo_produccion

    def contiene_ingrediente(self, ingrediente):
        return ingrediente in self.ingredientes

# Ejercicio 10: Clase para representar una torre de ajedrez
class TorreAjedrez:
    def __init__(self, color, posicion):
        self.color = color
        self.posicion = posicion

    def posibles_jugadas(self):
        fila, columna = self.posicion[1], self.posicion[0]
        movimientos = [f"{columna}{f}" for f in range(1, 9) if f != int(fila)]
        movimientos += [f"{c}{fila}" for c in "ABCDEFGH" if c != columna]
        return movimientos

    def puede_atacar(self, celda):
        return celda[0] == self.posicion[0] or celda[1] == self.posicion[1]
