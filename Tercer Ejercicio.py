#3. En España cada persona está identificada con un Documento Nacional de Identidad
# (DNI) en el que figura un número y una letra, por ejemplo 56999545W
# La letra que sigue al número se calcula siguiendo la metodología que vamos a
# indicar. Crea un programa que calcule la letra de un DNI a partir del número de DNI
# que introduzca el usuario. Es decir, se debe pedir el DNI completo por teclado y el
# programa nos devolverá si el DNI es válido o inválido.
# Para calcular la letra, se debe tomar el resto de dividir (módulo de la división)
# nuestro número de DNI entre 23. El resultado debe estar por tanto entre 0 y 22.
# Crea un método validarDNI(dni) donde según el resultado de la anterior fórmula
# busque en un array de caracteres la posición que corresponda a la letra y valide si
# el dni es válido o no, deberá retornar true o false, tener en cuenta que el DNI
# finaliza siempre con una letra si no es así el DNI es inválido. Esta es la tabla de
# caracteres:
# Posición 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
# Letra    T R W A G M Y F P D  X B  N  J  Z  S  Q  V  H  L  C  K  E
# Por ejemplo, si introducimos el DNI 20267079Q, el resto de dividirlo por 23 sería 8,
# luego la letra sería la P, que es la que ocupa esa posición en la matriz de
# caracteres, por tanto ese DNI es inválido. Si introducimos el DNI 12378459C, el
# resto de dividirlo por 23 sería 20, luego la letra sería la C por tanto el DNI es válido.
# Si ingresamos el DNI A12345678, es inválido como lo es 123456789, ya que inician
# por letra o finalizan con un número y no una letra.
def validarDNI(Cod_DNI):
    try: 
        int(Cod_DNI[:-1])
        Let_DNI =Cod_DNI[len(Cod_DNI)-1]
        Num_DNI=int(Cod_DNI[:-1])
        resto=Num_DNI % 23
        Lista_Letras =['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
        if (Lista_Letras[resto]==Let_DNI) : return 'Válido'
        return 'inválido'
    except ValueError:
        return 'Invalido'