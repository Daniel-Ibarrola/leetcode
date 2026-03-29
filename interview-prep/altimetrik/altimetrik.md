# Preguntas

1. Como has usado python?

He usado Python en distintos tipos de proyectos, 
desde herramientas de línea de comandos hasta 
microservicios expuestos mediante APIs REST y WebSockets. 
También lo he utilizado para desarrollar tooling interno, 
realizar análisis de datos e interactuar con bases de datos.

2. Como has usado bash?

He usado Bash en mi día a día principalmente para automatizar tareas y trabajar de forma más eficiente desde la terminal. 
Por ejemplo, lo he usado en **pipelines de CI** para ejecutar tests, correr builds, 
lanzar herramientas de validación y también para **subir y descargar artifacts** desde buckets o almacenamiento remoto.  

Además, lo he usado para tareas operativas como:

- **scripts de setup** para preparar entornos de desarrollo o despliegue,
- **cron jobs** para ejecutar tareas periódicas,
- **backups automáticos** cada cierto tiempo,
- **deploys** y tareas de release,
- **gestión de logs** para buscar errores o revisar el estado de procesos,
- **navegación y manipulación de archivos** en entornos Linux/servidores,
- y en general para **encadenar comandos** y resolver tareas repetitivas más rápido.

3. ¿Cómo abordarías la migración de un Bash legacy a Python?

Lo abordaría de forma incremental. Primero entendería el script actual: entradas, salidas,
dependencias, side effects, y casos especiales. 

Luego escribiría tests de caracterización o regresión para fijar el comportamiento actual. 
Después haría la reimplementación en Python por partes, validando que la nueva versión produce los 
mismos resultados que la anterior. Si hay diferencias, las reviso antes de considerar listo el cambio.

4. ¿Qué haces cuando encuentras un caso raro o una diferencia pequeña entre versiones?

Lo trato como algo importante, aunque parezca menor.
En este tipo de trabajo, una diferencia pequeña puede significar un cambio funcional relevante. 
Entonces vuelvo al origen: reviso el script legacy, entiendo si ese comportamiento es intencional o accidental, 
y valido con evidencia antes de ajustar la nueva versión. Prefiero ser cuidadoso que asumir que la diferencia no importa.

## Notas

- Hacerles muchas preguntas
- Tener pensadas ideas para la migración

Agregar estas preguntas:
1. como lidiar con imprevistos que puedan retrasar el proyecto y como lidiar si se pasan del deadline.
2. como estimar el tiempo que tardarias en completar alguna tarea