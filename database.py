import mysql.connector




mybd = mysql.connector.connect(
    host='localhost',
    user='root',
    password = 'usuario123'
)

my_cursor = mybd.cursor();

#==================================================================================
#crear base de datos
#=================================================================================
#my_cursor.execute('create database pokemons');


# my_cursor.execute('show databases');
# for db in my_cursor:
#     print(db[0]);


my_cursor.execute('use  pokemons');


#==================================================================================
#crear la tabla "pokemon"
#==================================================================================
#my_cursor.execute("create table pokemon (id_pokemon int not null auto_increment, life int default 100, level int default 0, pokemon varchar(100),  unique key(id_pokemon))");


#==================================================================================
#crear la tabla "jugador"
#==================================================================================
# my_cursor.execute('drop table jugador')
#my_cursor.execute("create table jugador(id int not null auto_increment, nombre_de_usario varchar(500) not null, contrasena varchar(500) not null, email varchar(500) not null, unique key(id))");

#==================================================================================
#crear la tabla "coach"
#==================================================================================
#my_cursor.execute("create table coach (id_coach int not null auto_increment,id_jugador int, position_x int, position_y int, experience int, id_pokemon int,  unique key(id_coach), foreign key(id_pokemon) references pokemon(id_pokemon), foreign key(id_jugador) references jugador(id)) ")
#==================================================================================
#crear la tabla "enemy"
#==================================================================================
#my_cursor.execute("create table enemy(id_enemy int not null auto_increment, name varchar(500), level int, life int, attack int, pokemon  varchar(100),  unique key(id_enemy))");

#==================================================================================
#crear la tabla "pokemon_attack"
#==================================================================================
#my_cursor.execute("create table pokemon_attack(id_pokemon_attack int not null auto_increment, id_enemy int, id_pokemon int, win bool, unique key(id_pokemon_attack), foreign key(id_enemy) references enemy(id_enemy), foreign key(id_pokemon) references pokemon(id_pokemon))");

#my_cursor.execute("drop database pokemons");

my_cursor.execute('show tables')
for tb in my_cursor:
    print(tb[0]);
# my_cursor.execute('select * from jugador');
# for jugador in my_cursor:
#     print(jugador)

# my_cursor.execute("show columns in jugador");
# for column in my_cursor:
#     print(column[0]);

# sql1 = "insert into jugador(nombre_de_usario,contrasena,email) values (%s, %s, %s)";
# record1 = ( 'n','contrasena', 'email');
# my_cursor.execute(sql1,record1 );
# mybd.commit();


# my_cursor.execute("select * from jugador where id = 1")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)

# my_cursor.execute("select * from jugador where id = 3")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)    

# my_cursor.execute("select * from jugador")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)    

