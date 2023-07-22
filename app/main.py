import os
import logging, json

FORMAT = '%(asctime)s %(funcName)s %(message)s'
logging.basicConfig(format=FORMAT)

def main():
    logger = logging.getLogger("llama_app")
    logger.setLevel(logging.DEBUG)
    logger.info("Starting llama app")

    myEnv = json.dumps(dict(os.environ), indent=4)
    logger.info("Environment: %s", myEnv)
    # print(myEnv)


if('__main__'):
    main()