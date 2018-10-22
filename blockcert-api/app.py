import boto3

from chalice import Chalice

app = Chalice(app_name='blockcert-api')

DB = boto3.resource('dynamodb', region_name='us-west-2')

users_table = DB.Table('blockcert.users')


@app.route('/users/{user_id}', methods=['GET'])
def get_users(user_id):
    response = users_table.get_item(Key={'id': user_id})
    return response['Item']


@app.route('/certs/{cert_id}', methods=['GET'])
def get_certs(cert_id):
    return {'hello': f'{cert_id}'}
