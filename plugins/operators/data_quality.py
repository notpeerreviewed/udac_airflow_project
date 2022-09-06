from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from helpers import SqlQueries

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id,
                 fmt: [str],
                 query,
                 failure_value,
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)

        self.redshift_conn_id = redshift_conn_id
        self.fmt = fmt
        self.query = query
        self.failure_value = failure_value


    def execute(self, context):
        self.log.info('Running DataQualityOperator')

        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        for f in self.fmt:
            query = self.query.format(f)
            res = redshift.get_first(query)[0]

            if res == self.failure_value:
                raise ValueError(f"failed query {query}, failure {self.failure_value}")