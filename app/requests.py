import urllib.request,json
from .models import Sources
from .models import Headlines


# Getting api key
api_key = None
# Getting the news base url
base_url = None
headlines_base_url=None


def configure_request(app):
    global api_key,sources_url,base_url,headline_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url=app.config['SOURCE_BASE_URL']
    headline_base_url=app.config['HEADLINES_BASE_URL']
   
def get_sources(category):
    '''
    a function that returns sources with category passed in as a parameter
    '''
    full_url = base_url.format(category,api_key)
    with urllib.request.urlopen(full_url) as url:
        source_data = url.read()
        json_source_data = json.loads(source_data)
        # print(json_source_data)

        source_list = None

        if json_source_data['sources']:
            json_lib = json_source_data['sources']
            source_list = process_sources(json_lib)
            
def process_sources(sources):
    '''
    an 'interface' that filters data and inserts it into a class
    '''
    source_list = []
    for one_source in sources:
        id = one_source.get('id')
        name = one_source.get('name')
        desc = one_source.get('description')
        url = one_source.get('url')
        country = one_source.get('country')
       

        data_sources = Sources(id,name,desc,url,country)
        source_list.append(data_sources)
        # print('full_headlines_url')

    return source_list

    return source_list