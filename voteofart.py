from enum import Enum
from utils.db_api import dbcontrol


class Table(Enum):
    ID = 0
    NAME = 1
    SRC = 2
    RATING = 3

def main():
    pass
    # initialize object Database
    # db = dbcontrol.DBManager()

    # only for initialize db --- ready
    # db.init_db()

    # edit rating into id --- ready
    # print(db.get_elem(1)[Table.ID.value])
    # db.edit_rating(1, 1500)

    # test calculate ELO --- ready
    # print(calculations.calc_rating(db.get_elem(2), db.get_elem(1)))

    # test function showered top-50 ratings arts
    # for i in db.top_arts():
    #     print(i)



if __name__ == '__main__':
    main()

