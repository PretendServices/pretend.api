import asyncio
from PretendAPI import API 

api = API("YOUR-API-KEY")

async def main():
    data = await api.get_instagram_user("apple")
    print(f"{data.username} has {data.followers:,} followers")

if __name__ == "__main__":
    asyncio.run(main())