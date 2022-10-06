import mysql.connector 


mybd = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = 'pas123',
)

my_cursor = mybd.cursor();

# my_cursor.execute('create database pokemons');

# my_cursor.execute('show databases');
# for db in my_cursor:
#     print(db);
my_cursor.execute('use  pokemons');
# my_cursor.execute('drop table jugador')
# my_cursor.execute("create table jugador(id int not null auto_increment, nombre_de_usario varchar(500) not null, contrasena varchar(500) not null, email varchar(500) not null, tipo_de_pokemon int, salud int default 100, nivel int default 0, experencia int default 0, unique key(id))");


# my_cursor.execute('show tables')
# for tb in my_cursor:
#     print(tb[0]);


# my_cursor.execute("show columns in jugador");
# for column in my_cursor:
#     print(column[0]);