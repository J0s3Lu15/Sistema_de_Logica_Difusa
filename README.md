# Sistema de Lógica Difusa para Recomendación Académica
![Vista Previa](vista_previa.jpg)

## Descripción:
Este README proporciona una explicación detallada del código Python llamado "TutorAcademico.py", que implementa un sistema de lógica difusa para brindar recomendaciones académicas a estudiantes universitarios. El sistema utiliza variables difusas para evaluar el desempeño académico del estudiante y recomendar la cantidad de materias que debería dar de baja en función de ciertas condiciones.

## Uso del Código
El código se ejecuta como una aplicación de consola donde el usuario proporciona su información académica (semestre, materias inscritas, materias recursando y si trabaja o no). Luego, el sistema de lógica difusa evalúa esta información y muestra las recomendaciones.

## Requisitos para ejecutar:
```bash
pip install numpy
pip install scikit-fuzzy
pip install colorama
```
## Como ejecutarlo:
```bash
python TutorAcademico.py
```
## ¿Qué es un Sistema de Lógica Difusa?
Un sistema de lógica difusa es una técnica utilizada en la inteligencia artificial y la computación para modelar y resolver problemas que implican incertidumbre y ambigüedad. A diferencia de la lógica clásica, que utiliza valores binarios (verdadero o falso), la lógica difusa trabaja con valores en un rango continuo, lo que permite representar de manera más precisa la naturaleza imprecisa de muchas situaciones del mundo real. Los sistemas de lógica difusa utilizan variables difusas, conjuntos difusos y reglas difusas para tomar decisiones basadas en la incertidumbre.

## Uso del Sistema de Lógica Difusa en este Código
El código "TutorAcademico.py" utiliza un sistema de lógica difusa para proporcionar recomendaciones académicas a estudiantes universitarios. En particular, el sistema recomienda la cantidad de materias que un estudiante debería dar de baja en función de las siguientes variables difusas:

- Semestre actual del estudiante.
- Cantidad de materias inscritas por el estudiante.
- Cantidad de materias que el estudiante está recursando (repitiendo).
- Si el estudiante trabaja o no (variable binaria).

El sistema utiliza funciones de membresía difusa, reglas difusas y una serie de condiciones para evaluar la situación académica del estudiante y proporcionar recomendaciones basadas en la lógica difusa.

## Pasos para crear el sistema de lógica difusa:

## Definición de Variables Difusas
El código define cinco variables difusas:

- semestre: Representa el semestre académico actual del estudiante (1-8).
- materias_inscrito: Representa la cantidad de materias inscritas por el estudiante (1-8).
- materias_recursando: Representa la cantidad de materias que el estudiante está recursando (0-4).
- trabaja: Indica si el estudiante trabaja o no (0 para "no" y 1 para "sí").
- dar_de_baja: La variable de consecuencia que representa la cantidad de materias recomendadas para dar de baja (0-7).

## Funciones de Membresía:
Se definen funciones de membresía para cada variable difusa. Estas funciones de membresía determinan cómo se mapean los valores de entrada en conjuntos difusos. Se utilizan funciones de membresía triangulares y automáticas (automf) para definir estos conjuntos difusos.

## Reglas Difusas:
El código define un total de 54 reglas difusas para evaluar las condiciones proporcionadas por el usuario en función de las variables difusas. Cada regla especifica una combinación de condiciones y su correspondiente consecuencia. Estas reglas se utilizan para tomar decisiones basadas en la lógica difusa y determinar la cantidad de materias que se recomienda dar de baja.

## Creación del Sistema de Control Difuso:
El sistema de control difuso se crea utilizando todas las reglas difusas definidas anteriormente. Este sistema evalúa las condiciones proporcionadas por el usuario y produce una recomendación basada en la lógica difusa.

## Configuración y Evaluación del Simulador:
El código utiliza un simulador para configurar valores de entrada (las condiciones del estudiante) y calcular la salida del sistema de control difuso. El simulador toma en cuenta las reglas, funciones de membresía y valores de entrada para generar una recomendación.

## Visualización de Recomendaciones:
Finalmente, el código muestra al usuario las recomendaciones basadas en la lógica difusa. Estas recomendaciones incluyen la cantidad de materias que se sugiere dar de baja, comentarios sobre el desempeño académico y sugerencias adicionales.

## Contactos:
Si te gusta mi trabajo o estás buscando consultoría para tus proyectos, Pentesting, servicios de RED TEAM - BLUE TEAM, implementación de normas de seguridad e ISOs, controles IDS - IPS, gestión de SIEM, implementación de topologías de red seguras, entrenamiento e implementación de modelos de IA, desarrollo de sistemas, Apps Móviles, Diseño Gráfico, Marketing Digital y todo lo relacionado con la tecnología, no dudes en contactarme al +591 75764248 y con gusto trabajare contigo.
