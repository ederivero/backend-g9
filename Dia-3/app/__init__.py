from flask import Flask, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hola soy un servidor de Flask 😎'


usuarios = [{
    "nombre": "Paolo",
    "dni": "77777777"
}, {
    "nombre": "Eduardo",
    "dni": "78787878"
}]


@app.route('/hello/<username>')
def hello(username):
    return f'Hola {username}'


@app.route('/user/<int:user_id>')
def show_user(user_id):
    return f'El id del usuario es: {user_id}'


@app.route('/price/<float:product_price>')
def show_price(product_price):
    return f'El precio del producto es: {product_price}'


@app.route("/auth/login", methods=['POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


from flask import render_template

@app.route('/page/')
@app.route('/page/<name>')
def page(name=None):
    headers = request.headers
    print(headers)
    return render_template('index.html', name=name)

@app.route('/try/request-data/', methods=['POST'])
def get_request_data():
    method = request.method
    print(method)
    # GET

    path = request.path
    print(path)
    # /auth/reques-data/

    # json = request.get_json()
    # print(json)
    # { "email": "email@gmail.com", "password": "mypassword"}

    headers = request.headers
    print(headers)
    # Host: 127.0.0.1:5000
    # User-Agent: insomnia/2022.6.0
    # Content-Type: multipart/form-data; boundary=X-INSOMNIA-BOUNDARY
    # Accept: */*
    # Content-Length: 197520

    form_data = request.form['email']
    print(form_data)
    # email@gmail.com

    form_data_files = request.files['image']
    print(form_data_files)
    # <FileStorage: 'image.png' ('image/png')>

    cookies = request.cookies
    print(cookies)
    #  ImmutableMultiDict([token])

    cookie = request.cookies.get('token')
    print(cookie)
    # Bearer ewrwpo22o2lk...

    return 'Try route'


@app.route("/products", methods=['POST', 'GET', 'PUT', 'DELETE'])
def products():
    return 'Esta es la ruta productos'