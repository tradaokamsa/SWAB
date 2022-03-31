from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    do_Ph = request.args.get('do_Ph')
    nhiet_do = request.args.get('nhiet_do')
    do_duc = request.args.get('do_duc')
    return render_template('index.html', do_Ph=do_Ph, nhiet_do=nhiet_do, do_duc=do_duc)

if __name__ == "__main__":
    app.run(debug=True) 