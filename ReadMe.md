# FeedBack Cat Facts Gustavo Holley

* Fecha de Entrega: 2022/12/27
* Fecha de Recolección: 2022/12/28
* Fecha de Revisión: 2023/01/03
  * Revisado por [Henry Blair G.](https://github.com/HenryBlairG)

***
## 1. Requerimientos Funcionales

| Requerimiento | Puntaje Máximo | Puntaje Obtenido | Observaciones |
|-:|:--:|:--:|:-|
|Los usuarios deben poder registrarse en la plataforma|10|10|Flujo Mediante Botón Register que redirige a formulario de Registro.|
|Los usuarios registrados deben poder ingresar a la plataforma|10|10|Vista Raíz permite ingresar mediante usuario (Tal vez sea bueno ponerle clave si era contemplado en el registro, de todas maneras está marcado como un `known bug`).|
|Los usuarios ingresados pueden consultar y marcar un cat Fact para indicar que les gusta|10|8|Desde la vista index se pueden visualizar CatFacts y marcar mediante un botón de `like`, Sin embargo al solicitar más no se renderean correctamente para marcarlos apropiadamente. Para cargar más en definitva se debe recargar la página|
|Los usuarios ingresados deben poder ver una lista de los cat Facts que les ha gustado|10|0|La vista index muestra catfacts con likes, pero no precisamente los que me gustaron a mi|
|Los usuarios ingresados deben poder visualizar los cat Facts más populares de la comunidad|10|0|La Lista de CatFacts populares existe en la interfaz, solo que vacía|

***
## 2. Requerimientos No Funcionales

### 2.1 Arquitectura

| Requerimiento | Puntaje Máximo | Puntaje Obtenido | Observaciones |
|-:|:--:|:--:|:-|
|El backend de la plataforma debe consumir la [API de cat facts](https://catfact.ninja/fact)|20|20|Se Consume API de cat facts|
|Arquitectura MVC|20|15|Se usó [Django](https://docs.djangoproject.com/en/4.1/)|
|Usar una base de datos relacional|10|10|Se usó [SQLite](https://www.sqlite.org/docs.html)|

### 2.2 Calidad de Desarrollo

| Requerimiento | Puntaje Máximo | Puntaje Obtenido | Observaciones |
|-:|:--:|:--:|:-|
|Documentación para levantar entorno|10|5|<ul><li>Faltó Descripción de Version de Python utilizada (Asumiremos `python3.11.1`)</li><li>Faltó indicar el gestor de Entornos (Asumiremos `venv`)</li><li>Excelente Uso de pantallazos</li><li>Faltó indicar la base de datos utilizada (Asumiremos `SQLite`)</li></ul>|
|Buenas prácticas de diseño de software|20|5| Se encontraron algunas redundacias lógicas y acoplamientos en los métodos ajenos al manejo de sesion en `Myapp/views.py`|
|Tests|10|0|No se encontraron tests|
|Buenas prácticas de manejo de git|10|4|Buen manejo de ramas, por funcionalidad. Los nombres de las ramas no explican en qué consisten los cambios introducidos, se nota un esfuerzo por explicar camios introducidos a nivel de commit, pero no sujetos a ninguna convención|


***
## 3. Bonus

| Detalle Bonus | Puntaje Máximo | Puntaje Obtenido | Observaciones |
|-:|:--:|:--:|:-|
|Usar docker + docker-compose en deploy local|10|0|Sin Docker ni docker-compose|
|Desacoplar Frontend de Backend como servicios separados en el docker-compose|10|0|Dificil sin containerizacion|
|Deploy|10|0|Sin Deploy Externo|
|Pipelines de Github Actions para correr tests y/o deploy|10|0|Sin Deploy Externo|
|Diagramas UML|10|3|Se incluyen Diagramas UML. <ul><li>Diagrama de clases de uso modela el caso de uso de manejo de sesion y usos Asociados a CatFacts como uno solo.</li><li>El Diagrama de clases modela más bien un diagrama de entidad-relación</li></ul>|


*** 
## 4. Observaciones Generales

Se muestra un Proyecto de buen alcance, se modelaron 3 de los 4 casos de uso principales del próposito de la plataforma y el caso de uso de prerrequisito de acceso (El manejo de sesión). A nivel de código se observan márgenes de mejora sin llegar a ver faltas en buenas prácticas de código graves. Se hace buena separación de Tareas (Hay una buena planificación del proyecto) Se observan también oportunidades de mejora en algunos aspectos de buenas prácticas. Algunas recomendaciones pueden ser:
* Usar una guía de estilos para programar tu proyecto
  * Existen herramientas que automatizan esto como el uso de plantillas de código, linters, etc.
  * Investigar sobre convenciones populares al momento de escoger una guía de estilos
* Al momento de consumir apis, es importante manejar los casos borde que implica, sean:
  * Caso en que el servicio no está disponible (Errores de timeout al emitir la request)
  * Caso de que el servicio esté con fallas internas (Errores con código de estado 500)
  * Caso en que la api cambie sin avisar a nadie y tu request sea erronea (Errores con código de estado 400)
  * Caso en que la api cambie el contenido de su respuesta (formato del json, o si ahora será csv, etc)
* Cuando modelas casos de uso, la relación entre los distintos casos de uso depende de cómo estén relacionados entre si. Si bien el signin actua como barrera para el acceso a la plataforma, no tiene que ver con todo lo que hago una vez entro a mi plataforma
* Los modelos de clases UML son una herramienta de muy bajo nivel al momento de describir tu software. Un diagrama de entidad relacion era el adecuado para expresar lo que mostraste.
* Cuando definas comportamientos de controladores, ten en cuenta que las funciones deben hacer una sola cosa. Cuando veas lógica repetida siempre busca mecanismos para que tu código sea lo menos redundante posible.
* Te adjunté mi implementación de Usar docker y docker-compose para dockerizar tu proyecto. Te vi muy motivado con eso y me pareció valioso que lo tengas para tener un punto de partida con el cual jugar.
* Este comentario es más personal, no todos los computines están de acuerdo conmigo y hay mejores que piensan distinto a esto que te voy a comentar: Procura evitar usar interfaces gráficas para tus herramientas de programación dia a dia. Eso te ayuda a primero comprender qué quieres lograr con la herramienta que estás usando (Y al mismo tiempo validar si para eso se usa la herramienta) y segundo te permite aprender a interactuar con los servidores en que publiques tus programas. Con respecto a esta ultima idea, te recomiendo aprender shellscript si usas linux o la sintaxis de powershell en windows 
* Github (Y la gran gran mayoría, si no todos, de los servicios donde puedes versionar tu código) usan markdown para mostrar texto. Apoyate en estos documentos para publicar tu documentación ya que te permite también versionarla de manera escalable y la deja servida para que todos puedan leerla sin necesidad de usar software externo.

***
## Puntaje Total: 90 / 150
# Nota:  4.2