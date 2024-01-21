import feedparser
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    feed = {
        "title": "My Feed",
        "href": "http://rss.slashdot.org/Slashdot/slashdotMain",
        "show_images": True,
        "entries": {},
    }

    feed_url = feed["href"]
    parsed_feed = feedparser.parse(
        feed_url,
    )
    return parsed_feed


if __name__ == "__main__":
    app.run(debug=True)
