# BigQueryAuto
Client to establish a connection to big query database, execute queries and compare datasets

#### Getting the credentials from service account
BigQueryAuth(kwargs).get_credentials() will create google oauth2 credentials object from service account credentials with a assigned scope as shown below in the image. 
![image](https://github.com/SarathChandraBellam/BigQueryAuto/assets/28837993/b9a5d8d5-78dc-42fe-8f45-3afb3ba71ad2)

#### Create a client object
BigQueryClient(credentials).get_client() will create client connection. The above generated oauth client credentials will be used for the same. 
![image](https://github.com/SarathChandraBellam/BigQueryAuto/assets/28837993/32b457fb-2afe-4a73-8d91-fe5484a31c8b)




