# import asyncio
# from typing import AsyncIterable, Awaitable
# from langchain.callbacks import AsyncIteratorCallbackHandler
# from test_cases_app.utils.llm_utils import azure_llm
# from pydantic import BaseModel


# async def send_message(message: str) -> AsyncIterable[str]:
#     callback = AsyncIteratorCallbackHandler()
#     model = azure_llm()


# async def wrap_done(fn: Awaitable, event: asyncio.Event):
#     try:
#         await fn
#     except Exception as e:
#         print(f"Caught exception: {e}")
#     finally:

#         event.set()


#     task = asyncio.create_task(wrap_done(
#         model.agenerate(messages=[[(content=message)]]),
#         callback.done),
#     )

#     async for token in callback.aiter():
#         # Use server-sent-events to stream the response
#         yield f"data: {token}\n\n"

#     await task

# class StreamRequest(BaseModel):
#     """Request body for streaming."""

#     message: str
