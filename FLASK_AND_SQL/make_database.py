"""
Kood genereerib vastvalt .csv failile databaasi diners.db, kus asub tabel CANTEEN,
mille tulpadeks on ID, Name, Location, Time_open ja Time_Closed.

Koodi käivitada ühe korra. Mitu korda käivitades tekitab duplikaadid.
"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Time
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import csv

# Baas klass SQLAlchemy ORM mudeli kasutamiseks
Base = sqlalchemy.orm.declarative_base()


# Defineerin tabeli "Canteen" jaoks kõikide tulpade pealkirjad ja mis tüüpi andmed sisestan
class Canteen(Base):
    __tablename__ = 'CANTEEN'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(String, nullable=False)
    LOCATION = Column(String, nullable=False)
    TIME_OPEN = Column(Time)
    TIME_CLOSED = Column(Time)


# Avan databaasi, kui databaasi pole, siis teeb selle. Teeb ka sessiooni databaasiga confimiseks.
def opendb():
    engine = create_engine('sqlite:///diners.db')
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    database_session = session_maker()
    print("Opened database successfully")
    return database_session


"""
Võtan .csv failist vajalikud andmed vastavalt tulpadele.
Muudan ka ajad datetime objektideks, et neid saaks pärast võrrelda.
"""


def get_data(data_session, file):
    with open(file, newline='') as csvfile:
        file_content = csv.DictReader(csvfile, delimiter=';')
        for row in file_content:
            name = row['Name']
            location = row['Location']
            time_open_str, time_closed_str = row['Open'].split('-')
            time_open = datetime.strptime(time_open_str.strip(), '%H:%M').time()
            time_closed = datetime.strptime(time_closed_str.strip(), '%H:%M').time()
            canteen = Canteen(NAME=name, LOCATION=location, TIME_OPEN=time_open, TIME_CLOSED=time_closed)
            data_session.add(canteen)
    data_session.commit()
    print("Data from Canteens.csv imported successfully")


if __name__ == "__main__":
    session = opendb()
    get_data(session, './Canteens.csv')
    session.close()
    print("Connection closed")
