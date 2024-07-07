###Especio Vectorial

##Ejercio 1

import sympy as sp

def suma_vectorial(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def multiplicacion_escalar(c, v):
    return (c * v[0], v[1])

def es_espacio_vectorial():
    # Definir variables simbólicas
    x1, y1, x2, y2, c, d = sp.symbols('x1 y1 x2 y2 c d')

    # Vectores simbólicos
    v1 = (x1, y1)
    v2 = (x2, y2)
    v0 = (0, 0)

    # 1. Cerradura bajo la suma
    suma_v1_v2 = suma_vectorial(v1, v2)
    if not (suma_v1_v2 == (x1 + x2, y1 + y2)):
        print("Falló la cerradura bajo la suma")
        return False

    # 2. Conmutatividad de la suma
    if not (suma_vectorial(v1, v2) == suma_vectorial(v2, v1)):
        print("Falló la conmutatividad de la suma")
        return False

    # 3. Asociatividad de la suma
    v3 = (sp.symbols('x3'), sp.symbols('y3'))
    if not (suma_vectorial(v1, suma_vectorial(v2, v3)) == suma_vectorial(suma_vectorial(v1, v2), v3)):
        print("Falló la asociatividad de la suma")
        return False

    # 4. Existencia del elemento neutro
    if not (suma_vectorial(v1, v0) == v1):
        print("Falló la existencia del elemento neutro")
        return False

    # 5. Existencia del elemento opuesto
    opuesto_v1 = (-v1[0], -v1[1])
    if not (suma_vectorial(v1, opuesto_v1) == v0):
        print("Falló la existencia del elemento opuesto")
        return False

    # 6. Cerradura bajo la multiplicación por un escalar
    if not (multiplicacion_escalar(c, v1) == (c * x1, y1)):
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    # 7. Distributividad de la multiplicación escalar respecto a la suma vectorial
    if not (multiplicacion_escalar(c, suma_vectorial(v1, v2)) == suma_vectorial(multiplicacion_escalar(c, v1), multiplicacion_escalar(c, v2))):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma vectorial")
        return False

    # 8. Distributividad de la multiplicación escalar respecto a la suma escalar
    if not (multiplicacion_escalar(c + d, v1) == suma_vectorial(multiplicacion_escalar(c, v1), multiplicacion_escalar(d, v1))):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma escalar")
        return False

    # 9. Asociatividad de la multiplicación escalar
    if not (multiplicacion_escalar(c * d, v1) == multiplicacion_escalar(c, multiplicacion_escalar(d, v1))):
        print("Falló la asociatividad de la multiplicación escalar")
        return False

    # 10. Existencia del elemento unidad
    if not (multiplicacion_escalar(1, v1) == v1):
        print("Falló la existencia del elemento unidad")
        return False

    return True

# Ejecutar la verificación
print(es_espacio_vectorial())  # Debería imprimir True o False

##Ejercicio 2
import sympy as sp

def suma_vectorial(v1, v2):
    return (v1[0], 0)

def multiplicacion_escalar(c, v):
    return (c * v[0], c * v[1])

def es_espacio_vectorial():
    # Definir variables simbólicas
    x1, y1, x2, y2, c, d = sp.symbols('x1 y1 x2 y2 c d')

    # Vectores simbólicos
    v1 = (x1, y1)
    v2 = (x2, y2)
    v0 = (0, 0)

    # 1. Cerradura bajo la suma
    suma_v1_v2 = suma_vectorial(v1, v2)
    if not (suma_v1_v2 == (x1, 0)):
        print("Falló la cerradura bajo la suma")
        return False

    # 2. Conmutatividad de la suma
    if not (suma_vectorial(v1, v2) == suma_vectorial(v2, v1)):
        print("Falló la conmutatividad de la suma")
        return False

    # 3. Asociatividad de la suma
    v3 = (sp.symbols('x3'), sp.symbols('y3'))
    if not (suma_vectorial(v1, suma_vectorial(v2, v3)) == suma_vectorial(suma_vectorial(v1, v2), v3)):
        print("Falló la asociatividad de la suma")
        return False

    # 4. Existencia del elemento neutro
    if not (suma_vectorial(v1, v0) == v1):
        print("Falló la existencia del elemento neutro")
        return False

    # 5. Existencia del elemento opuesto
    opuesto_v1 = (-v1[0], -v1[1])
    if not (suma_vectorial(v1, opuesto_v1) == v0):
        print("Falló la existencia del elemento opuesto")
        return False

    # 6. Cerradura bajo la multiplicación por un escalar
    if not (multiplicacion_escalar(c, v1) == (c * x1, c * y1)):
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    # 7. Distributividad de la multiplicación escalar respecto a la suma vectorial
    if not (multiplicacion_escalar(c, suma_vectorial(v1, v2)) == suma_vectorial(multiplicacion_escalar(c, v1), multiplicacion_escalar(c, v2))):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma vectorial")
        return False

    # 8. Distributividad de la multiplicación escalar respecto a la suma escalar
    if not (multiplicacion_escalar(c + d, v1) == suma_vectorial(multiplicacion_escalar(c, v1), multiplicacion_escalar(d, v1))):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma escalar")
        return False

    # 9. Asociatividad de la multiplicación escalar
    if not (multiplicacion_escalar(c * d, v1) == multiplicacion_escalar(c, multiplicacion_escalar(d, v1))):
        print("Falló la asociatividad de la multiplicación escalar")
        return False

    # 10. Existencia del elemento unidad
    if not (multiplicacion_escalar(1, v1) == v1):
        print("Falló la existencia del elemento unidad")
        return False

    return True

# Ejecutar la verificación
print(es_espacio_vectorial())  # Debería imprimir True o False

##Ejercicio 3
import sympy as sp

def suma_vectorial(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def multiplicacion_escalar(c, v):
    return (sp.sqrt(c) * v[0], sp.sqrt(c) * v[1])

def es_espacio_vectorial():
    # Definir variables simbólicas
    x1, y1, x2, y2, x3, y3, c, d = sp.symbols('x1 y1 x2 y2 x3 y3 c d')

    # Vectores simbólicos
    v1 = (x1, y1)
    v2 = (x2, y2)
    v3 = (x3, y3)
    v0 = (0, 0)

    # 1. Cerradura bajo la suma
    suma_v1_v2 = suma_vectorial(v1, v2)
    if not suma_v1_v2:
        print("Falló la cerradura bajo la suma")
        return False

    # 2. Conmutatividad de la suma
    if suma_vectorial(v1, v2) != suma_vectorial(v2, v1):
        print("Falló la conmutatividad de la suma")
        return False

    # 3. Asociatividad de la suma
    if suma_vectorial(v1, suma_vectorial(v2, v3)) != suma_vectorial(suma_vectorial(v1, v2), v3):
        print("Falló la asociatividad de la suma")
        return False

    # 4. Existencia del elemento neutro
    if suma_vectorial(v1, v0) != v1:
        print("Falló la existencia del elemento neutro")
        return False

    # 5. Existencia del elemento opuesto
    opuesto_v1 = (-v1[0], -v1[1])
    if suma_vectorial(v1, opuesto_v1) != v0:
        print("Falló la existencia del elemento opuesto")
        return False

    # 6. Cerradura bajo la multiplicación por un escalar
    if multiplicacion_escalar(c, v1) is None:
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    # 7. Distributividad de la multiplicación escalar respecto a la suma vectorial
    if multiplicacion_escalar(c, suma_vectorial(v1, v2)) != suma_vectorial(multiplicacion_escalar(c, v1), multiplicacion_escalar(c, v2)):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma vectorial")
        return False

    # 8. Distributividad de la multiplicación escalar respecto a la suma escalar
    if multiplicacion_escalar(c + d, v1) != suma_vectorial(multiplicacion_escalar(c, v1), multiplicacion_escalar(d, v1)):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma escalar")
        return False

    # 9. Asociatividad de la multiplicación escalar
    if multiplicacion_escalar(c * d, v1) != multiplicacion_escalar(c, multiplicacion_escalar(d, v1)):
        print("Falló la asociatividad de la multiplicación escalar")
        return False

    # 10. Existencia del elemento unidad
    if multiplicacion_escalar(1, v1) != v1:
        print("Falló la existencia del elemento unidad")
        return False

    return True

# Ejecutar la verificación
print(es_espacio_vectorial())  # Debería imprimir True o False

##Ejercicio 4
import sympy as sp

def suma_vectorial(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])

def multiplicacion_escalar(c, v):
    return (c * v[0], c * v[1], 0)

def es_espacio_vectorial():
    # Definir variables simbólicas
    x1, y1, z1, x2, y2, z2, x3, y3, z3, c, d = sp.symbols('x1 y1 z1 x2 y2 z2 x3 y3 z3 c d')

    # Vectores simbólicos
    v1 = (x1, y1, z1)
    v2 = (x2, y2, z2)
    v3 = (x3, y3, z3)
    v0 = (0, 0, 0)

    # 1. Cerradura bajo la suma
    suma_v1_v2 = suma_vectorial(v1, v2)
    if not suma_v1_v2:
        print("Falló la cerradura bajo la suma")
        return False

    # 2. Conmutatividad de la suma
    if suma_vectorial(v1, v2) != suma_vectorial(v2, v1):
        print("Falló la conmutatividad de la suma")
        return False

    # 3. Asociatividad de la suma
    if suma_vectorial(v1, suma_vectorial(v2, v3)) != suma_vectorial(suma_vectorial(v1, v2), v3):
        print("Falló la asociatividad de la suma")
        return False

    # 4. Existencia del elemento neutro
    if suma_vectorial(v1, v0) != v1:
        print("Falló la existencia del elemento neutro")
        return False

    # 5. Existencia del elemento opuesto
    opuesto_v1 = (-v1[0], -v1[1], -v1[2])
    if suma_vectorial(v1, opuesto_v1) != v0:
        print("Falló la existencia del elemento opuesto")
        return False

    # 6. Cerradura bajo la multiplicación por un escalar
    if multiplicacion_escalar(c, v1) is None:
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    # 7. Distributividad de la multiplicación escalar respecto a la suma vectorial
    if multiplicacion_escalar(c, suma_vectorial(v1, v2)) != suma_vectorial(multiplicacion_escalar(c, v1), multiplicacion_escalar(c, v2)):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma vectorial")
        return False

    # 8. Distributividad de la multiplicación escalar respecto a la suma escalar
    if multiplicacion_escalar(c + d, v1) != suma_vectorial(multiplicacion_escalar(c, v1), multiplicacion_escalar(d, v1)):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma escalar")
        return False

    # 9. Asociatividad de la multiplicación escalar
    if multiplicacion_escalar(c * d, v1) != multiplicacion_escalar(c, multiplicacion_escalar(d, v1)):
        print("Falló la asociatividad de la multiplicación escalar")
        return False

    # 10. Existencia del elemento unidad
    if multiplicacion_escalar(1, v1) != (v1[0], v1[1], 0):
        print("Falló la existencia del elemento unidad")
        return False

    return True

# Ejecutar la verificación
print(es_espacio_vectorial())  # Debería imprimir True o False

##Ejercicio 5
import sympy as sp

def suma_vectorial(v1, v2):
    return (0, 0, 0)

def multiplicacion_escalar(c, v):
    return (c * v[0], c * v[1], c * v[2])

def es_espacio_vectorial():
    # Definir variables simbólicas
    x1, y1, z1, x2, y2, z2, x3, y3, z3, c, d = sp.symbols('x1 y1 z1 x2 y2 z2 x3 y3 z3 c d')

    # Vectores simbólicos
    v1 = (x1, y1, z1)
    v2 = (x2, y2, z2)
    v3 = (x3, y3, z3)
    v0 = (0, 0, 0)

    # 1. Cerradura bajo la suma
    suma_v1_v2 = suma_vectorial(v1, v2)
    if suma_v1_v2 != (0, 0, 0):
        print("Falló la cerradura bajo la suma")
        return False

    # 2. Conmutatividad de la suma
    if suma_vectorial(v1, v2) != suma_vectorial(v2, v1):
        print("Falló la conmutatividad de la suma")
        return False

    # 3. Asociatividad de la suma
    if suma_vectorial(v1, suma_vectorial(v2, v3)) != suma_vectorial(suma_vectorial(v1, v2), v3):
        print("Falló la asociatividad de la suma")
        return False

    # 4. Existencia del elemento neutro
    if suma_vectorial(v1, v0) != v0:
        print("Falló la existencia del elemento neutro")
        return False

    # 5. Existencia del elemento opuesto
    if suma_vectorial(v1, v1) != v0:
        print("Falló la existencia del elemento opuesto")
        return False

    # 6. Cerradura bajo la multiplicación por un escalar
    if multiplicacion_escalar(c, v1) is None:
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    # 7. Distributividad de la multiplicación escalar respecto a la suma vectorial
    if multiplicacion_escalar(c, suma_vectorial(v1, v2)) != suma_vectorial(multiplicacion_escalar(c, v1), multiplicacion_escalar(c, v2)):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma vectorial")
        return False

    # 8. Distributividad de la multiplicación escalar respecto a la suma escalar
    if multiplicacion_escalar(c + d, v1) != suma_vectorial(multiplicacion_escalar(c, v1), multiplicacion_escalar(d, v1)):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma escalar")
        return False

    # 9. Asociatividad de la multiplicación escalar
    if multiplicacion_escalar(c * d, v1) != multiplicacion_escalar(c, multiplicacion_escalar(d, v1)):
        print("Falló la asociatividad de la multiplicación escalar")
        return False

    # 10. Existencia del elemento unidad
    if multiplicacion_escalar(1, v1) != v1:
        print("Falló la existencia del elemento unidad")
        return False

    return True

# Ejecutar la verificación  
print(es_espacio_vectorial())  # Debería imprimir True o False


###SubEspacio Vectorial

##Ejercicio 1
import sympy as sp

def suma_vectorial(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2], v1[3] + v2[3])

