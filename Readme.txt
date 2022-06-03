Todas las páginas del sitio se encontraran dentro de app_final.

Este es un sitio de reseñas de juegos.

Las reseñas no se podrán agregar si no hay un juego con nombre igual en la base de datos. 
Si el usuario intenta hacerlo, se le informara que el juego no se encuentra en la base de datos.

De la misma manera, para dejar una reseña, el usuario debe ingresar un nombre de autor de esa reseña.
Este debe ser o un usuario pre-existente o llamarse "anonimo" todo con minúscula.
Si el usuario intenta crear una reseña con un usuario no valido, se le informara de esto.

Se pueden registrar usuarios. Estos usuarios no pueden llamarse igual a otro. Si se intenta, se le informara que el nombre de usuario ya existe.
Se pueden agregar juegos. Este juego no puede llamarse igual a otro. Si se intenta, se le informara que el juego ya esta en el sistema.

El sitio permite ver todas las reviews publicadas, que salen ordenadas primero por nombre del juego y luego todos las reviews individuales de cada usuario. 
Si un juego esta en el sistema pero no tiene reviews, solo se podrá ver la información del juego en esta página.

Se pueden hacer una busqueda más acotada, por juego o por nombre del autor de la review.
Esto buscara en la base de datos la información pertinente para cada caso y lo mostrara.
Si se ingresa un juego que no existe aquí o un usuario que no ha dejado reviews, el resultado de la busqueda vendra vacía.
