import feedparser
from grabfeed.grabber import return_rss


def get_feed_url(url):
    feed = return_rss(url)
    if str(feed).startswith('http://') or str(feed).startswith('https://'):
        return feed
    else:
        return url.rstrip('/') + feed


def get_news(feed):
    feeds = []
    d = feedparser.parse(feed)
    for entry in d['entries']:
        feeds.append({'titulo': entry['title'],
                      'url': entry['link'],
                      'descripcion' : entry['summary']})

    return feeds