import urllib.request,json


def configure_request(app):
    global api_key
    api_key = app.config['QUOTE_API_KEY']


def get_quotes():
    with urllib.request.urlopen(api_key) as url:
        response = url.read()

        if response:
            quote = json.loads(response)

            return quote