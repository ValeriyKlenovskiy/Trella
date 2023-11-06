from fastapi import FastAPI
from tasks.router import router as router_task

app = FastAPI(
    title="Trello"
)

app.include_router(router_task)
