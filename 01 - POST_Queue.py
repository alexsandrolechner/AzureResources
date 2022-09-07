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

letters = string.ascii_lowercase
number = random.random()
queue = QueueClient.from_queue_url(
    queue_url="https://storage001teste.queue.core.windows.net/in-message",
    credential=token_credential
)


queue.send_message("Message: " + str(number) +
                   ''.join(random.choice(letters) for i in range(10)))
print("--------------------------------------")
