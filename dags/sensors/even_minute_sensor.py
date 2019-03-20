import datetime as dt
import logging

from airflow.sensors.base_sensor_operator import BaseSensorOperator


class EvenMinuteSensor(BaseSensorOperator):

    def poke(self, context):
        minute = dt.datetime.today().minute
        logging.info(f'Minute sensed: {minute}')
        return minute % 2 == 0
