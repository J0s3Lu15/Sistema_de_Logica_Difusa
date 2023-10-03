import numpy as np
from colorama import Fore, Back, Style, init
import sys
import time
import skfuzzy as fuzz
from skfuzzy import control as ctrl

init()

# Definir las variables difusas

semestre = ctrl.Antecedent(np.arange(1, 9, 1), 'semestre')
materias_inscrito = ctrl.Antecedent(np.arange(1, 9, 1), 'materias_inscrito')
materias_recursando = ctrl.Antecedent(np.arange(0, 5, 1), 'materias_recursando')
trabaja = ctrl.Antecedent(np.arange(0, 2, 1), 'trabaja')
dar_de_baja = ctrl.Consequent(np.arange(0, 8, 1), 'dar_de_baja')

# Definir las funciones de membresía

semestre['bajo'] = fuzz.trimf(semestre.universe, [1, 1, 4])
semestre['medio'] = fuzz.trimf(semestre.universe, [4, 4, 7])
semestre['alto'] = fuzz.trimf(semestre.universe, [6, 8, 9])

materias_inscrito['pocas'] = fuzz.trimf(materias_inscrito.universe, [1, 1, 4])
materias_inscrito['medio'] = fuzz.trimf(materias_inscrito.universe, [4, 4, 7])
materias_inscrito['muchas'] = fuzz.trimf(materias_inscrito.universe, [6, 8, 9])

materias_recursando.automf(3)

dar_de_baja.automf(3)
dar_de_baja['ninguna'] = fuzz.trimf(dar_de_baja.universe, [0, 0, 0])

trabaja['no'] = fuzz.trimf(trabaja.universe, [0, 0, 0])
trabaja['si'] = fuzz.trimf(trabaja.universe, [1, 1, 1])

# Definir las reglas difusas

regla1 = ctrl.Rule(semestre['bajo'] & materias_inscrito['pocas'] &
                   materias_recursando['poor'] & trabaja['si'], dar_de_baja['ninguna'])

regla2 = ctrl.Rule(semestre['bajo'] & materias_inscrito['pocas'] &
                   materias_recursando['poor'] & trabaja['no'], dar_de_baja['ninguna'])

regla3 = ctrl.Rule(semestre['bajo'] & materias_inscrito['pocas'] &
                   materias_recursando['average'] & trabaja['si'], dar_de_baja['ninguna'])

regla4 = ctrl.Rule(semestre['bajo'] & materias_inscrito['pocas'] &
                   materias_recursando['average'] & trabaja['no'], dar_de_baja['ninguna'])

regla5 = ctrl.Rule(semestre['bajo'] & materias_inscrito['pocas'] &
                   materias_recursando['good'] & trabaja['si'], dar_de_baja['poor'])

regla6 = ctrl.Rule(semestre['bajo'] & materias_inscrito['pocas'] &
                   materias_recursando['good'] & trabaja['no'], dar_de_baja['ninguna'])

regla7 = ctrl.Rule(semestre['bajo'] & materias_inscrito['medio'] &
                   materias_recursando['poor'] & trabaja['si'], dar_de_baja['ninguna'])

regla8 = ctrl.Rule(semestre['bajo'] & materias_inscrito['medio'] &
                   materias_recursando['poor'] & trabaja['no'], dar_de_baja['ninguna'])

regla9 = ctrl.Rule(semestre['bajo'] & materias_inscrito['medio'] &
                   materias_recursando['average'] & trabaja['si'], dar_de_baja['poor'])

regla10 = ctrl.Rule(semestre['bajo'] & materias_inscrito['medio'] &
                    materias_recursando['average'] & trabaja['no'], dar_de_baja['ninguna'])

regla11 = ctrl.Rule(semestre['bajo'] & materias_inscrito['medio'] &
                    materias_recursando['good'] & trabaja['si'], dar_de_baja['average'])

regla12 = ctrl.Rule(semestre['bajo'] & materias_inscrito['medio'] &
                    materias_recursando['good'] & trabaja['no'], dar_de_baja['poor'])

regla13 = ctrl.Rule(semestre['bajo'] & materias_inscrito['muchas'] &
                    materias_recursando['poor'] & trabaja['si'], dar_de_baja['average'])

regla14 = ctrl.Rule(semestre['bajo'] & materias_inscrito['muchas'] &
                    materias_recursando['poor'] & trabaja['no'], dar_de_baja['poor'])

regla15 = ctrl.Rule(semestre['bajo'] & materias_inscrito['muchas'] &
                    materias_recursando['average'] & trabaja['si'], dar_de_baja['average'])

regla16 = ctrl.Rule(semestre['bajo'] & materias_inscrito['muchas'] &
                    materias_recursando['average'] & trabaja['no'], dar_de_baja['average'])

