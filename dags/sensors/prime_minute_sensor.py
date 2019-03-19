import datetime as dt
import logging

from airflow.sensors.base_sensor_operator import BaseSensorOperator


class PrimeMinuteSensor(BaseSensorOperator):

    PRIME_MINUTES = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

    def poke(self, context):
        minute = dt.datetime.today().minute
        logging.info(f'Minute sensed: {minute}')
        return dt.datetime.today().minute in self.PRIME_MINUTES
