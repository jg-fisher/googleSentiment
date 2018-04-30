from scripts import Crypto
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/eth')
def sentiment():
	term = 'eth_price'
	analysis = Crypto.Analysis(term)
	analysis.run()
	return jsonify({"Term": term, "Sentiment": analysis.sentiment, "Subjectivity": analysis.subjectivity})

if __name__ == '__main__':
	app.run(debug=True)


