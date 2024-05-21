# Proyecto CODER 

Comision: 54135

Alumno: Lucas Gomez

## Acerca del Projecto

Tenia planeado hacer como si fuera una pagina web como zonaprop o algo similar donde la gente pueda publicar sus 
propiedades (para venta o alquiler) y el cliente pueda buscar en base a lo que quiere. 
Desde el navbar podes acceder a las publicaciones, a las ciudades disponibles, a crear una publicación y a home,
a home quise hacer como en la mayoria de aplicaciones que si tocas el nombre de la empresa del navbar (izquierda)
te lleve a home, aunque igualmente puse el boton que te dirige al mismo lugar.

## Aplicaciones

Cuenta con la aplicación core y las aplicaciones: publicacion y venta

## Modelos

En la aplicacion publicacion hay 3 modelos:
Paises: Para registrar países
Ciudades: Para registrar ciudades que hereden de un país previamente registrado
Publicacion: Para crear publicaciones con un nombre, un precio, una descripción, que herede de una ciudad y tenga un concepto, ya sea alquiler o venta.

En la aplicacion venta hay modelos similares a los que el profesor propuso en la clase. Esto es así con el fin de que desde admin se le pueda agregar fotos de perfil o avatares a los usuarios que venden publicaciones

## Observaciones

core/components: card_with_img.html --> hay partes de esa plantilla que no estan aplicadas actualmente como el 
TITULO PREVIEW porque estaba cuando descargue el bootstrap y me gusto la idea asi que lo deje almacenado ahi para
usarlo posteriormente con las publicaciones.

El unico problema que tuve fue en core/index.html linea 23, por algun motivo en la pagina web me daba error cuando
ponía src="{% static 'core/img/casa.webp' %}" (aunque esté subida la img a static) entonces decidi poner directamente 
el link a la imagen. Entiendo que esto puede no ser una buena practica pero lo quería aclarar.