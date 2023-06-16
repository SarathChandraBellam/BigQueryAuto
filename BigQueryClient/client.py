from google.cloud import bigquery


class BigQueryClient:
    """
    Class to establish a client connection, execute queries and compare result sets
    """

    def __init__(self, credentials):
        self.credentials = credentials

    def get_client(self):
        """
        Method to return big query client authenticated by service account credentials
        """
        client_ = bigquery.Client(credentials=self.credentials)
        return client_

    @staticmethod
    def execute_query(client, query, result_type="rows", timeout=None):
        """
        Method to execute the query and return the data as per result type
        """
        query_job = client.query(query)
        if timeout is not None:
            query_job.configuration.query.timeout = timeout
        result = query_job.result()
        if result_type.lower() == "json":
            json_data = [dict(row) for row in result]
            return json_data
        elif result_type.lower() == "dataframe":
            df = query_job.to_dataframe()
            return df
        else:
            return result
