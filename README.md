# PruebaTecnicaRedegal
Repositorio para subir el código implementado en la prueba técnica de Redegal

## 1. Explicación de la aproximación

Para desarrollar la solución al problema planteado, se ha recurrido principalmente al uso de DataFrames con la librería [Panda](https://pandas.pydata.org/). A continuación, se explicará de forma resumida los pasos que realiza el script implementado:

1. Lo primero que hace el script es, mediante el uso de la librería  [Argparse](https://docs.python.org/3/library/argparse.html), configurar los argumentos que puede recibir por línea de comandos. Esto nos permite configurar características como que solamente se pueda recibir un argumento (el nombre del fichero), definir una opción para describir el uso del comando (mediante -h o --help), etc.

2. Una vez dentro de la función main, primero se definen unas constantes que se utilizarán más adelante. A continuación, se implementa todo el código de la solución dentro de un try-except, para poder captar las posibles excepciones y mostrar un mensaje personalizado que ayude al usuario. 

3. Nada mas comenzar el try, se realiza la comprobación de la extensión del fichero ".parquet". En el caso de que no exista el fichero o la extensión no sea la correcta, saltará una excepción. Si se han pasado las comprobaciones necesarias, lo que se hace a continuación es crear con Panda dos dataframes, uno para el contenido del fichero ".parquet" y otro para el contenido ".csv". El fichero con extensión parquet contiene todos los datos de los viajes de [Yellow Taxi Trip Records](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page), y el fichero con extensión csv contiene los datos relacionados con las zonas de la ciudad, es decir, las Borough y las Zones. Una vez se tiene los dos dataframes, se hace un merge juntandolos ambos mediante el campo respectivo de cada dataframe que identifique la localización de destino.

4. Una vez se tiene el dataframe completo con todos los datos que nos interesan, se tendrán que realizar una serie de operaciones sobre él. La primera es filtrar el dataframe para quedarse solo con los viajes que tengan un tiempo de recorrido mayor a 0.95. A continuación, se agrupan todas las filas por Borough y por Zone, y se aplica la función size() sobre cada grupo para obtener el número de elementos de cada grupo. Este valor, mediante la función reset_index(), se almacena en una nueva columna llamada "Trips", asociada a cada grupo creado. Por último, se obtiene un nuevo dataframe solamente con las columnas de interés, y sobre este nuevo dataframe aplica la función sort_values() para ordenar de manera descendente las zonas con mayor numero de viajes, y a continuación se optiene el top 10 de esas zonas.

5. Por último, se imprime por pantalla el dataframe final.


## 2. Librerías de terceros usadas

-   os: Se utiliza esta librería para separar la extensión del nombre del fichero, y posteriormente comprobar esta extensión. Y también se usa para optener el path del fichero .python, y así poder obtener el fichero con la información de las zonas
-   pandas: Se utiliza esta librería para poder trabajar con todos los datos necesarios y analizarlos de forma fácil, usando el mismo formato ya que los dos ficheros que se usan vienen en formatos diferentes (parquet y csv)
-   argparse: Se utiliza esta librería para poder gestionar los argumentos que se le pasen por la línea de comandos al script de una forma más eficiente.

## 3. Como ejecutar el programa

Para ejecutar el programa desde 0, tendremos que realizar unos pasos previos:

1. Instalar [Python](https://www.python.org/downloads/). En este caso se utiliza la versión 3.10.7, que se puede descargar desde este enlace https://www.python.org/downloads/release/python-3107/. Tendremos que ir a la sección de Files, y elegir el instalador que nuestro sistema operativo requiera. 
2. Instalar las librería comentadas anteriormente. Para poder instalar las librerías, en este caso se ha usado el administrador de paquetes [pip](https://pypi.org/project/pip/), el cual se puede instalar siguiendo la guía disponible en la documentación oficial https://pip.pypa.io/en/stable/installation/. Una vez tenemos el administrador de paquetes, tendremos que instalar las librerías con los comandos "*pip install argparse*" y "*pip install pandas*".

Una vez tenemos esto configurado, podremos probar el programa. Para ello, abriremos una consola de comandos (cmd por ejemplo) dentro del directorio raíz del proyecto, e introduciremos el comando "*python main.py **nombre_archivo_paquet.paquet***". El archivo no tiene por que encontrarse en el directorio raíz del proyecto, en ese caso, tendremos que indicar la ruta entera al archivo. 

Ejemplo comando en el caso de que el fichero se encuentre en el directorio raiz:

    python main.py yellow_tripdata_2020-05.parquet

Ejemplo comando en el caso de que el fichero se encuentre en el directorio raiz:

    python main.py C:\Users\charl\Downloads\yellow_tripdata_2020-05.parquet
    
Para obtener información del comando, podemos ejecutarlo con la opción -h o --help, y nos mostrará información acerca de los argumentos del comando.