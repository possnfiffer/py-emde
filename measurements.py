from peewee import *

db = SqliteDatabase('measurements.db')


class Measurement(Model):
    sea_level_pressure = FloatField()
    relative_humidity = FloatField()
    temperature = FloatField()
    rainfall = FloatField()
    wind_direction = FloatField()
    wind_speed = FloatField()
    month = IntegerField()
    day = IntegerField()
    year = IntegerField()
    hour = IntegerField()
    minute = IntegerField()
    second = IntegerField()


    class Meta:
        database = db

# Measurement types and samples
# sea level pressure 1013.15
# relative humidity  41.4
# temperature        18.2
# rainfall           0.60
# wind direction     126.9
# wind speed         0.79
# date               02 02 2016 20 20 12 (Month Day Year Hour Minute Second) I'll split this one out
# month              02 I'll need to strip the leading 0 off of theses so that I don't get a syntax error
# day                02 I'll need to strip the leading 0 off of theses so that I don't get a syntax error
# year               2016
# hour               20
# minute             20
# second             12

measurements = [
    {'sea_level_pressure': 1013.15,
        'relative_humidity': 41.4,
        'temperature': 18.2,
        'rainfall': 0.60,
        'wind_direction': 126.9,
        'wind_speed': 0.79,
        'month': 2,
        'day': 2,
        'year': 2016,
        'hour': 20,
        'minute': 20,
        'second': 12},
    {'sea_level_pressure': 1012.15,
        'relative_humidity': 42.4,
        'temperature': 12.2,
        'rainfall': 0.20,
        'wind_direction': 122.9,
        'wind_speed': 0.29,
        'month': 2,
        'day': 2,
        'year': 2016,
        'hour': 22,
        'minute': 22,
        'second': 12},
]


def add_measurements():
    for measurement in measurements:
        Measurement.create(sea_level_pressure=measurement['sea_level_pressure'],
                       relative_humidity=measurement['relative_humidity'],
                       temperature=measurement['temperature'],
                       rainfall=measurement['rainfall'],
                       wind_direction=measurement['wind_direction'],
                       wind_speed=measurement['wind_speed'],
                       month=measurement['month'],
                       day=measurement['day'],
                       year=measurement['year'],
                       hour=measurement['hour'],
                       minute=measurement['minute'],
                       second=measurement['second'])

if __name__ == '__main__':
    db.connect()
    db.create_tables([Measurement], safe=True)
    add_measurements()
