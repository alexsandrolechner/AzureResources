# AzureResources

Um dos problemas que geralmente temos são as conexões via Connection String aos recursos Azure. Uma conexão via Connection String pode nos trazer sérios problemas, por isto utilizaremos algumas formas de se evitar isto.
![image](https://user-images.githubusercontent.com/5125303/188926710-bafe0ff1-354c-417a-9a6c-17898616eee0.png)

01 - POST_Queue.py: Utilizando Service principal conseguimos contornar a necessidade de postar algo em uma QUEUE
01 - GET_Queue.py: Utilizando Service principal conseguimos contornar a necessidade de ler as mensagens de uma QUEUE
