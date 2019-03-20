from flask import Flask, render_template
from flask_script import Manager

from app.goods_views import goods_blue
from app.models import db

app = Flask(__name__)

app.register_blueprint(blueprint=goods_blue, url_prefix='/goods')

# 初始化数据库的配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@119.23.253.128:3306/jd_text'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.secret_key = '123ashufaihsufifs'

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
