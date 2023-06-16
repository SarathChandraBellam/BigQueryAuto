# BigQueryAuto
Client to establish a connection to big query database, execute queries and compare datasets

#### Getting the credentials from service account
BigQueryAuth(kwargs).get_credentials() will create google oauth2 credentials object from service account credentials with a assigned scope as shown below in the image. 
![image](https://github.com/SarathChandraBellam/BigQueryAuto/assets/28837993/b9a5d8d5-78dc-42fe-8f45-3afb3ba71ad2)

#### Create a client object
BigQueryClient(credentials).get_client() will create client connection. The above generated oauth client credentials will be used for the same. 
![image](https://github.com/SarathChandraBellam/BigQueryAuto/assets/28837993/32b457fb-2afe-4a73-8d91-fe5484a31c8b)

#### Execute a query
BigQueryClient(credentials).execute_query(client, query, timeout=None, result_type="rows") will create a queryjob object, executes the query and return the output as per result type parameter. it can row iterator(rows), pandas dataframe object (dataframe), json object (json)
![image](https://github.com/SarathChandraBellam/BigQueryAuto/assets/28837993/ea67d135-4aa0-480c-a3f3-2d7150dd2c8b)

###### Example of result_type = json 

![image](https://github.com/SarathChandraBellam/BigQueryAuto/assets/28837993/8f75335f-e439-4893-8b02-90c5bab03183)

###### Example of result_type = dataframe

![image](https://github.com/SarathChandraBellam/BigQueryAuto/assets/28837993/92161fbb-a367-40de-b90d-a8cf09c59dac)






