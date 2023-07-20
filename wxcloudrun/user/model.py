from datetime import datetime

from wxcloudrun import db


# 计数表
class User(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Users'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(32), nullable=False)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    logined_at = db.Column('loginedAt', db.TIMESTAMP, nullable=False, default=datetime.now())

    index_openid = db.Index('idx_openid', openid)
