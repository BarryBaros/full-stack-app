#localhost:5000/create_contact - this is the address and "create_contact" is the endpoint
#google.com - this is the domain or URL

#create: first_name, last_name, email

#Frontend sends a request(GET, POST, PATCH, DELETE)
#Backend sends a response

from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})


#Run flask application
if __name__=="__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
