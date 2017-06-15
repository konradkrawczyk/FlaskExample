from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/apiexample', methods=['GET', 'POST'])
def process_api_call():
	import json
	sample_input = request.args.get('sample_input')
	
	#Create a dictionary
	results = {'received_input':sample_input}
	
	#jsonify
	results_json = json.dumps(results)	
		
	return results_json
    	#return "bla"

@app.route('/printprettywebsite', methods=['GET', 'POST'])
def process_website_request():
	sample_input = request.args.get('sample_input')

	header = "<head></head>"
	body = "<body><b>We have received this input: "+str(sample_input)+"</body>"
	
	website = "<html>"+header+body+"</html>"

	return website
    	#return "bla"
