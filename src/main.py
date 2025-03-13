import os
import sys
from fastapi import FastAPI
from src.users.router import router as users_router
from src.task.router import router as tasks_router


sys.path.insert(1, os.path.join(sys.path[0], '..'))


app = FastAPI()

app.include_router(users_router)
app.include_router(tasks_router)


