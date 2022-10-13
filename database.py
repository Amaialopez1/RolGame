import mysql.connector




mybd = mysql.connector.connect(
    host='localhost',
    user='root',
    password = 'usuario123'
)

my_cursor = mybd.cursor(buffered=True);
# my_cursor.execute('drop database pokemons')


my_cursor.execute('use  pokemons');

#----------------------------------------------------------------
# 1 crear base de datos , unas tablas (solo elimina "#")
#my_cursor.execute('create database pokemons');
#my_cursor.execute('use  pokemons');

# my_cursor.execute('show databases');
# for db in my_cursor:
#     print(db[0]);


#my_cursor.execute("create table pokemon (id_pokemon int not null auto_increment, life int default 100, level int default 0, pokemon varchar(100),  unique key(id_pokemon))");

#my_cursor.execute("create table jugador(id int not null auto_increment, nombre_de_usario varchar(500) not null, contrasena varchar(500) not null, email varchar(500) not null, unique key(id))");

#my_cursor.execute("create table coach (id_coach int not null auto_increment,id_jugador int, position_x int, position_y int, experience int, id_pokemon int,  unique key(id_coach), foreign key(id_pokemon) references pokemon(id_pokemon) on delete set null on update cascade, foreign key(id_jugador) references jugador(id) on delete set null on update cascade)")

#my_cursor.execute("create table enemy(id_enemy int not null auto_increment, name varchar(500), level int, life int, attack int, pokemon  varchar(100),  unique key(id_enemy))");

#my_cursor.execute("create table pokemon_attack(id_pokemon_attack int not null auto_increment, id_enemy int, id_pokemon int, win bool, unique key(id_pokemon_attack), foreign key(id_enemy) references enemy(id_enemy), foreign key(id_pokemon) references pokemon(id_pokemon))");

#----------------------------------------------------------------
# 2 update (solo elimina "#")

#my_cursor.execute("drop table pokemon_attack");
#my_cursor.execute("drop table enemy");
#my_cursor.execute("alter table coach drop column position_x");
#my_cursor.execute("alter table coach drop column position_y")
#my_cursor.execute("alter table pokemon drop column pokemon")
#my_cursor.execute("alter table pokemon add column tipo_de_pokemon varchar(100)")
#my_cursor.execute("alter table coach change column experience experience int default 0")


#----------------------------------------------------------------


# my_cursor.execute('show columns from jugador');
# for jugador in my_cursor:
#     print(jugador)

# my_cursor.execute("show columns in coach");
# for column in my_cursor:
#     print(column[0]);

my_cursor.execute("show columns in pokemon");
for column in my_cursor:
    print(column[0]);

# sql1 = "insert into jugador(nombre_de_usario,contrasena,email) values (%s, %s, %s)";
# record1 = ( 'n','contrasena', 'email');
# my_cursor.execute(sql1,record1 );
# mybd.commit();


my_cursor.execute("select * from jugador ")
result = my_cursor.fetchall()
for row in result:
    print(row)

# my_cursor.execute("select * from jugador where id = 3")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)    

# my_cursor.execute("select * from jugador")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)    

my_cursor.execute('show tables')
for tb in my_cursor:
    print(tb[0]);