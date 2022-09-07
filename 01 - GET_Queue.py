import string
import random
from azure.identity import ClientSecretCredential
from azure.storage.queue import QueueClient

active_directory_application_id = "ffaec6b2-d955-49e0-9724-65a343281d7c"
active_directory_application_secret = "loP8Q~BzxZwU0Tscc5bSGCvxxHYaIPFddD_QabQm"
active_directory_tenant_id = "9e87f26e-cb05-4d5b-b441-b7e4e9da15a6"
    
token_credential = ClientSecretCredential(
    active_directory_tenant_id,
    active_directory_application_id,
    active_directory_application_secret
)
    
queue = QueueClient.from_queue_url(

    queue_url="https://storage001teste.queue.core.windows.net/in-message",
    credential=token_credential
)

messages = queue.receive_messages()
for msg in messages:
    print(msg.content)
    print("--------------------------------------")
