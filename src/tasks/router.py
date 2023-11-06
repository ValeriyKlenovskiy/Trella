from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from tasks.models import task
from tasks.schemas import TaskCreate, Task, TaskUpdate

router = APIRouter(
    prefix="/api",
    tags=["Api"]
)


@router.get("/", response_model=List[Task])
async def get_tasks(session: AsyncSession = Depends(get_async_session)):
    query = select(task)
    result = await session.execute(query)
    return result.all()


@router.get("/{id}", response_model=List[Task])
async def get_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(task).where(task.c.id == task_id)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_task(new_task: TaskCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(task).values(**new_task.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "added"}


@router.put("/")
async def update_task(task_id: int, editable_task: TaskUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(task).where(task.c.id == task_id).values(**editable_task.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "edited"}


@router.delete("/")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    query = delete(task).where(task.c.id == task_id)
    await session.execute(query)
    await session.commit()
    return {"status": "deleted"}
