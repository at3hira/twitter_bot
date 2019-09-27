import tweepy, config

def tweet(url):
    """Twitter APIを使用してツイートする関数
    """
    # OAuthHandlerインスタンスを作成
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    # ツイート
    api.update_status(url)
