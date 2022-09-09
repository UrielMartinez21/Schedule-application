#---------------------- Sub-funciones ----------------------

# Cantidad de dias para hacer la consulta
def Cantidad_Dias(NumeroDias):
    Dias = []
    Horas = []
    for valor in range(NumeroDias):
        dia = input(f"\tDia {valor+1}: ")
        hora = input(f"\tHora {valor+1}: ")
        Dias.append(dia)
        Horas.append(hora)
    return Dias,Horas 


# Acorde a la cantidad de dias hara la consulta
def Opcion_Dias(tabla_excel,opcionDias,Dias,Horas):
    if opcionDias==1:
        resultado = tabla_excel[
            (tabla_excel[Dias[0]] == Horas[0])
            ]
        print(resultado[["Grupo","Asignatura","Profesor","Lun","Mar","Mie","Jue","Vie"]])

    if opcionDias==2:
        resultado = tabla_excel[
            (tabla_excel[Dias[0]] == Horas[0]) &
            (tabla_excel[Dias[1]] == Horas[1])
            ]
        print(resultado[["Grupo","Asignatura","Profesor","Lun","Mar","Mie","Jue","Vie"]])

    if opcionDias == 3:
        resultado = tabla_excel[
            (tabla_excel[Dias[0]] == Horas[0]) &
            (tabla_excel[Dias[1]] == Horas[1]) &
            (tabla_excel[Dias[2]] == Horas[2])
            ]
        print(resultado[["Grupo","Asignatura","Profesor","Lun","Mar","Mie","Jue","Vie"]])

#---------------------- Funcion para exportar ----------------------

def Consultar_Dias(tabla_excel,NumeroDias):
    dias,horas=Cantidad_Dias(NumeroDias)
    Opcion_Dias(tabla_excel,NumeroDias,dias,horas)