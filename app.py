from flask import Flask, jsonify, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='ff213539420c4385b30dccc52205cc88')

@app.route('/get_articles', methods=['GET'])
def get_articles():
    query_param = request.args.get('query', 'bitcoin')
    all_articles = newsapi.get_everything(q=query_param)
    return jsonify(all_articles)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False)
