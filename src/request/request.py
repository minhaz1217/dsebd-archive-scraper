import aiohttp

async def get(url: str):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        return await response.text()