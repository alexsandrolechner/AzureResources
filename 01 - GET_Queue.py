import string
import random
from azure.identity import ClientSecretCredential
from azure.storage.queue import QueueClient

active_directory_application_id = "xxxx-d955-49e0-9724-xxx"
active_directory_application_secret = "loP8Q~BzxZwU0TsccXXaIPFddD_QaXX"
active_directory_tenant_id = "ZZ7f26e-cb2305-4444b-741-b7e4eXXXX"
    
token_credential = ClientSecretCredential(
    active_directory_tenant_id,
    active_directory_application_id,
    active_directory_application_secret
)
    
queue = QueueClient.from_queue_url(

    queue_url="https://STORAGENAME.queue.core.windows.net/in-message",
    credential=token_credential
)

messages = queue.receive_messages()
for msg in messages:
    print(msg.content)
    print("--------------------------------------")