regla17 = ctrl.Rule(semestre['bajo'] & materias_inscrito['muchas'] &
                    materias_recursando['good'] & trabaja['si'], dar_de_baja['good'])

regla18 = ctrl.Rule(semestre['bajo'] & materias_inscrito['muchas'] &
                    materias_recursando['good'] & trabaja['no'], dar_de_baja['good'])

regla19 = ctrl.Rule(semestre['medio'] & materias_inscrito['pocas'] &
                    materias_recursando['poor'] & trabaja['si'], dar_de_baja['ninguna'])

regla20 = ctrl.Rule(semestre['medio'] & materias_inscrito['pocas'] &
                    materias_recursando['poor'] & trabaja['no'], dar_de_baja['ninguna'])

regla21 = ctrl.Rule(semestre['medio'] & materias_inscrito['pocas'] &
                    materias_recursando['average'] & trabaja['si'], dar_de_baja['ninguna'])

regla22 = ctrl.Rule(semestre['medio'] & materias_inscrito['pocas'] &
                    materias_recursando['average'] & trabaja['no'], dar_de_baja['ninguna'])

regla23 = ctrl.Rule(semestre['medio'] & materias_inscrito['pocas'] &
                    materias_recursando['good'] & trabaja['si'], dar_de_baja['poor'])

regla24 = ctrl.Rule(semestre['medio'] & materias_inscrito['pocas'] &
                    materias_recursando['good'] & trabaja['no'], dar_de_baja['poor'])

regla25 = ctrl.Rule(semestre['medio'] & materias_inscrito['medio'] &
                    materias_recursando['poor'] & trabaja['si'], dar_de_baja['ninguna'])

regla26 = ctrl.Rule(semestre['medio'] & materias_inscrito['medio'] &
                    materias_recursando['poor'] & trabaja['no'], dar_de_baja['ninguna'])

regla27 = ctrl.Rule(semestre['medio'] & materias_inscrito['medio'] &
                    materias_recursando['average'] & trabaja['si'], dar_de_baja['average'])

regla28 = ctrl.Rule(semestre['medio'] & materias_inscrito['medio'] &
                    materias_recursando['average'] & trabaja['no'], dar_de_baja['poor'])

regla29 = ctrl.Rule(semestre['medio'] & materias_inscrito['medio'] &
                    materias_recursando['good'] & trabaja['si'], dar_de_baja['good'])

regla30 = ctrl.Rule(semestre['medio'] & materias_inscrito['medio'] &
                    materias_recursando['good'] & trabaja['no'], dar_de_baja['poor'])

regla31 = ctrl.Rule(semestre['medio'] & materias_inscrito['muchas'] &
                    materias_recursando['poor'] & trabaja['si'], dar_de_baja['poor'])

regla32 = ctrl.Rule(semestre['medio'] & materias_inscrito['muchas'] &
                    materias_recursando['poor'] & trabaja['no'], dar_de_baja['ninguna'])

regla33 = ctrl.Rule(semestre['medio'] & materias_inscrito['muchas'] &
                    materias_recursando['average'] & trabaja['si'], dar_de_baja['good'])

regla34 = ctrl.Rule(semestre['medio'] & materias_inscrito['muchas'] &
                    materias_recursando['average'] & trabaja['no'], dar_de_baja['poor'])

regla35 = ctrl.Rule(semestre['medio'] & materias_inscrito['muchas'] &
                    materias_recursando['good'] & trabaja['si'], dar_de_baja['good'])

regla36 = ctrl.Rule(semestre['medio'] & materias_inscrito['muchas'] &
                    materias_recursando['good'] & trabaja['no'], dar_de_baja['good'])

regla37 = ctrl.Rule(semestre['alto'] & materias_inscrito['pocas'] &
                    materias_recursando['poor'] & trabaja['si'], dar_de_baja['ninguna'])

regla38 = ctrl.Rule(semestre['alto'] & materias_inscrito['pocas'] &
                    materias_recursando['poor'] & trabaja['no'], dar_de_baja['ninguna'])

regla39 = ctrl.Rule(semestre['alto'] & materias_inscrito['pocas'] &
                    materias_recursando['average'] & trabaja['si'], dar_de_baja['ninguna'])

regla40 = ctrl.Rule(semestre['alto'] & materias_inscrito['pocas'] &
                    materias_recursando['average'] & trabaja['no'], dar_de_baja['ninguna'])

regla41 = ctrl.Rule(semestre['alto'] & materias_inscrito['pocas'] &
                    materias_recursando['good'] & trabaja['si'], dar_de_baja['poor'])

