import os
import logging, json
from llama_index import VectorStoreIndex, SimpleDirectoryReader

FORMAT = '%(asctime)s %(funcName)s %(message)s'
logging.basicConfig(format=FORMAT)

def main():
    logger = logging.getLogger("llama_app")
    logger.setLevel(logging.DEBUG)
    logger.info("Starting llama app")

    myEnv = json.dumps(dict(os.environ), indent=4)
    logger.info("Environment: %s", myEnv)
    # print(myEnv)

    documents = SimpleDirectoryReader('data').load_data()
    index = VectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()
    response = query_engine.query("What did the author do growing up?")
    print(response)

if('__main__'):
    main()