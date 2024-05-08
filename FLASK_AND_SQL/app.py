"""
Kood teeb Flask Web API, et saaks pärast GUI kaudu võtta neid andmeid databaasist.
Kasutame meetodeid GET, POST, PUT ja DELETE.
"""

import sqlalchemy
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, Time
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Teeme Flaski
app = Flask(__name__)

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


# Loob ühenduse ja teeb sessiooni databaasi muutmiseks
def connect_db():
    engine = create_engine('sqlite:///diners.db')
    Base.metadata.bind = engine
    dbsession = sessionmaker(bind=engine)
    return dbsession()


# Võtab kõik andmed tabelist ja muudab need JSON-iks, annab need edasi GET meetodil
@app.route('/', methods=['GET'])
def show_canteens():
    session = connect_db()
    canteens = session.query(Canteen).all()
    session.close()
    canteen_list = [{'ID': canteen.ID, 'NAME': canteen.NAME, 'LOCATION': canteen.LOCATION,
                     'TIME_OPEN': str(canteen.TIME_OPEN),
                     'TIME_CLOSED': str(canteen.TIME_CLOSED)} for canteen in canteens]
    return jsonify(canteen_list)


"""
Võtab query parameetri "time_range" ja selle abil otsib välja kõik sööklad, mis on avatud selles
vahemikus, mida sisestati parameetritesse. Kasutab datetime'i, et võrrelda aegu.
Võrdlemiseks võtab kõik andmed tabelist ja siis võrdleb ainult aegu for-loopiga.
Pärast teeb uue listi, kus on kõik sööklad, mis on avatud.
"""


@app.route('/canteens_by_time', methods=['GET'])
def get_canteens_by_time():
    time_range = request.args.get('time_range')
    if not time_range:
        return 'Please provide a time range like this: "HH:MM-HH:MM"', 400

    # Muudame datetime objektideks
    start_time_str, end_time_str = map(str.strip, time_range.split('-'))
    start_time = datetime.strptime(start_time_str, '%H:%M')
    end_time = datetime.strptime(end_time_str, '%H:%M')

    session = connect_db()
    canteens = session.query(Canteen).all()
    session.close()

    open_canteens = []
    for canteen in canteens:
        canteen_open = canteen.TIME_OPEN
        canteen_closed = canteen.TIME_CLOSED
        if canteen_open <= start_time.time() <= canteen_closed and canteen_open <= end_time.time() <= canteen_closed:
            open_canteens.append({
                'ID': canteen.ID,
                'NAME': canteen.NAME,
                'LOCATION': canteen.LOCATION,
                'TIME_OPEN': str(canteen_open),
                'TIME_CLOSED': str(canteen_closed)
            })

    return jsonify(open_canteens)


# Võtab tabeli parameetrid POST requestina ja sisestab need databaasi.
@app.route('/canteens', methods=['POST'])
def add_canteen():
    data = request.json
    if not all(key in data for key in ('NAME', 'LOCATION', 'TIME_OPEN', 'TIME_CLOSED')):
        return 'Data is not filled. Please give NAME, LOCATION, TIME_OPEN, and TIME_CLOSED.', 400

    # Muudame datetime objektideks
    time_open = datetime.strptime(data['TIME_OPEN'], '%H:%M').time()
    time_closed = datetime.strptime(data['TIME_CLOSED'], '%H:%M').time()

    session = connect_db()
    new_canteen = Canteen(NAME=data['NAME'], LOCATION=data['LOCATION'], TIME_OPEN=time_open,
                          TIME_CLOSED=time_closed)
    session.add(new_canteen)
    session.commit()
    session.close()

    return 'Canteen added successfully!', 201


"""
Võtab URL-ist söökla ID ja selle järgi uuendab tema andmed.
Vajab kõiki andmeid, et saaks uuendada.
"""


@app.route('/canteens/<int:canteen_id>', methods=['PUT'])
def update_canteen(canteen_id):
    session = connect_db()
    canteen = session.query(Canteen).filter_by(ID=canteen_id).first()
    if not canteen:
        return 'No canteen exists with this ID.', 404

    data = request.json
    if 'NAME' in data:
        canteen.NAME = data['NAME']
    if 'LOCATION' in data:
        canteen.LOCATION = data['LOCATION']
    if 'TIME_OPEN' in data:
        canteen.TIME_OPEN = datetime.strptime(data['TIME_OPEN'], '%H:%M').time()
    if 'TIME_CLOSED' in data:
        canteen.TIME_CLOSED = datetime.strptime(data['TIME_CLOSED'], '%H:%M').time()

    session.commit()
    session.close()

    return 'Canteen updated successfully!', 200


# Kustutab tabelist ära selle söökla ID, mida user paneb DELETE meetodiga kaasa.
@app.route('/canteens/<int:canteen_id>', methods=['DELETE'])
def delete_canteen(canteen_id):
    session = connect_db()
    canteen = session.query(Canteen).filter_by(ID=canteen_id).first()
    if not canteen:
        return 'No canteen exists with this ID.', 404

    session.delete(canteen)
    session.commit()
    session.close()

    return 'Canteen deleted successfully!', 200


if __name__ == '__main__':
    app.run()
