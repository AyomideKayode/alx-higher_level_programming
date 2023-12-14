# Project: 0x0F. Python - Object-relational mapping

## Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

```sh
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

With an ORM:

```sh
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## Resources

### Read or watch:

- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
- [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
- [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
- [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
- [10 common stumbling blocks for SQLAlchemy newbies](https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
- [Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)

## Learning Objectives

### General

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to <code>SELECT</code> rows in a MySQL table from a Python script
- How to <code>INSERT</code> rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

## Tasks

0. [Get all states](./0-select_states.py) :

Write a script that lists all `states` from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

```sh
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```

1. [Filter states](./1-filter_states.py) :

Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

```sh
ayomide@Kazzywiz:~/alx-higher_level_programming/0x0F-python-object_relational_mapping$ ./1-filter_states.py root ayomide_Kayode7 hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
ayomide@Kazzywiz:~/alx-higher_level_programming/0x0F-python-object_relational_mapping$ 
```

| Task                           | File                                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------ |
|                                |
| 2. Filter states by user input | [2-my_filter_states.py](./2-my_filter_states.py)                                                       |
| 3. SQL Injection...            | [3-my_safe_filter_states.py](./3-my_safe_filter_states.py)                                             |
| 4. Cities by states            | [4-cities_by_state.py](./4-cities_by_state.py)                                                         |
| 5. All cities by state         | [5-filter_cities.py](./5-filter_cities.py)                                                             |
| 6. First state model           | [model_state.py](./model_state.py)                                                                     |
| 7. All states via SQLAlchemy   | [7-model_state_fetch_all.py](./7-model_state_fetch_all.py)                                             |
| 8. First state                 | [8-model_state_fetch_first.py](./8-model_state_fetch_first.py)                                         |
| 9. Contains `a`                | [9-model_state_filter_a.py](./9-model_state_filter_a.py)                                               |
| 10. Get a state                | [10-model_state_my_get.py](./10-model_state_my_get.py)                                                 |
| 11. Add a new state            | [11-model_state_insert.py](./11-model_state_insert.py)                                                 |
| 12. Update a state             | [12-model_state_update_id_2.py](./12-model_state_update_id_2.py)                                       |
| 13. Delete states              | [13-model_state_delete_a.py](./13-model_state_delete_a.py)                                             |
| 14. Cities in state            | [model_city.py](./model_city.py), [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py) |
