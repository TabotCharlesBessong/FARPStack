
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlmodel import Field

class TimeMixin(BaseModel):
  """Mxin to for detection value of when the entity was created and when it was last modified. """
  
  created_at: datetime = Field(default_factory=datetime.now)
  modified_at: datetime = Field(
    sa_column = Column(DateTime,default=datetime.now,onupdate=datetime.now,nullable=False)
  )