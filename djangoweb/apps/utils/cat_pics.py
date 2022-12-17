import asyncio
import json
from urllib.request import Request, urlopen

import httpx


def get_response(url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req_data = Request(url, headers=hdr)
    if req_data:
        data = urlopen(req_data).read()
        # print('----------downloaded cat image ------------')
        return data
    else:
        print("Error receiving data")
        return None

# async def get_response(url):
#     async with httpx.AsyncClient() as client:
#         r = await client.get(url)
#
#     return r


def main_cat():
    url_data = "https://api.thecatapi.com/v1/images/search"
    try:
        joke = get_response(url_data)
        json_data = json.loads(joke)
        return json_data[0]['url']
    except Exception as e:
        return "https://ms.storyasset.link/GvMLkxrjQUdFDJMWxRDyH1bEFzh1/11-affectionate-cat-breeds-ms-mqhvxzghjj.jpg"


if __name__ == '__main__':
    main_cat()


