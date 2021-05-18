import requests as req

import aiohttp
import asyncio

PORT_GPT2 = '5000'
PORT_ROBERT = '5500'
PORT_LSTM = '7000'
ports = ['5000', '5500', '7000']
BASE_URL = 'http://127.0.0.1:'
ROUTE = '/predict'

async def predict_from_server(text):

    sum = 0
    data = {'text': text}
    async with aiohttp.ClientSession() as session:

        for port in ports:
            url = BASE_URL + port + ROUTE
            async with session.post(url, data=data) as resp:
                label = await resp.text()
                sum = sum + int(label)

    return 1 if sum > 1 else 0

# asyncio.run(main())