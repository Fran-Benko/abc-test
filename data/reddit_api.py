# data/reddit_api.py
import requests
from config.settings import REDDIT_CLIENT_ID, REDDIT_CLIENT_KEY, REDDIT_USR_GRANT_TP, REDDIT_USR_USERNAME, REDDIT_USR_PASSWORD, REDDIT_ACCESS_URL, REDDIT_HOST


class RedditAPI:
    @staticmethod
    def get_posts(ticker: str) -> str:
        """Fetch Reddit posts mentioning the ticker."""
        # Authenticacion mediante request
        auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_ID, REDDIT_CLIENT_KEY)


        # Datos del usuario de Reddit
        data = { 
            'grant_type': REDDIT_USR_GRANT_TP,
            'username' : REDDIT_USR_USERNAME,
            'password' : REDDIT_USR_PASSWORD
        }

        # Una identificacion generica
        headers = {
            'User-Agent':'MyAPI:/0.0.1'
        }

        # Enviar el request
        auth_res = requests.post(REDDIT_ACCESS_URL, auth=auth, data=data, headers=headers)

        # Ver la respuesta de la API
        token = auth_res.json()['access_token']
        headers['Authorization'] = f'bearer {token}'



        try:
            response = requests.get(f"{REDDIT_HOST}/r/{ticker}/new", headers=headers)
            response.raise_for_status()

            data = [] # Inicializo

            # Iterar sobre los datos que recibimos de la consulta
            for post in response.json()['data']['children']:
                # poner los datos en el df
                data.append([
                    post['data']['subreddit'],
                    post['data']['title'],
                    post['data']['selftext'],
                    post['data']['upvote_ratio'],
                    post['data']['ups'],
                    post['data']['downs'],
                    post['data']['score']
                    ])


            cols = ['subreddit', 'title', 'selftext', 'upvote_ratio', 'ups', 'downs', 'score']

            return [data, cols]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Reddit posts: {e}")
            return []