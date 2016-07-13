import tweepy

auth = tweepy.OAuthHandler("byEBbmGLc4scB59ZoG4Lszzc0", "271bxFZc4CFU7HRVYsCfQT7q4UfodM4eA20co9lDVY2hvCfNzp")
auth.set_access_token("368675631-AjI4E4XU3PrkTOAEObQvupDJq813Xd7FVBlhQ1ng", "bvHnZOtc6zHrbuQqHNBYpXZXpgSYjWRrxkD8zmitNN4GY")

api = tweepy.API(auth)

api.update_profile_background_image("")
