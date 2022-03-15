import logging
import os

from flask import Flask
from flask_restful import Api, Resource, reqparse

from config import config

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s]: [{}] [%(levelname)s] %(message)s".format(os.getpid()),
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger()


class HelloWorld(Resource):
    def get(self):
        message = "Hello World"
        return {"message": message}

    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument("message", required=True)  # add args

        args = parser.parse_args()  # parse arguments to dictionary

        message = args["message"]
        return {"message": message}


def create_app():
    app = Flask(__name__)
    app.config.from_object(config())
    print(config)
    logger.info(f"""Starting app in {app.env} mode...""")
    api = Api(app)
    api.add_resource(HelloWorld, "/", "/hello")

    logger.info("App started.")
    return app


if __name__ == "__main__":
    # `app.run` is unsafe for production.
    app = create_app()
    app.run()
