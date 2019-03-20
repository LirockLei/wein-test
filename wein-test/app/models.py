from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Goods(db.Model):
    """商品信息"""

    __tablename__ = "jd_goods"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    # 商品id
    title = db.Column(db.String(256), nullable=False)    # 商品名称
    img_url = db.Column(db.String(256))  # 商品图片路径
    price = db.Column(db.String(32))  # 商品价格
    detail = db.Column(db.String(1024))   # 商品详情介绍