def multiplicacion_escalar(c, v):
    return (c * v[0], c * v[1], c * v[2], c * v[3])

def es_subespacio_vectorial():
    # Definir variables simbólicas
    x1, y1, z1, w1 = sp.symbols('x1 y1 z1 w1')
    x2, y2, z2, w2 = sp.symbols('x2 y2 z2 w2')
    c = sp.symbols('c')

    # Vectores en W
    v1 = (x1, y1, z1, 0)
    v2 = (x2, y2, z2, 0)
    v0 = (0, 0, 0, 0)

    # 1. Cerradura bajo la suma
    suma_v1_v2 = suma_vectorial(v1, v2)
    if suma_v1_v2[3] != 0:
        print("Falló la cerradura bajo la suma")
        return False

    # 2. Cerradura bajo la multiplicación por un escalar
    escalar_v1 = multiplicacion_escalar(c, v1)
    if escalar_v1[3] != 0:
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    # 3. Contiene el vector cero
    if v0 not in [v1, v2]:
        print("No contiene el vector cero")
        return False

    return True

# Ejecutar la verificación
print(es_subespacio_vectorial())  # Debería imprimir True o False

##Ejerccio 2
import sympy as sp

def suma_vectorial(v1, v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return (x1 + x2, y1 + y2, (2 * (x1 + x2)) - (3 * (y1 + y2)))

def multiplicacion_escalar(c, v):
    x, y, z = v
    return (c * x, c * y, c * (2 * x - 3 * y))

def es_subespacio_vectorial():
    # Definir variables simbólicas
    x1, y1, x2, y2, c = sp.symbols('x1 y1 x2 y2 c')

    # Vectores en W
    v1 = (x1, y1, 2*x1 - 3*y1)
    v2 = (x2, y2, 2*x2 - 3*y2)
    v0 = (0, 0, 0)

    # 1. Cerradura bajo la suma
    suma_v1_v2 = suma_vectorial(v1, v2)
    if suma_v1_v2[2] != 2 * suma_v1_v2[0] - 3 * suma_v1_v2[1]:
        print("Falló la cerradura bajo la suma")
        return False

    # 2. Cerradura bajo la multiplicación por un escalar
    escalar_v1 = multiplicacion_escalar(c, v1)
    if escalar_v1[2] != 2 * escalar_v1[0] - 3 * escalar_v1[1]:
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    # 3. Contiene el vector cero
    if v0 != (0, 0, 2*0 - 3*0):
        print("No contiene el vector cero")
        return False

    return True

# Ejecutar la verificación
print(es_subespacio_vectorial())  # Debería imprimir True o False

##Ejercicio 3
import sympy as sp

def suma_matrices(m1, m2):
    return m1 + m2

def multiplicacion_escalar(c, m):
    return c * m

def es_subespacio_vectorial():
    # Definir variables simbólicas
    a1, b1, a2, b2, c = sp.symbols('a1 b1 a2 b2 c')

    # Matrices en W
    m1 = sp.Matrix([[0, a1], [b1, 0]])
    m2 = sp.Matrix([[0, a2], [b2, 0]])
    m0 = sp.Matrix([[0, 0], [0, 0]])

    # 1. Cerradura bajo la suma
    suma_m1_m2 = suma_matrices(m1, m2)
    if not (suma_m1_m2[0, 0] == 0 and suma_m1_m2[1, 1] == 0):
        print("Falló la cerradura bajo la suma")
        return False

    # 2. Cerradura bajo la multiplicación por un escalar
    escalar_m1 = multiplicacion_escalar(c, m1)
    if not (escalar_m1[0, 0] == 0 and escalar_m1[1, 1] == 0):
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    # 3. Contiene el vector cero
    if m0 != sp.Matrix([[0, 0], [0, 0]]):
        print("No contiene el vector cero")
        return False

    return True

# Ejecutar la verificación
print(es_subespacio_vectorial())  # Debería imprimir True o False

##4 Ejercicio
import sympy as sp

def suma_matrices(m1, m2):
    return m1 + m2

def multiplicacion_escalar(c, m):
    return c * m

def es_subespacio_vectorial():
    # Definir variables simbólicas
    a1, b1, c1, a2, b2, c2, c = sp.symbols('a1 b1 c1 a2 b2 c2 c')

    # Matrices en W
    m1 = sp.Matrix([[a1, b1], [a1 + b1, 0], [0, c1]])
    m2 = sp.Matrix([[a2, b2], [a2 + b2, 0], [0, c2]])
    m0 = sp.Matrix([[0, 0], [0, 0], [0, 0]])

    # 1. Cerradura bajo la suma
    suma_m1_m2 = suma_matrices(m1, m2)
    if not (suma_m1_m2[0, 0] == suma_m1_m2[1, 0] - suma_m1_m2[1, 1] and suma_m1_m2[2, 0] == 0):
        print("Falló la cerradura bajo la suma")
        return False

    # 2. Cerradura bajo la multiplicación por un escalar
    escalar_m1 = multiplicacion_escalar(c, m1)
    if not (escalar_m1[0, 0] == escalar_m1[1, 0] - escalar_m1[1, 1] and escalar_m1[2, 0] == 0):
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    # 3. Contiene el vector cero
    if m0 != sp.Matrix([[0, 0], [0, 0], [0, 0]]):
        print("No contiene el vector cero")
        return False

    return True

# Ejecutar la verificación
print(es_subespacio_vectorial())  # Debería imprimir True o False

#5
import sympy as sp
from sympy.abc import x

def es_continua(f):
    # Si la función no tiene discontinuidades en el intervalo [0, 1]
    return sp.simplify(sp.limit(f, x, 0)) == f.subs(x, 0) and sp.simplify(sp.limit(f, x, 1)) == f.subs(x, 1)

def es_integrable(f):
    # Las funciones continuas son integrables en un intervalo cerrado y acotado
    return True

def es_subespacio_vectorial():
    # Definir funciones simbólicas
    f1 = sp.Function('f1')(x)
    f2 = sp.Function('f2')(x)
    c = sp.symbols('c')

    # 1. Cerradura bajo la suma
    suma_f1_f2 = f1 + f2
    if not es_continua(suma_f1_f2):
        print("Falló la cerradura bajo la suma")
        return False

    # 2. Cerradura bajo la multiplicación por un escalar
    escalar_f1 = c * f1
    if not es_continua(escalar_f1):
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    # 3. Contiene el vector cero
    cero = sp.Function('cero')(x)
    if not es_continua(cero):
        print("No contiene el vector cero")
        return False

    return True

# Ejecutar la verificación
print(es_subespacio_vectorial())  # Debería imprimir True o False

###3.	Combinación Lineal

##Ejercicio 1
import sympy as sp

# Definir los escalares simbólicos
a, b = sp.symbols('a b')

# Definir los vectores de S
v1 = sp.Matrix([2, -1, 3])
v2 = sp.Matrix([5, 0, 4])

# Definir los vectores a verificar
z = sp.Matrix([-1, -2, 2])
v = sp.Matrix([8, -1/4, 27/4])
w = sp.Matrix([1, -8, 12])
u = sp.Matrix([1, 1, -1])

# Función para verificar si un vector es combinación lineal de v1 y v2
def es_combinacion_lineal(vector):
    combinacion_lineal = a * v1 + b * v2
    ecuaciones = [sp.Eq(combinacion_lineal[0], vector[0]), sp.Eq(combinacion_lineal[1], vector[1]), sp.Eq(combinacion_lineal[2], vector[2])]
    solucion = sp.solve(ecuaciones, (a, b))
    return solucion

# Verificar cada vector
solucion_z = es_combinacion_lineal(z)
solucion_v = es_combinacion_lineal(v)
solucion_w = es_combinacion_lineal(w)
solucion_u = es_combinacion_lineal(u)

print("Solución para z = (-1, -2, 2):")
print(solucion_z)

print("Solución para v = (8, -1/4, 27/4):")
print(solucion_v)

print("Solución para w = (1, -8, 12):")
print(solucion_w)

print("Solución para u = (1, 1, -1):")
print(solucion_u)

#Ejercicio 2
import sympy as sp

# Definir los escalares simbólicos
a, b = sp.symbols('a b')

# Definir los vectores de S
v1 = sp.Matrix([1, 2, -2])
v2 = sp.Matrix([2, -1, 1])

# Definir los vectores a verificar
z = sp.Matrix([-4, -3, 3])
v = sp.Matrix([-2, -6, 6])
w = sp.Matrix([-1, -22, 22])
u = sp.Matrix([1, -5, -5])

# Función para verificar si un vector es combinación lineal de v1 y v2
def es_combinacion_lineal(vector):
    combinacion_lineal = a * v1 + b * v2
    ecuaciones = [sp.Eq(combinacion_lineal[0], vector[0]), sp.Eq(combinacion_lineal[1], vector[1]), sp.Eq(combinacion_lineal[2], vector[2])]
    solucion = sp.solve(ecuaciones, (a, b))
    return solucion

# Verificar cada vector
solucion_z = es_combinacion_lineal(z)
solucion_v = es_combinacion_lineal(v)
solucion_w = es_combinacion_lineal(w)
solucion_u = es_combinacion_lineal(u)

print("Solución para z = (-4, -3, 3):")
print(solucion_z)

print("Solución para v = (-2, -6, 6):")
print(solucion_v)

print("Solución para w = (-1, -22, 22):")
print(solucion_w)

print("Solución para u = (1, -5, -5):")
print(solucion_u)

##Ejercici 3
import sympy as sp

# Definir los escalares simbólicos
a, b, c = sp.symbols('a b c')

# Definir los vectores de S
v1 = sp.Matrix([2, 0, 7])
v2 = sp.Matrix([2, 4, 5])
v3 = sp.Matrix([2, -12, 13])

# Definir los vectores a verificar
u = sp.Matrix([-1, 5, -6])
v = sp.Matrix([-3, 15, 18])
w = sp.Matrix([1/3, 4/3, 1/2])
z = sp.Matrix([2, 20, -3])

# Función para verificar si un vector es combinación lineal de v1, v2 y v3
def es_combinacion_lineal(vector):
    combinacion_lineal = a * v1 + b * v2 + c * v3
    ecuaciones = [sp.Eq(combinacion_lineal[0], vector[0]), sp.Eq(combinacion_lineal[1], vector[1]), sp.Eq(combinacion_lineal[2], vector[2])]
    solucion = sp.solve(ecuaciones, (a, b, c))
    return solucion

# Verificar cada vector
solucion_u = es_combinacion_lineal(u)
solucion_v = es_combinacion_lineal(v)
solucion_w = es_combinacion_lineal(w)
solucion_z = es_combinacion_lineal(z)

print("Solución para u = (-1, 5, -6):")
print(solucion_u)

print("Solución para v = (-3, 15, 18):")
print(solucion_v)

print("Solución para w = (1/3, 4/3, 1/2):")
print(solucion_w)

print("Solución para z = (2, 20, -3):")
print(solucion_z)

##Ejercicio 4

import sympy as sp

# Definir los escalares simbólicos
a, b = sp.symbols('a b')

# Definir los vectores de S
v1 = sp.Matrix([6, -7, 8, 6])
v2 = sp.Matrix([4, 6, -4, 1])

# Definir los vectores a verificar
u = sp.Matrix([-42, 113, -112, -60])
v = sp.Matrix([49/2, 99/4, -14, 19/2])
w = sp.Matrix([-4, -14, 27/2, 53/8])
z = sp.Matrix([8, 4, -1, 17/4])

# Función para verificar si un vector es combinación lineal de v1 y v2
def es_combinacion_lineal(vector):
    combinacion_lineal = a * v1 + b * v2
    ecuaciones = [sp.Eq(combinacion_lineal[0], vector[0]), sp.Eq(combinacion_lineal[1], vector[1]), sp.Eq(combinacion_lineal[2], vector[2]), sp.Eq(combinacion_lineal[3], vector[3])]
    solucion = sp.solve(ecuaciones, (a, b))
    return solucion

# Verificar cada vector
solucion_u = es_combinacion_lineal(u)
solucion_v = es_combinacion_lineal(v)
solucion_w = es_combinacion_lineal(w)
solucion_z = es_combinacion_lineal(z)

print("Solución para u = (-42, 113, -112, -60):")
print(solucion_u)

print("Solución para v = (49/2, 99/4, -14, 19/2):")
print(solucion_v)

print("Solución para w = (-4, -14, 27/2, 53/8):")
print(solucion_w)

print("Solución para z = (8, 4, -1, 17/4):")
print(solucion_z)

##Ejercicio 5 
import numpy as np

# Definir las matrices A y B
A = np.array([[2, -3], [4, 1]])
B = np.array([[0, 5], [1, -2]])

# Definir las matrices C5, C6, C7 y C8
C5 = np.array([[6, -19], [10, 7]])
C6 = np.array([[6, 2], [9, 11]])
C7 = np.array([[-2, 28], [1, -11]])
C8 = np.array([[0, 0], [0, 0]])

# Función para comprobar si una matriz es una combinación lineal de A y B
def es_combinacion_lineal(A, B, C):
    # Reestructurar las matrices para crear un sistema de ecuaciones lineales
    AB = np.hstack((A.reshape(-1, 1), B.reshape(-1, 1)))
    C_plano = C.reshape(-1, 1)
    
    # Resolver el sistema de ecuaciones
    try:
        coeficientes = np.linalg.solve(AB, C_plano)
        return True, coeficientes.flatten()
    except np.linalg.LinAlgError:
        return False, None

# Comprobar cada matriz
resultados = {}
for i, C in enumerate([C5, C6, C7, C8], start=5):
    es_comb, coeficientes = es_combinacion_lineal(A, B, C)
    resultados[f"C{i}"] = (es_comb, coeficientes)

# Imprimir resultados
for matriz, (es_comb, coeficientes) in resultados.items():
    if es_comb:
        print(f"{matriz} es una combinación lineal de A y B con coeficientes: {coeficientes}")
    else:
        print(f"{matriz} no es una combinación lineal de A y B")


##4.	Independencia Lineal

#Ejercicio 1
import numpy as np

# Definir los vectores
v1 = np.array([-2, 2])
v2 = np.array([3, 5])

# Crear la matriz con estos vectores como filas
matriz = np.array([v1, v2])

# Calcular el determinante
det = np.linalg.det(matriz)

# Verificar si el determinante es cero
if det == 0:
    print("El conjunto S es linealmente dependiente.")
else:
    print("El conjunto S es linealmente independiente.")

#Ejercicio 2
import numpy as np

# Definir los vectores
v1 = np.array([3, -6])
v2 = np.array([-1, 2])

# Crear la matriz con estos vectores como filas
matriz = np.array([v1, v2])

# Calcular el determinante
det = np.linalg.det(matriz)

# Verificar si el determinante es cero
if det == 0:
    print("El conjunto S es linealmente dependiente.")
else:
    print("El conjunto S es linealmente independiente.")


#Ejercicio 3
import numpy as np

# Definir los vectores
v1 = np.array([0, 0])
v2 = np.array([1, -1])

# Crear la matriz con estos vectores como filas
matriz = np.array([v1, v2])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Verificar si el rango es menor que el número de vectores
if rango < len(matriz):
    print("El conjunto S es linealmente dependiente.")
else:
    print("El conjunto S es linealmente independiente.")


#Ejercicio 4

import numpy as np

# Definir los vectores
v1 = np.array([1, 0])
v2 = np.array([1, 1])
v3 = np.array([2, -1])

# Crear la matriz con estos vectores como filas
matriz = np.array([v1, v2, v3])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Verificar si el rango es menor que el número de vectores
if rango < len(matriz):
    print("El conjunto S es linealmente dependiente.")
else:
    print("El conjunto S es linealmente independiente.")


#Ejercicio 5
import numpy as np

# Definir los vectores
v1 = np.array([1, -4, 1])
v2 = np.array([6, 3, 2])

# Crear la matriz con estos vectores como filas
matriz = np.array([v1, v2])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Verificar si el rango es menor que el número de vectores
if rango < len(matriz):
    print("El conjunto S es linealmente dependiente.")
else:
    print("El conjunto S es linealmente independiente.")


##5.	Base y Dimensión

#Ejercicio 1

import numpy as np

# Definir los vectores
v1 = np.array([1, 3])
v2 = np.array([1, -1])

# Crear la matriz con estos vectores como columnas
matriz = np.column_stack([v1, v2])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Imprimir la base y la dimensión
print("Base:", [v1, v2])
print("Dimensión:", rango)

#Ejercicio 2

import numpy as np

# Definir los vectores
v1 = np.array([0, 0])
v2 = np.array([1, 2])
v3 = np.array([2, 4])

# Crear la matriz con estos vectores como columnas
matriz = np.column_stack([v1, v2, v3])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Obtener la base (vectores linealmente independientes)
base = [v2, v3] if rango == 2 else [v2]

# Imprimir la base y la dimensión
print("Base:", base)
print("Dimensión:", rango)

#Ejercicio 3

import numpy as np

# Definir los vectores
v1 = np.array([1, 2])
v2 = np.array([2, -3])
v3 = np.array([3, 2])

# Crear la matriz con estos vectores como columnas
matriz = np.column_stack([v1, v2, v3])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Obtener la base (vectores linealmente independientes)
if rango == 3:
    base = [v1, v2, v3]
elif rango == 2:
    base = [v1, v2] if np.linalg.matrix_rank(np.column_stack([v1, v2])) == 2 else [v1, v3]
else:
    base = [v1]

# Imprimir la base y la dimensión
print("Base:", base)
print("Dimensión:", rango)

#Ejercicio 4

import numpy as np

# Definir los vectores
v1 = np.array([1, 3])
v2 = np.array([-2, 6])

# Crear la matriz con estos vectores como columnas
matriz = np.column_stack([v1, v2])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Obtener la base (vectores linealmente independientes)
base = [v1, v2] if rango == 2 else [v1]

# Imprimir la base y la dimensión
print("Base:", base)
print("Dimensión:", rango)


#Ejercicio 5

import numpy as np

# Definir los vectores
v1 = np.array([1, 2, 0])
v2 = np.array([0, 1, -1])

# Crear la matriz con estos vectores como columnas
matriz = np.column_stack([v1, v2])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Imprimir la base y la dimensión
print("Base:", [v1, v2])
print("Dimensión:", rango)


##6.	Rango e Imagen de una Matriz

#Ejercicio 1 

import numpy as np

# Definir la matriz
matriz = np.array([[2, 4], [1, 6]])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Obtener la imagen de la matriz (columnas linealmente independientes)
_, columnas_independientes = np.linalg.qr(matriz)

# Imprimir el rango y la imagen de la matriz
print("Rango:", rango)
print("Imagen de la matriz:", columnas_independientes)

#Ejercicio 2

import numpy as np

# Definir la matriz
matriz = np.array([[1, 2, 3]])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Obtener la imagen de la matriz (columnas linealmente independientes)
_, columnas_independientes = np.linalg.qr(matriz)

# Imprimir el rango y la imagen de la matriz
print("Rango:", rango)
print("Imagen de la matriz:", columnas_independientes)


#Ejercicio 3

import numpy as np

# Definir la matriz
matriz = np.array([[-1, 2, 4], [-1, 2, 1]])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Obtener la imagen de la matriz (columnas linealmente independientes)
_, columnas_independientes = np.linalg.qr(matriz)

# Imprimir el rango y la imagen de la matriz
print("Rango:", rango)
print("Imagen de la matriz:", columnas_independientes)

#Ejercicio 4
import numpy as np

# Definir la matriz
matriz = np.array([[4, 20, 31], [6, -5, -6], [2, -11, -16]])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Obtener la imagen de la matriz (columnas linealmente independientes)
_, columnas_independientes = np.linalg.qr(matriz)

# Imprimir el rango y la imagen de la matriz
print("Rango:", rango)
print("Imagen de la matriz:", columnas_independientes)

#Ejercicio 5
import numpy as np

# Definir la matriz
matriz = np.array([[2, 4, -3, -6], [7, 14, -6, -3], [-2, -4, 1, -2], [2, 4, -2, -2]])

# Calcular el rango de la matriz
rango = np.linalg.matrix_rank(matriz)

# Obtener la imagen de la matriz (columnas linealmente independientes)
_, columnas_independientes = np.linalg.qr(matriz)

# Imprimir el rango y la imagen de la matriz
print("Rango:", rango)
print("Imagen de la matriz:", columnas_independientes)


##7.	Cambio de Base
#Ejercicio 1
import numpy as np

# Definir la base B
B = np.array([[2, 0], [-1, 1]])

# Definir el vector de coordenadas en la base B
x_B = np.array([4, 1])

# Convertir a la base estándar
x_estandar = np.dot(B, x_B)

# Imprimir el vector en la base estándar
print("Vector en la base estándar:", x_estandar)

#Ejercicio 2
import numpy as np

# Definir la base B
B = np.array([[-1, 4], [4, -1]])

# Definir el vector de coordenadas en la base B
x_B = np.array([-2, 3])

# Convertir a la base estándar
x_estandar = np.dot(B, x_B)

# Imprimir el vector en la base estándar
print("Vector en la base estándar:", x_estandar)

#Ejercicio 3
import numpy as np

# Definir la base B
B = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1]])

