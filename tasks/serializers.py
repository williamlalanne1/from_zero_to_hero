from app import db, ma

from .models import Task

class TaskSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
       model = Task
