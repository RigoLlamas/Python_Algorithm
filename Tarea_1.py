"""
1.	La calificación final de un alumno es un número entero que se obtiene promediando la calificación
 de sus exámenes, tareas, proyecto y concursos. El “.5” sube 1.

print("Ingrese las calificaciones de su alumno")
examen = int(input("Calificacion examen: "))
tareas = int(input("Calificacion tareas: "))
proyectos = int(input("Calificacion proyectos: "))
concursos = int(input("Calificacion concursos: "))

puntajeFinal = examen +tareas + proyectos + concursos
print("El puntaje obtenido es: ", puntajeFinal, " / 400")

calificacionFinal = float(puntajeFinal / 4)

print("El alumno tiene una nota final redondeada de: ", int(calificacionFinal + 0.5))


2.	Número de ejemplares completos (sin parte fraccionaria) de un producto que se pueden comprar si cuento con X pesos y el producto cuesta Y pesos.
 X y Y pueden incluir centavos.

x = float(input("Costo del producto: "))
y = float(input("Cantidad de dinero actual: "))
print("El cliente puede comprar hasta", (int (y/x))), "productos"


3.	Solicitar los datos de una persona por separado: nombre, apellido paterno y apellido materno.
 Imprimir su nombre completo en una sola línea, incluyendo los espacios correspondientes. Utilizar concatenación.

nombre = input("Ingrese nombre: ")
apellidoPaterno = input("Ingrese apellido paterno: ")
apellidoMaterno = input("Ingrese apellido materno: ")

print(nombre + " " + apellidoPaterno + " " + apellidoMaterno)

4.	La longitud de la hipotenusa de un triángulo rectángulo, dadas las longitudes de los catetos, según el teorema de Pitágoras.
 Use el operador de potencia **. ¿A qué potencia hay que elevar un número para obtener su raíz cuadrada?

print("Ingresa los lados del triangulo para calcular la hipotenusa del triangulo")
catetoAdyacente = float(input("Valor del cateto adyacente (a): "))
catetoOpuesto = float(input("Valor del cateto opuesto (b): "))

print("El valor de la hipotenusa es: ", (catetoAdyacente**2 + catetoOpuesto**2)**(1/2))

5.	Una hora tiene un número determinado de segundos.
 Pedir al usuario el número total de segundos y mostrar en pantalla el número de segundos restantes después de quitar los segundos que suman horas completas.
 Por ejemplo, si el total de segundos es 7350, la respuesta es 150. Usar el operador módulo.

print("Convertidor de segundos a horas")

totalSegundos = int(input("Ingresé la cantidad de segundos a convertir: "))

horasCalculadas = int(totalSegundos / 3600)

print("Se ingresaron ", totalSegundos, " equivalentes a:")
print("Horas totales: ", horasCalculadas)
print("Segundos restantes: ", (totalSegundos % 3600))

"""