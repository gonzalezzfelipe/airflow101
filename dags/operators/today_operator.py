import datetime as dt

from airflow.models import BaseOperator


class TodayOperator(BaseOperator):

    def execute(self, context):
        print(f'Today is {dt.datetime.today()}')
        print(f'Execution date is {context["execution_date"]}')
