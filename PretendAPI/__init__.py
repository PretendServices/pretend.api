import aiohttp 
import discord
from typing import Optional, Literal

from .errors import *
from .models import *

class API():
    """
    The API manager object
    
    Parameters 
    ----------
    api_key: :class:`str`
        A valid Pretend API key
    """

    def __init__(self, api_key: str): 
        self.api_key = api_key 
        self.base_url = "https://v1.pretend.bot"
        self.headers = {
            "api-key": self.api_key
        }
    
    async def __do_request(
        self, 
        path: str,
        method: Literal['GET', 'POST'] = "GET",
        return_type: Literal['json', 'text'] = "json",
        params: Optional[dict] = None, 
        json: Optional[dict] = None   
    ):
        """
        Send a request to the API

        Parameters
        ----------
        path: :class:`str`
            The path to request from 
        method :class:`Literal['GET', 'POST']`
            The HTTP method to use for the request
        return_type: :class:`Literal['json', 'text']`
            The value type to return from the request
        params: :class:`Optional[dict]`
            URL parameters
        json: :class:`Optional[dict]`
            Request body parameters
        """

        async with aiohttp.ClientSession(headers=self.headers) as cs: 
            async with cs.request(method, f"{self.base_url}{path}", json=json, params=params) as r: 
                if r.ok:
                    if return_type == "json":
                        return await r.json()
                    else:
                        return await r.text()
                
                raise HTTPError(
                    (await r.json())['detail'],
                    r.status
                )
    
    async def get_key_info(self) -> APIKey:
        """
        Get information about the current API key
        """

        data = await self.__do_request("/apikey")  
        return APIKey(**data)
    
    async def uwuify(
        self, 
        message: str
    ) -> str:
        """
        Uwuify a message
        Example: hello -> hewwo
        
        Parameters
        ----------
        message: :class:`str` 
            The message you are trying to convert
        """

        data = await self.__do_request(
            "/uwu",
            params={'message': message}
        )

        return data['message']
    
    async def get_snapchat_user(
        self, 
        username: str
    ) -> SnapchatUser:
        """
        Get information about a snapchat profile
        
        Parameters 
        ----------
        username: :class:`str` 
            The snapchat username you are trying to fetch snapchat information from
        """

        data = await self.__do_request(
            "/snapchat/user", 
            params={'username': username}
        )
        return SnapchatUser(**data)
    
    async def get_snapchat_story(
        self, 
        username: str
    ):
        """
        Get a snapchat user's story (it has to be a verified snapchat account)
        
        Parameters 
        ----------
        username: :class:`str` 
            The snapchat user you are trying to fetch the story from
        """

        data = await self.__do_request(
            "/snapchat/story",
            params={'username': username}
        )

        return SnapchatStories(**data)         
    
    async def get_tiktok_user(
        self, 
        username: str
    ) -> TikTokUser: 
        """
        Get information from a tiktok profile 

        Parameters 
        ----------
        username: :class:`str` 
            The TikTok user you are trying to fetch information from    
        """

        data = await self.__do_request(
            "/tiktok",
            params={'username': username}
        )

        return TikTokUser(**data)
    
    async def get_roblox_user(
        self, 
        username: str
    ) -> RobloxUser: 
        """
        Get information from a roblox profile 

        Parameters 
        ----------
        username: :class:`str` 
            The Roblox user you are trying to fetch information from    
        """

        data = await self.__do_request(
            "/roblox",
            params={'username': username}
        )

        return RobloxUser(**data)
    
    async def get_instagram_user(
        self, 
        username: str
    ) -> InstagramUser: 
        """
        Get Instagram user information
        
        Parameters
        ----------
        username: :class:`str`
            The Instagram user you are trying to fetch information from
        """

        data = await self.__do_request(
            "/instagram/user",
            params={"username": username}
        )

        return InstagramUser(**data)
    
    async def get_instagram_story(
        self, 
        username: str
    ) -> InstagramStories: 
        """
        Get an user's Instagram stories

        Parameters
        ----------
        username: :class:`str`
            The Instagram user to fetch stories from    
        """

        data = await self.__do_request(
            "/instagram/story", 
            params={'username': username}
        )

        return InstagramStories(**data)
    
    async def download_spotify(
        self, 
        url: str
    ) -> SpotifySong:
        """
        Download a spotify song from url
        
        Parameters
        ----------
        url: :class:`str`
            The spotify song url you are trying to download
        """

        data = await self.__do_request(
            "/spotify/song",
            params={'url': url}
        )

        return SpotifySong(**data)
    
    async def lastfm_chart(
        self, 
        username: str,
        size: str = "3x3", 
        period: Literal['overall', '7day', '1month', '3month', '6month', '12month'] = 'overall' 
    ) -> ImageURL: 
        """
        Get a Collage of user's top albums scrobbled by Last FM

        Parameters
        ----------
        username: :class:`str`
            The Last FM username you are trying to get a collage from 
        size: :class:`str`
            The size of the collage. By default this is `3x3`
        period :class:`Literal['overall', '7day', '1month', '3month', '6month', '12month']`
            Fetch top albums of this user for a limited period of time. By default this is `overall`                 
        """

        data = await self.__do_request(
            "/lastfm/chart",
            params={
                "username": username, 
                "size": size, 
                "period": period
            }
        )

        return ImageURL(**data)
    
    async def ask_chatgpt(
        self, 
        prompt: str
    ) -> str:
        """
        Get a response from Chat GPT

        Parameters
        ----------
        prompt: :class:`str`
            The question you are asking Chat GPT         
        """

        data = await self.__do_request(
            "/openai/chatgpt",
            method="POST", 
            params={"prompt": prompt}
        )

        return data['response'].replace("\\n", "\n")
    
    async def join_discord_server(
        self, 
        user_token: str, 
        invite_code: str
    ):
        """
        Join a discord server using an user account

        Parameters
        ----------
        user_token: :class:`str`
            A Discord User token
        invite_code: :class:`str`
            The server's invite code. If server's invite is discord.gg/pretendbot invite code is pretendbot
        """

        return await self.__do_request(
            "/discord/joiner",
            method="POST", 
            json = {
                "token": user_token, 
                "invite": invite_code
            }   
        )
    
    async def post_avatar(
        self, 
        user: discord.User
    ) -> str: 
        """
        Post an user's avatar to pretend avatar network (bot developer only endpoint)
        
        Parameters
        ----------
        user: :class:`discord.User`
            The discord user you are trying to post it's avatar from 
        """

        payload = {
            "url": user.display_avatar.url, 
            "type": "gif" if user.display_avatar.is_animated() else "png", 
            "userid": str(user.id), 
            "name": str(user)
        }

        return await self.__do_request(
            "/avatars",
            method="POST", 
            json=payload
        )
    
    async def roleplay(
        self, 
        image_type: Literal[
            'airkiss',
            'bite',
            'blush',
            'brofist',
            'celebrate',
            'cheers',
            'clap',
            'confused',
            'cry',
            'cuddle',
            'hug',
            'hump',
            'kiss',
            'lick',
            'love',
            'pat',
            'punch',
            'tickle',
            'wave'
        ]
    ) -> ImageURL:
        """
        Get an Anime Roleplay GIF

        Parameters
        ----------
        image_type: :class:`str`
            The image category you are trying to fetch
        """

        data = await self.__do_request(f"/roleplay/{image_type}")
        return ImageURL(**data)
    
    async def is_nsfw(
        self, 
        url: str
    ) -> bool: 
        """
        Check if an image contains NSFW content

        Parameters
        ----------
        url: :class:`str`
            The image url
        """

        data = await self.__do_request(
            "/nsfw",
            params={"url": url}
        )

        return data.get("is_nsfw")
    
    async def get_random_pfp(
        self,
        type: Literal['banners', 'pfps'],
        category: Literal['anime', 'girl', 'roadmen', 'cute', 'imsg', 'mix'],
        format: Optional[str] = None
    ) -> ImageURL:
        """
        Get a random picture from a specific category
        
        Parameters
        ----------
        type: :class:`Literal['banners', 'pfps']`
            The kind of picture you are trying to get
        category :class:`Literal['anime', 'girl', 'roadmen', 'cute', 'imsg', 'mix']`
            The picture category you are trying to fetch from 
        format: :class:`Optional[str]`
            The specific picture format you are trying to fetch. If not passed it will return a random gif or png
        """

        data = await self.__do_request(
            f"/pictures/{type}/{category}",
            params={"format": format} if format else None
        )

        return ImageURL(image_url=data['url'])
    
    async def get_captcha_image(self) -> CaptchaImage:
        """
        Get a random captcha image along with the correct captcha response
        """

        data = await self.__do_request("/image/captcha")
        return CaptchaImage(**data)

    async def screenshot(
        self,
        website_url: str,
        timeout: int = 1
    ) -> ImageURL:
        """
        Take a screenshot of a certain webpage
        
        Parameters
        ----------
        website_url: :class:`str`
            The url of the website you are trying to screenshot
        timeout :class:`int`
            The amount of seconds to wait before taking the screenshot 
        """

        data = await self.__do_request(
            "/screenshot",
            params={
                'url': website_url,
                'timeout': timeout
            }
        )

        return ImageURL(image_url=data['screenshot_url'])