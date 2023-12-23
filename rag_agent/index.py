async def gen():
    from agent import agent
    response = await agent.astream_chat(
        "What is 121 + 8? Once you have the answer, use that number to write a"
        " story about a group of mice."
    )

    response_gen = response.response_gen

    async for token in response.async_response_gen():
        print(token, end="")


import asyncio

loop = asyncio.new_event_loop()

loop.run_until_complete(gen())