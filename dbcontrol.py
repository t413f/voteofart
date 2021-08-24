import sqlite3

class DBManager():

    def __init__(self):
        self.conn = sqlite3.connect("mydb.db")
        self.cursor = self.conn.cursor()

    def create_db(self):
        with self.conn:
            """
                PRAGMA foreign_keys = 0;
                
                CREATE TABLE sqlitestudio_temp_table AS SELECT *
                                                          FROM paintings;
                
                DROP TABLE paintings;
                
                CREATE TABLE paintings (
                    id     INTEGER PRIMARY KEY
                                   UNIQUE
                                   NOT NULL,
                    name   TEXT    NOT NULL
                                   UNIQUE,
                    src    VARCHAR UNIQUE
                                   NOT NULL,
                    rating INTEGER DEFAULT (1500) 
                );
                
                INSERT INTO paintings (
                                          id,
                                          name,
                                          src
                                      )
                                      SELECT id,
                                             name,
                                             src
                                        FROM sqlitestudio_temp_table;
                
                DROP TABLE sqlitestudio_temp_table;
                
                PRAGMA foreign_keys = 1;
            :return:
            """
            pass

    def init_db(self, name, src):
        with self.conn:
            self.cursor.execute("")
            pass

    def get_elem(self):
        with self.conn:
            self.cursor.execute("")
            pass

    def edit_rating(self):
        with self.conn:
            self.cursor.execute("")
            pass

    def show_rating(self):
        with self.conn:
            self.cursor.execute("")
            pass
