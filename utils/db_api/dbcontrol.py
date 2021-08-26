import sqlite3
import os

class DBManager():

    def __init__(self):
        self.conn = sqlite3.connect("D:\\voteofart\\mydb.db")
        self.cursor = self.conn.cursor()

    def create_db(self):
        with self.conn:
            """
            /////////////CODE FOR CREATE DB TABLE/////////////
                
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

    def init_db(self):
        with self.conn:
            for root, dirs, files in os.walk("D:\\gallery\\images"):
                for id, file in enumerate(files,start=1):
                    self.cursor.execute("INSERT INTO paints values (?, ?, ?, ?)", (id, file.removesuffix('.jpg'), os.path.join(root, file), 1500))

    def get_elem(self, id):
        with self.conn:
            result = self.cursor.execute("SELECT * FROM paintings WHERE id = ?", (id,)).fetchone()
            return result

    def edit_rating(self, id, rating):
        with self.conn:
            self.cursor.execute("UPDATE paintings SET rating = ? WHERE id = ?", (rating, id))

    def top_arts(self):
        with self.conn:
            result = self.cursor.execute("SELECT * FROM paintings order by rating DESC limit 50").fetchall()
            return result