# Definir el vector de coordenadas en la base B
x_B = np.array([2, 3, 1])

# Convertir a la base estándar
x_estandar = np.dot(B, x_B)

# Imprimir el vector en la base estándar
print("Vector en la base estándar:", x_estandar)

#Ejercicio 4

import numpy as np

# Definir la base B
B = np.array([[3/4, 3, -3/2], [5/2, 4, 6], [0, 7/2, 2]])

# Definir el vector de coordenadas en la base B
x_B = np.array([2, 0, 4])

# Convertir a la base estándar
x_estandar = np.dot(B, x_B)

# Imprimir el vector en la base estándar
print("Vector en la base estándar:", x_estandar)


#Ejercicio 5
import numpy as np

# Definir la base B
B = np.array([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]])

# Definir el vector de coordenadas en la base B
x_B = np.array([-1, -2, -3, -1])

# Convertir a la base estándar
x_estandar = np.dot(B, x_B)

# Imprimir el vector en la base estándar
print("Vector en la base estándar:", x_estandar)

##8.	Transformación Lineal
#Ejercicio 1
import numpy as np

def L_a(v):
    x, y = v
    return np.array([x + y, x - y])

def es_transformacion_lineal(L, dimension):
    # Comprobar aditividad
    u = np.random.rand(dimension)
    v = np.random.rand(dimension)
    if not np.allclose(L(u + v), L(u) + L(v)):
        return False
    
    # Comprobar homogeneidad
    c = np.random.rand()
    if not np.allclose(L(c * u), c * L(u)):
        return False
    
    return True

