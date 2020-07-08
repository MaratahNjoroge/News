# News Highlights

This application lists various sources of news and subsequent highlights in each of the source. Clicking an individual highlight takes the user to the article itself for the full published story.

## By **[MaratahNjoroge](https://github.com/MaratahNjoroge)**

## Description
[This](https://maratah-news.herokuapp.com/) is a web application that lists various News sources gotten from [News API](https://newsapi.org/). A user can click on a News source and be directed to a page that contains News Articles from the selected News source. The article's title, image, date of publication and preview will be displayed and a user can click on the article to be directed to the source's site to read the entire article.

## User Stories
As a user I would like:
* To see various news sources and select the ones I prefer
* To see all the news articles from that news source
* To see the image, description and time the news article was created.
* To click on an article and read it fully from the news source.

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Display News sources | N/A | List of various News sources is displayed |
| Articles from selected News source | **Click** a News source | Directed to a page with a list of articles from the selected source |
| Display image, description, title and date of publish | N/A | An articles image, title, description and date of publication are displayed |
| Read an entire article | **Click** on an article | Directed to the source's site to read the entire article |

## Prerequisites
* Python3.6

## How to use it
* must have internet connection
* Click https://maratah-news.herokuapp.com/) <br/>
  or <br/>
* Copy https://maratah-news.herokuapp.com/) and  Paste the link on your prefered browser


## Setup/Installation Requirements
* internet access
* git clone https://github.com/MaratahNjoroge/News
* $ cd news-highlights
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh

# CREDITS

#### Google.com, StackOverflow.com and Miguel Grinberg -author of 'Flask Web Development, 2nd Edition'


# Support and Contacts

In case You have any issues using this code please do not hesitate to get in touch with me through maratah7@gmail.com or leave a commit here on github.

## Known Bugs

No known bugs

## Technologies Used
- Python3.6
- Flask framework
- Bootstrap
- Coolors

### License

**[MIT](./LICENSE)** (c) 2020 **[MaratahNjoroge](https://github.com/MaratahNjoroge/Portfolio-LP)**
