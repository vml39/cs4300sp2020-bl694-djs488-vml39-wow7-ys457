from . import *
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder
from app.irsystem.models.results import get_results, get_suggested_words
from app.irsystem.models.results_v1 import get_results_v1

project_name = "Karma Farmer"
net_id = "Brian Lu: bl694, Maria Silaban: djs488, Vivian Li: vml39, William Wang: wow7, Yuna Shin: ys457"

@irsystem.route('/', methods=['GET'])
def search():
	query = request.args.get('search') or ""
	weight = request.args.get('weight') or 50
	version = request.args.get('version')
	version = int(version) if version else 2
	if not query:
		data = []
		count = 0
		output_message = ''
	else:
		output_message = "Suggested Subreddits"
		data = []
		count = 0
		results = get_results(query, weight) if version == 2 else get_results_v1(query)
		for i in results:
			data.append(i)
	return render_template(
		'search.html',
		name=project_name,
		netid=net_id,
		output_message=output_message,
		data=data,
		query=query,
		weight=weight,
		version=version
	)

@irsystem.route('/suggested_words', methods=['GET'])
def get_words():
    query = request.args.get('search')
    subreddit = request.args.get('subreddit')
    suggested_words = get_suggested_words(query, subreddit)
    return { "suggested_words": suggested_words }
