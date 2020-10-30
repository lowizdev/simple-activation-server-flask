#DB INSTALLATION AND INITIALIZATION FOR TEST CASES

#UNCOMMENT BELOW TO INITIALIZE DB
'''from ativador import db, Register
db.create_all()

teste1 = Register(activation_key = "123456789", application_key = "eusouachave")
teste2 = Register(activation_key = "987654321", application_key = "eusououtrachave")

db.session.add(teste1)
db.session.add(teste2)
db.session.commit()''' 

#TESTING WITH A REQUEST

import requests
import pprint

response = requests.post('http://localhost:5000/activate', json={
    "activation_key": "123456789"
})

pp = pprint.PrettyPrinter(indent=4) #printing stuff in a pretty charm

pp.pprint(response.content)