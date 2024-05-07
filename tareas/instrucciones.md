Tarea: Automatización de pruebas con GitHub Actions

Objetivo: Configurar y utilizar GitHub Actions para automatizar pruebas de scripts en Python, partiendo de un repositorio base proporcionado.

Pasos a seguir:
    1. Crear tu carpeta para la entrega:
        • Hacer Fork al repositorio de la clase en GitHub
        • Clonar el repositorio
        • Crea una branch para trabajar
        • Crear una carpeta con tu nombre y primer apellido dentro de la carpeta ‘tareas’

    2. Copiar el código de Python:
        • Copia a tu carpeta el archivo de la carpeta ‘códigos’ 

    3. Configurar GitHub Actions Workflow:
        • Crear un archivo YML con tu nombre y apellido en la carpeta .github/workflows: Este archivo configurará el workflow que se ejecutará automáticamente cada vez que hagas un push. Tienes que especificar que solo quieres que se haga el action cuando se cambian cosas en tu carpeta de tareas (triger). 

        • Dentro de tu carpeta crea un docker file que asegure que se podrá correr el archivo .py. Recuerda como se tiene que hacer un docker file con envs. 

        • Buscar la manera de probar el código usando GitHub Actions: Configura el workflow para que ejecute automáticamente las pruebas cada vez que se actualice tu carpeta.

    4. Ejecutar Pruebas Locales:
        • Verificar que las pruebas se ejecutan correctamente en tu repositorio personal antes de hacer push: Asegúrate de que todo funciona como se espera para evitar fallos en el proceso de CI/CD.

    5. Documentación:
        • Redactar un archivo .txt en tu carpeta: Debe explicar el propósito del proyecto, cómo se ejecutan las pruebas localmente, y cómo está configurado el workflow de GitHub Actions. Asegúrate de incluir cualquier información que pueda ser útil para entender y ejecutar correctamente el proyecto.

Criterios de Evaluación:
    • Correcta configuración y funcionalidad del workflow en GitHub Actions.
    • Eficiencia de las pruebas unitarias implementadas.
    • Claridad y completitud de la documentación proporcionada.
 
Entregable:
    • Hacer pull request de tu carpeta y el archivo evn.yml
