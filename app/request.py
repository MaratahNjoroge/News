from app import app
import urllib.request,json
from .models import blog

Blog = blog.Blog

#api key
api_key = app.config['BLOG_API_KEY']

base_url = app.config['BLOG_API_BASE_URL']

def get_blogs(category):
    '''
    Function that gets json to thr url request
    '''
    get_blogs_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_blogs_url) as url:
        get_blogs_data = url.read()
        get_blogs_response = json.loads(get_blogs_data)

        blog_results = None

        if get_blogs_response['results']:
            blog_results_list = get_blogs_response['results']
            blog_results = process_results(blog_results_list)

    return blog_results


def process_results(blog_list):
    '''
    This is a process function that take in blog_list as an argu,emt
    
    Args:
        blog_list : List that contains blog details

    Returns:
        blog_results: List of blog objects

    '''
    blog_results = []
    for blog_item in blog_list:        
        id = blog_item.get('id')        
        title = blog_item.get('title')
        name = blog_item.get('name')
        author = blog_item.get('author')
        description = blog_item.get('description')
        publishedAt = blog_item.get('date_published')
        content = blog_item.get('blog_content')
       

        if content:
            blog_object = Blog(id,title,name,author,description,publishedAt,content)
            blog_results.append(blog_object) 

    return blog_results
    

    
