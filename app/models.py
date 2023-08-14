from .database import Base
from sqlalchemy import TIMESTAMP, Sequence, Column, Integer, String, Boolean
from sqlalchemy.sql import func


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, Sequence("note_id_seq"), primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=True)
    published = Column(Boolean, nullable=False, server_default='True')
    createdAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())
