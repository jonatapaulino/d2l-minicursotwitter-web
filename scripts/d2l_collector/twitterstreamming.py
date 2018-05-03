# coding=utf8

# Import dos pacotes necessários do Twython
from twython import TwythonStreamer
from twython import Twython

# Import métodos para tratar a data
from datetime import datetime
import pytz


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        # Id do twitter
        object_id = data['id']

        # Id do usuário que postou o texto
        user_id = data['user']['id']

        # Usuário que postou o texto
        user_name = data['user']['screen_name']

        # Texto postado em utf-8

        if 'retweeted_status' in data.keys():
            text = data['retweeted_status']['text']
        else:
            text = data['text'].encode('utf-8')

        # Data que foi publicado
        posted_at_tweet = data['created_at']

        # Data que foi publicado formatada
        fmt = '%Y-%m-%d %H:%M:%S.%f'
        new_date = datetime.strptime(posted_at_tweet, '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)

        published_date = str(new_date.strftime(fmt))

        tweet = {
            'object_id': object_id,
            'user_id': user_id,
            'user_name': user_name,
            'text': text,
            'published_date': published_date,
            'create_date': published_date,
            'last_update': published_date,
        }

        print(tweet)

    def on_error(self, status_code, data):
        print(status_code)

        self.disconnect()


if __name__ == "__main__":

    consumer_key = None # Get Keys and Access Token at apps.twitter.com
    consumer_secret = None # Get Keys and Access Token at apps.twitter.com
    access_token = None # Get Keys and Access Token at apps.twitter.com
    access_token_secret = None # Get Keys and Access Token at apps.twitter.com

    #E criamos nossa instância do coletor
    stream = MyStreamer(consumer_key, consumer_secret, access_token, access_token_secret)

    stream.statuses.filter(track="#minicursotwitterludiico") #inicialize o código e poste um twitter com essa hashtag.