regla42 = ctrl.Rule(semestre['alto'] & materias_inscrito['pocas'] &
                    materias_recursando['good'] & trabaja['no'], dar_de_baja['ninguna'])

regla43 = ctrl.Rule(semestre['alto'] & materias_inscrito['medio'] &
                    materias_recursando['poor'] & trabaja['si'], dar_de_baja['ninguna'])

regla44 = ctrl.Rule(semestre['alto'] & materias_inscrito['medio'] &
                    materias_recursando['poor'] & trabaja['no'], dar_de_baja['ninguna'])

regla45 = ctrl.Rule(semestre['alto'] & materias_inscrito['medio'] &
                    materias_recursando['average'] & trabaja['si'], dar_de_baja['average'])

regla46 = ctrl.Rule(semestre['alto'] & materias_inscrito['medio'] &
                    materias_recursando['average'] & trabaja['no'], dar_de_baja['poor'])

regla47 = ctrl.Rule(semestre['alto'] & materias_inscrito['medio'] &
                    materias_recursando['good'] & trabaja['si'], dar_de_baja['average'])

regla48 = ctrl.Rule(semestre['alto'] & materias_inscrito['medio'] &
                    materias_recursando['good'] & trabaja['no'], dar_de_baja['poor'])

regla49 = ctrl.Rule(semestre['alto'] & materias_inscrito['muchas'] &
                    materias_recursando['poor'] & trabaja['si'], dar_de_baja['average'])

regla50 = ctrl.Rule(semestre['alto'] & materias_inscrito['muchas'] &
                    materias_recursando['poor'] & trabaja['no'], dar_de_baja['poor'])

regla51 = ctrl.Rule(semestre['alto'] & materias_inscrito['muchas'] &
                    materias_recursando['average'] & trabaja['si'], dar_de_baja['average'])

regla52 = ctrl.Rule(semestre['alto'] & materias_inscrito['muchas'] &
                    materias_recursando['average'] & trabaja['no'], dar_de_baja['average'])

regla53 = ctrl.Rule(semestre['alto'] & materias_inscrito['muchas'] &
                    materias_recursando['good'] & trabaja['si'], dar_de_baja['good'])

regla54 = ctrl.Rule(semestre['alto'] & materias_inscrito['muchas'] &
                    materias_recursando['good'] & trabaja['no'], dar_de_baja['good'])

# Crear el sistema de control difuso

tutor_academico = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9, regla10, regla11, regla12, regla13, regla14, regla15, regla16, regla17, regla18, regla19, regla20, regla21, regla22, regla23, regla24, regla25, regla26, regla27, regla28, regla29, regla30, regla31, regla32, regla33, regla34, regla35, regla36, regla37, regla38, regla39, regla40, regla41, regla42, regla43, regla44, regla45, regla46, regla47, regla48, regla49, regla50, regla51, regla52, regla53, regla54])

# Crear el simulador

simulador = ctrl.ControlSystemSimulation(tutor_academico)

# Solicitar la entrada del usuario y validar
banner = '''
  _____      _                       _                 _   __           _           
 |_   _|   _| |_ ___  _ __          / \   ___ __ _  __| | /_/ _ __ ___ (_) ___ ___  
   | || | | | __/ _ \| '__| ____   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __/ _ \ 
   | || |_| | || (_) | |   |____| / ___ \ (_| (_| | (_| |  __/ | | | | | | (_| (_) |
   |_| \__,_|\__\___/|_|         /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___\___/ 
   ---------------------------By - José Luis Flores Tito----------------------------
   ---------------------------------------------------------------------------------
   El siguiente tutor académico te ayudara a tener un desempeño mas optimo en la
   universidad, porfavor responda las siguientes preguntas para recibir una
   recomendación acorde a su situación: 
'''                                                                                                                                                                    
print (Style.BRIGHT + Fore.CYAN + banner)

#Validador de entradas

while True:
    try:
        semestre_input = int(input("Ingresa tu semestre (1-8): "))
        if 1 <= semestre_input <= 8:
            break
        else:
            print("El semestre debe estar entre 1 y 8. Inténtalo de nuevo.")
    except ValueError:
        print("Ingresa un número válido para el semestre.")

while True:
    try:
        materias_inscrito_input = int(input("Ingresa la cantidad de materias inscritas (1-8): "))
        if 1 <= materias_inscrito_input <= 8:
            break
        else:
            print("La cantidad de materias inscritas debe estar entre 1 y 8. Inténtalo de nuevo.")
    except ValueError:
        print("Ingresa un número válido para la cantidad de materias inscritas.")

