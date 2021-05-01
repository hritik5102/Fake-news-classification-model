import requests as req

import aiohttp
import asyncio

PORT_GPT2 = '5000'
PORT_BERT = '5500'
PORT_LSTM = '7000'
ports = ['5000', '5500', '7000']
BASE_URL = 'http://127.0.0.1:'
ROUTE = '/predict'

# def predict_from_server(text):

#     data = {'text': text}
#     a = req.post(BASE_URL + PORT_GPT2 + ROUTE, data)
#     b = req.post(BASE_URL + PORT_BERT + ROUTE, data) 
#     c = req.post(BASE_URL + PORT_LSTM + ROUTE, data)  
#     sum = int(a.text) + int(b.text) + int(c.text)
#     return 1 if sum > 1 else 0

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