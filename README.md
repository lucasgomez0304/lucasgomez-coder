# Proyecto CODER 

Comision: 54135

Alumno: Lucas Gomez

## Acerca del Projecto

Tenia planeado hacer como si fuera una pagina web como zonaprop o algo similar donde la gente pueda publicar sus 
propiedades (para venta o alquiler) y el cliente pueda buscar en base a lo que quiere. En un futuro tengo planeado 
añadir filtrosde busqueda tanto para paises, ciudades, precios y si es para alquileres o venta. Tambien, agregar 
fotos tanto a las publicaciones como a las imagenes de las ciudades. 
Desde el navbar podes acceder a las publicaciones, a las ciudades disponibles, a crear una publicación y a home,
a home quise hacer como en la mayoria de aplicaciones que si tocas el nombre de la empresa del navbar (izquierda)
te lleve a home, aunque igualmente puse el boton que te dirige al mismo lugar.
A su vez agregar cuando inicia sesion un correo electronico donde el cliente va a poder contactar al dueño de la
propiedad atraves de la publicación.

## Aplicaciones

Cuenta con la aplicación core y la aplicación publicacion

## Modelos

En la aplicacion publicacion hay 3 modelos:
Paises: Para registrar países
Ciudades: Para registrar ciudades que hereden de un país previamente registrado
Publicacion: Para crear publicaciones con un nombre, una descripción y una ciudad (aunque en la publicacion se ve
la ciudad y el pais).

## Observaciones

core/components: card_with_img.html --> hay partes de esa plantilla que no estan aplicadas actualmente como el 
TITULO PREVIEW porque estaba cuando descargue el bootstrap y me gusto la idea asi que lo deje almacenado ahi para
usarlo posteriormente con las publicaciones.

El unico problema que tuve fue en core/index.html linea 23, por algun motivo en la pagina web me daba error cuando
ponía src="{% static 'core/img/casa.webp' %}" (aunque esté subida la img a static) entonces decidi poner directamente 
el link a la imagen. Entiendo que esto puede no ser una buena practica pero lo quería aclarar.