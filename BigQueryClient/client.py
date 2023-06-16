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
    def execute_query(client, query, result_type="rows"):
        """
        Method to execute the query and return the data as per result type
        """
        query_job = client.query(query)
        if result_type.lower() == "rows":
            return query_job.result()
        elif result_type.lower() == "dataframe":
            return query_job.to_dataframe()
        else:
            return query_job.result()
