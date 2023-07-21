from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncio
import uuid
from fastapi.responses import HTMLResponse
from http import HTTPStatus

app = FastAPI()

class Task(BaseModel):
    task_id: uuid.UUID
    status: str
    result: list = []

tasks = {}

async def process_task(task_id, urls):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch_url(session, url) for url in urls])
        tasks[task_id].result = results
        tasks[task_id].status = "completed"

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello, this is a simple crawler server.</h1>"

@app.post("/api/v1/tasks/", response_model=Task, status_code=201)
async def create_task(urls: List[str]):
    task_id = uuid.uuid4()
    task = Task(task_id=task_id, status="running")
    tasks[task_id] = task

    asyncio.create_task(process_task(task_id, urls))

    return task

@app.get("/api/v1/tasks/{task_id}", response_model=Task)
async def read_task(task_id: uuid.UUID):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.middleware("http")
async def log_requests(request, call_next):
    response = await call_next(request)
    scope = request.scope
    http_version = f"{scope['http_version'][0]}.{scope['http_version'][1]}"
    status_code = response.status_code
    status_phrase = HTTPStatus(status_code).phrase
    print(f"{scope['client'][0]}:{scope['client'][1]} - "
          f'"{scope["method"]} {scope["path"]} HTTP/{http_version}" '
          f'{status_code} {status_phrase}')
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
