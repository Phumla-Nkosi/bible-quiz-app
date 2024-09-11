#!/usr/bin/env python3
"""Result Module"""

from typing import Dict
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Result(BaseModel, Base):
    """Result Class"""

    __tablename__ = 'results'

    score = Column(Integer, nullable=False, default=0)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def to_dict(self) -> Dict[str, str]:
        """Overrides parents to_dict"""
        obj = super().to_dict()

        obj.pop('user_id')
        obj.update({'user': getattr(self, 'user').to_dict()})
        return obj
