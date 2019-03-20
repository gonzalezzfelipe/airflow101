import datetime as dt
import logging

from airflow.models import BaseOperator


class TodayOperator(BaseOperator):

    def execute(self, context):
        """Log the difference between now and execution_date."""
        logging.info(f'Today is {dt.datetime.today()}')
        logging.info(f'Execution date is {context["execution_date"]}')
