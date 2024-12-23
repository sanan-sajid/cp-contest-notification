from flask import Flask, request, jsonify
from atcoder import result as atcoder
from codeforces import result as codeforces
from codechef import result as codechef
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/process', methods=['GET'])
def process():
    choice = request.args.get('choice')

    if choice == '1':
        output = atcoder("whatsapp")
    elif choice == '2':
        output = codeforces("whatsapp")
    elif choice == '3':
        output = codechef("whatsapp")
    elif choice == '4':
        output = atcoder("facebook")    
    elif choice == '5':
        output = codeforces("facebook")    
    elif choice == '6':
        output = codechef("facebook")    
    else:
        return jsonify({"error": "Invalid choice!"}), 400

    return jsonify({"output": output})

if __name__ == "__main__":
    app.run()  