# Verificar si es transformación lineal
print("L(x, y) = (x + y, x - y) es transformación lineal:", es_transformacion_lineal(L_a, 2))

#Ejercicio 2
import numpy as np

# Definir la función que verifica si una transformación es lineal
def es_transformacion_lineal(L, dimension):
    # Comprobar aditividad
    u = np.random.rand(dimension)
    v = np.random.rand(dimension)
    if not np.allclose(L(u + v), L(u) + L(v)):
        return False
    
    # Comprobar homogeneidad
    c = np.random.rand()
    if not np.allclose(L(c * u), c * L(u)):
        return False
    
    return True

# Definir la transformación L
def L_b(v):
    x, y, z = v
    return np.array([x + 1, y - z])

# Verificar si es transformación lineal
es_lineal = es_transformacion_lineal(L_b, 3)
print(f"L([x, y, z]^T) = [x + 1, y - z]^T es transformación lineal: {es_lineal}")

#Ejercicio 3

import numpy as np

def es_transformacion_lineal(L, dimension):
    # Comprobar aditividad
    u = np.random.rand(dimension)
    v = np.random.rand(dimension)
    if not np.allclose(L(u + v), L(u) + L(v)):
        return False
    
    # Comprobar homogeneidad
    c = np.random.rand()
    if not np.allclose(L(c * u), c * L(u)):
        return False
    
    return True

