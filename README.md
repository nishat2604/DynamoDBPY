# DynamoDBPY
This is a test POC which  help  to learn Python Flask API CRUD method with Dynamo DB. It helps to give us a basic understanding about to  connect api backend with  Dynaomodb 

Below package are require to install  before start 
#pip install -r requiremets.txt that  is 
Flask
jsonify 
requests
SQLAlchemy
boto3
uuid

To  call dyanamo DB  first need to connect wtih  AWS and the code is dynamodb = boto3.resource(    'dynamodb',
    region_name='us-east-2',  # Make sure the region is correct
    aws_access_key_id='#######',
    aws_secret_access_key='****************'  )

Now call the Dynamo db table which  is already create at AWS
table = dynamodb.Table('CustomerUserInfo') 

There are 4 main method to  call the DynamoDB operations/command
a) table.put_item()  #insert 
b) table.scan()  #  Get  all items data = response.get('Items', [])
c) table.update_item  #passthe key , Attributes with  Dictionary attribute1 ={ value:"" ,Action="PUT"}
d) table.delete_item # pass key 
$ python app.py
#some special  command 

echo "# DynamoDBPY" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:nishat2604/DynamoDBPY.git
git push -u origin main

command to  delete the port 
lsof -i:5001
kill -9 40950






