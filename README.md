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