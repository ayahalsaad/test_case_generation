from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router.test_case_generator_router import router

app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)


app.get("/")
def read_root():
    return {"Hello": "World"}


app.get("/health_check/")
def health_check():
    return True





