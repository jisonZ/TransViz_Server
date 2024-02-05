from ..extensions import db
from sqlalchemy.sql import func
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import Mapped, mapped_column
from dataclasses import dataclass 

# class modelflow(db.Model):
#   id = db.Column(db.String(100), primary_key=True)
#   name = db.Column(db.String(50), nullable=False)
#   flowData = db.Column(db.Text, nullable=False)
#   deployed = db.Column(db.Boolean, default=False)
#   isPublic = db.Column(db.Boolean, default=False)
#   apikeyid = db.Column(db.String(100), nullable=True)
#   chatbotConfig = db.Column(db.Text, nullable=True)
#   apiConfig = db.Column(db.Text, nullable=True)
#   analytic = db.Column(db.Text, nullable=True)
#   createdDate = db.Column(mysql.DATETIME(timezone=True), default=func.now())
#   updatedDate = db.Column(mysql.DATETIME(timezone=True), default=func.now())
#   categpry = db.Column(db.String(100), nullable=True)

@dataclass 
class modelflow(db.Model):
  id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
  name: Mapped[str] = mapped_column(db.Text, nullable=False)
  flowData: Mapped[str] = mapped_column(db.Text, nullable=False)
  deployed: Mapped[bool] = mapped_column(db.Boolean, default=False)
  isPublic: Mapped[bool] = mapped_column(db.Boolean, default=False)
  apikeyid: Mapped[str] = mapped_column(db.String(100), nullable=True)
  chatbotConfig: Mapped[str] = mapped_column(db.Text, nullable=True)
  apiConfig: Mapped[str] = mapped_column(db.Text, nullable=True)
  analytic: Mapped[str] = mapped_column(db.Text, nullable=True)
  createdDate: Mapped[str] = mapped_column(mysql.DATETIME(timezone=True), default=func.now())
  updatedDate: Mapped[str] = mapped_column(mysql.DATETIME(timezone=True), default=func.now())
  category: Mapped[str] = mapped_column(db.String(100), nullable=True)