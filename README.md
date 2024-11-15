Guillermo Aramburu - Gonzalo Bascans

Descripción del Diagrama
Se crea una clase Gremio donde se van a almacenar dos listas, aventureros y misiones.
Misiones es una clase abstracta, que heredan de ella mision individual y mision grupal.
Para el alcance del trabajo quizá no era necesario separar en dos entidades, pero lo
hicimos de esta manera porque si la app crece en un futuro, es más escalable.
También se crea la clase abstracta aventurero, que de ella heredaran las 3 clases de aventureros existentes.
La relación con gremio es 1 gremio y de 0--n misiones y 0--n aventureros. A su vez,
misiones y aventureros están relacionadas de ambos lados 0--n.
Esto es porque cada instancia de cada clase puede existir y permanecer sin la existencia de la otra. Ninguna puede existir sin Gremio.
Las clases heredadas de aventurero cada una tiene sus atributos, y Ranger tiene una clase Mascota que solo existe y tiene sentido si existe el ranger. Esta relación es de Composición.

Descripción de la Aplicación
La aplicación es un Juego de pasar misiones. Se deberán registrar aventureros, registrar misiones, y luego realizarlas. Las misiones pueden ser individuales o grupales. Luego de realizadas, se repartirá experiencia y dinero. Se podrá consultar top 10 aventureros con más misiones resueltas, top 10 aventureros de mayor habilidad y top 5 de misiones con mayor recompensa.

Funcionamiento:
Se deberá correr el main. Como no consulta a ninguna base de datos, no hay aventureros ni misiones seteadas, por lo tanto, se deberán crear. Es intuitiva, se deberá leer la terminal e ingresar por consola lo que se quiere hacer en función de lo que la terminal indique. En caso de ingresar datos incorrectos, la aplicacion lo llevará al menú principal.
