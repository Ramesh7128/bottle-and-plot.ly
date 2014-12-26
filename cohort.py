import os
from bottle import route, run, template, get, post, request

import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in("ramesh.ravi3", "9dxictpo66")

@get('/plot')
def form():
	return '''<h2>Graph via plot.ly</h2>
				<form method="POST" action="/plot">
					NAME: <input name="name1" type="text" />
					AGE: <input name="age1" type="text" /><br/>
					NAME: <input name="name2" type="text" />
					AGE: <input name="age2" type="text" /><br/>
					NAME: <input name="name3" type="text" />
					AGE: <input name="age3" type="text" /><br/>
					<input type="submit"/>
				</form>'''

@post('/plot')
def submit():
	name1 = request.forms.get('name1')
	age1 = request.forms.get('age1')
	name2 = request.forms.get('name2')
	age2 = request.forms.get('age2')
	name3 = request.forms.get('name3')
	age3 = request.forms.get('age3')

	data = Data([
		Bar(
			x=[name1, name2, name3],
			y=[age1,age2, age3]
			)	
		])
	response = py.plot(data, filename='base_bar')
	url = str(response)

	if response:
		return template('''<h1>Congrats!</h1>
							<div>
								View your graph here: <a href="url"></a>
							</div>
							''',
							response=response
							)
					

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8080))
	run(host='0.0.0.0', port=port, debug=True)	