while True:
    try:
        materias_recursando_input = int(input("Ingresa la cantidad de materias que estás recursando (0-4): "))
        if 0 <= materias_recursando_input <= 4:
            break
        else:
            print("La cantidad de materias recursando debe estar entre 0 y 4. Inténtalo de nuevo.")
    except ValueError:
        print("Ingresa un número válido para la cantidad de materias recursando.")

while True:
    trabaja_input = input("¿Trabajas? (si/no): ").lower()
    if trabaja_input in ['si', 'no']:
        break
    else:
        print("Por favor, responde 'si' o 'no'. Inténtalo de nuevo.")

if trabaja_input == 'si':
    trabaja_input = int(1)
elif trabaja_input == 'no':
    trabaja_input = int(0)
else:
    print("Datos invalidos")

# Configurar las entradas en el simulador

simulador.input['semestre'] = semestre_input
simulador.input['materias_inscrito'] = materias_inscrito_input
simulador.input['materias_recursando'] = materias_recursando_input
simulador.input['trabaja'] = trabaja_input

# Realizar la evaluación

simulador.compute()

# Obtener la recomendación

c_mat_baja = round(simulador.output['dar_de_baja'])

def barra_de_carga5s():
    tiempo_total = 5  # Tiempo total de carga en segundos
    intervalo_actualizacion = 0.1  # Intervalo de actualización de la barra en segundos
    pasos = int(tiempo_total / intervalo_actualizacion)
    

    for i in range(pasos + 1):
        porcentaje = int(i / pasos * 100)
        barra = "|" * int(i / pasos * 20)
        espacios = " " * (20 - len(barra))
        sys.stdout.write(f"\r[{barra}{espacios}] {porcentaje}%")
        sys.stdout.flush()
        time.sleep(intervalo_actualizacion)

    sys.stdout.write("\n\n")

print(Style.BRIGHT +"\nAnalizando perfil de datos y generando recomendación... ")
barra_de_carga5s()

#Se generan multiples recomendaciones a partir de las variables difusas y sus resultados

if c_mat_baja == 0:
    print(Fore.GREEN + "No deberias dar de baja ninguna materia!!!.")
elif c_mat_baja == 1 or c_mat_baja == 2:
    print(Fore.GREEN + f"Te recomiendo dar de baja {c_mat_baja} materias.")
elif c_mat_baja == 3 or c_mat_baja == 4 and trabaja_input == 1:
    print(Fore.GREEN +'''Es admirable que usted trabaje y estudie al mismo tiempo,
sin embargo, tiene que planificar bien sus tiempos para
rendir eficientemente en el estudio y trabajo.''')
    print(Fore.YELLOW + f"Tambien te recomiendo dar de baja {c_mat_baja} materias.")  
elif c_mat_baja == 3 or c_mat_baja == 4:
    print(Fore.YELLOW + f"Te recomiendo dar de baja {c_mat_baja} materias.")
else:
    print(Fore.RED + f"Te recomiendo dar de baja {c_mat_baja} materias.")

if materias_recursando_input == 1 or materias_recursando_input == 2:
    print(Fore.GREEN + "Tienes pocas materias recursando, esta bien pero no te descuides...")
elif materias_recursando_input == 3:
    print(Fore.YELLOW + "Pon mas atención, tienes muchas materias recursando!!!")
elif materias_recursando_input == 4:
    print(Fore.RED + '''Tienes que hacer algo, tienes muchas materias recursando,
tu futuro esta en PELIGRO!!!''')

elif semestre_input == 4 or semestre_input == 5 or semestre_input == 6 and materias_recursando_input == 0:
    print(Fore.GREEN + '''Por otro lado estas a la mitad del
camino y no tienes materias recursando.
           ¡¡¡SIGUE ASI!!!''')
elif semestre_input >= 7 and materias_recursando_input == 0:
    print(Fore.GREEN + '''Por otro lado es genial que hayas llegado hasta
este semestre tan alto sin recursar materias.
           ¡¡¡Felicidades!!!''')

if  materias_recursando_input >= 1 and semestre_input >= 7:
    print(Fore.GREEN + '''Por otro lado estas a punto de lograrlo,
si te sientes confiado, deberias dar el examen extraordinario,
y quitarte esa materia que llevas cargando.''')

elif materias_recursando_input >= 1 and semestre_input <= 6:
    print(Fore.GREEN + '''No tienes aun el conocimiento holistico, pero
si te sientes confiado, deberias dar el examen extraordinario,
y quitarte esa materia que llevas cargando.''')

total_materias = (materias_inscrito_input + materias_recursando_input) - c_mat_baja

print(Fore.GREEN + f"Lo ideal seria que lleves {total_materias} materias en total,")
print(Fore.GREEN + "asi podras tener un buen equilibrio y desempeño.")