def L_c(v):
    matriz = np.array([[1, 2, 3], [-1, 2, 4]])
    return np.dot(matriz, v)

# Verificar si es transformación lineal
es_lineal = es_transformacion_lineal(L_c, 3)
print(f"L([x, y, z]^T) = [1 2 3; -1 2 4][x, y, z]^T es transformación lineal: {es_lineal}")


#Ejercicio 4
import numpy as np

def es_transformacion_lineal(L, dimension):
    # Comprobar aditividad
    u = np.random.rand(dimension)
    v = np.random.rand(dimension)
    if not np.allclose(L(u + v), L(u) + L(v)):
        return False
    
    # Comprobar homogeneidad
    c = np.random.rand()
    if not np.allclose(L(c * u), c * L(u)):
        return False
    
    return True

def L_a_extra(v):
    return np.array([0, 0])

# Verificar si es transformación lineal
es_lineal = es_transformacion_lineal(L_a_extra, 3)
print(f"L(x, y, z) = (0, 0) es transformación lineal: {es_lineal}")

#Ejercicio 5
import numpy as np

def es_transformacion_lineal(L, dimension):
    # Comprobar aditividad
    u = np.random.rand(dimension)
    v = np.random.rand(dimension)
    if not np.allclose(L(u + v), L(u) + L(v)):
        return False
    
    # Comprobar homogeneidad
    c = np.random.rand()
    if not np.allclose(L(c * u), c * L(u)):
        return False
    
    return True

def L_b_extra(v):
    return np.array([1, 2, -1])

# Verificar si es transformación lineal
es_lineal = es_transformacion_lineal(L_b_extra, 3)
print(f"L(x, y, z) = (1, 2, -1) es transformación lineal: {es_lineal}")
