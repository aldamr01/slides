import os
from opensearch_dsl import connections
from dotenv import load_dotenv

load_dotenv()

def connect():
    
    host = os.getenv("OPENSEARCH_HOST")
    username = os.getenv("OPENSEARCH_USER")
    password = os.getenv("OPENSEARCH_PASS")
    auth = (username, password)

    if not all([host, username, password]):
        raise ValueError("Missing OpenSearch credentials in .env file")  

    return connections.create_connection(
        alias="default",
        hosts=[host],  
        http_auth=auth,  
        use_ssl=True,
        verify_certs=False
    )