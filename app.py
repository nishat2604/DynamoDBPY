import boto3
from flask import Flask, request, jsonify
from  boto3.dynamodb.conditions import Key
from flask_cors import CORS
import uuid
#get Aws session

dynamodb = boto3.resource(    'dynamodb',
    region_name='us-east-2',  # Make sure the region is correct
    aws_access_key_id='#####',
    aws_secret_access_key='********'  )

table = dynamodb.Table('CustomerUserInfo') 
print(table)
    
app = Flask(__name__)
CORS(app)
@app.route("/useradd", methods=['POST'])
def useradd():
    print("PutItem succeeded:")
    data = request.get_json()  # Get JSON data from the request
    # # Process the data (e.g., add a user to a database)
    table.put_item(Item={
        "CustID": str( uuid.uuid1()),
        "name":data['name'],
        "address":data['address']
        
})
    return jsonify({"message": "User added successfully!", "data": data})


@app.route("/getuser", methods=['GET'])
def getuser():
    
    response = table.scan()
    data = response.get('Items', [])
    
    return jsonify({"message": "User get item successfully!", "data": data})



@app.route("/updateuser",methods=["POST"])
def updateuser():
    data = request.get_json()  # Get JSON data from the request
    response = table.update_item(
        Key = {
            'CustID': "1"
        },
        AttributeUpdates={
            'name': {
                    'Value': "nfarooqui",
                    'Action': 'PUT'
                },
                'address': {
                    'Value': "Calgary",
                    'Action': 'PUT'
                }
        },
        ReturnValues = "UPDATED_NEW" # returns the new updated values
    )
    return jsonify({"message": "User get item successfully!", "data": response})
if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
    