from flask import Flask
from routes import routing_system

# useful links
# https://realpython.com/flask-blueprint/#what-a-flask-application-looks-like
# https://github.com/Shihara-Dilshan/John-Keells-App-Revamp/blob/main/Server/api/product.py
# https://github.com/Shihara-Dilshan/John-Keells-App-Revamp/blob/main/Server/services/product_service.py


app = Flask(__name__)
app.register_blueprint(routing_system)

if __name__ == '__main__':
    app.run()
