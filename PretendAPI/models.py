from pydantic import BaseModel
from typing import Literal, List, Optional

class APIKey(BaseModel):
    key: str 
    user_id: int 
    role: Literal['master', 'bot_developer', 'premium', 'pro', 'basic']

class SnapchatUser(BaseModel): 
    display_name: str 
    username: str 
    snapcode: str 
    bio: str 
    avatar: str 
    url: str

class SnapchatStory(BaseModel):
    url: str 
    timestamp: int 
    media_type: Literal['png', 'mp4']

class SnapchatStories(BaseModel):
    stories: List[SnapchatStory]
    count: int

class TikTokUser(BaseModel):
    username: str 
    nickname: Optional[str] 
    avatar: str 
    bio: str 
    verified: bool 
    private: bool
    url: str 
    followers: int 
    following: int 
    hearts: int 
    friends: int 
    videoCount: int

class RobloxUser(BaseModel):
    username: str 
    display_name: str 
    bio: str 
    id: str 
    created_at: int 
    banned: bool 
    avatar_url: str 
    url: str 
    friends: int 
    followings: int
    followers: int

class InstagramUser(BaseModel):
    username: str 
    full_name: str 
    bio: str 
    profile_pic: str 
    pronouns: List[str]
    highlights: int 
    posts: int 
    followers: int 
    following: int 
    id: int
    url: str

class InstagramStory(BaseModel):
    expiring_at: int 
    taken_at: int 
    type: Literal['video', 'image']
    url: str

class InstagramStories(BaseModel):
    user: InstagramUser 
    stories: List[InstagramStory]

class SpotifySong(BaseModel):
    artist: str 
    title: str 
    image: str 
    download_url: str

class ImageURL(BaseModel):
    image_url: str

class CaptchaImage(ImageURL):
    response: str