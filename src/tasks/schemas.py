from pydantic import BaseModel


class TaskBase(BaseModel):
    text: str
    user: str
    done_type: str


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskDelete(TaskBase):
    pass
