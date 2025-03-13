from src.dao.base import BaseDAO
from src.task.models import Tasks


class TasksDAO(BaseDAO):
    model = Tasks