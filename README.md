pretend-api
==========

A Python API wrapper for [pretend's API](https://v1.pretend.best)

Installing
==========

**Python 3.8 or higher is required**

```sh
pip install git+https://github.com/PretendServices/pretend-api.git 
```

Usage example (Screenshot endpoint)

```py 
import asyncio
from PretendAPI import API 
    
api = API("YOUR-API-KEY")
    
async def main():
    data = await api.get_instagram_user("apple")
    print(f"{data.username} has {data.followers:,} followers")
    
if __name__ == "__main__":
    asyncio.run(main())
```

You can find more examples in the examples folder

Methods
==========

**Current available methods for using our API:**

- get_key_info (get information about your own key)
- uwuify (uwuify a message)
- get_snapchat_user (get information about a snapchat user's profile)
- get_snapchat_story (get someone's snapchat story)
- get_tiktok_user (get information about someone's tiktok profile)
- get_roblox_user (get information about someone's roblox profile)
- get_instagram_user (get information about someone's instagram profile)
- get_instagram_story (get someone's instagram story)
- download_spotify (download a spotify song using an url)
- lastfm_chart (create a lastfm collage of the user's top albums)
- ask_chatgpt (ask a question to chatgpt)
- join_discord_server (join a discord server using an user account)
- roleplay (get an anime gif for each available emotion)
- is_nsfw (check if the provided image url is nsfw)
- get_random_pfp (get a random profile picture from a specific category)
- screenshot (get a screenshot from the given url)
- get_captcha_image (get a captcha image containing text along with the response)