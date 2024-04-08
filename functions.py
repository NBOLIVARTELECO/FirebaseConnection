import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import firestore

#Segundo commit

def FirestoresExampleSet():

    # Initialize Firebase Admin SDK with service account credentials
    cred = credentials.Certificate("TESTPOO.json")
    firebase_admin.initialize_app(cred)
    #niji

    # Access Firestore database
    db = firestore.client()

    # Example: Add data to Firestore
    doc_ref = db.collection("usuarios").document("usuariorUno")
    doc_ref.set({
        "nombre": "Johny",
        "EDAD": 28,
        "email": "john@example.comm"
    })

    # # Example: Read data from Firestore
    # docs = db.collection("users").get()
    # for doc in docs:
    #     print(f"{doc.id} => {doc.to_dict()}")
    #CRUD
    # Leer, Escribir, Actualizar, Borrar

def RealtimeSet():


    # Initialize Firebase Admin SDK with service account credentials
    cred = credentials.Certificate("TESTPOO.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://testpoo-59c96-default-rtdb.firebaseio.com'
    })

    # Get a reference to the Firebase Realtime Database
    ref = db.reference('/')

    # Example: Write data to the Realtime Database
    ref.set({
        'users': {
            'user12': {
                'name': 'John',
                'age': 30
            },
            'user2': {
                'name': 'Alice',
                'age': 25
            }
        }
    })