from app import app
import urllib.request,json
from .models import movie
api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]
def get_news(category):
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_result = None

        if get_news_response['results']:
            news_result_list = get_news_response['results']
            news_result = process_result(news_result_list)


    return news_result
def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        overview = news_item.get('overview')
        poster = news_item.get('poster_path')
        vote_average = news_item.get('vote_average')
        vote_count = news_item.get('vote_count')

        if poster:
            news_object = News_results(id,title,overview,poster,vote_average,vote_count)
            news_results.append(news_object)

    return news_results