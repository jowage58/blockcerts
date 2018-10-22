from chalice import Chalice

app = Chalice(app_name='blockcert-api')


@app.route('/users/{user_id}', methods=['GET'])
def get_users(user_id):
    return {'hello': f'{user_id}'}


@app.route('/certs/{cert_id}', methods=['GET'])
def get_certs(cert_id):
    return {'hello': f'{cert_id}'}
