from flask import Flask
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    return "{\"message\":\"hi python app\"}" 
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0",port=int("3000"),debug=True)%                                                                                                                                                                                                               madhusudhanan@madhus-MacBook-Air docker-sample % 
