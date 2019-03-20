import os
import uuid

from flask import Blueprint, render_template, session, jsonify, request

from app.models import Goods, db

goods_blue = Blueprint('goods', __name__)


# 展示商品页面
@goods_blue.route('/all_goods/', methods=['GET'])
def all_goods():
    return render_template('all_goods.html')


# 查询所有商品
@goods_blue.route('/show_all_goods/', methods=['GET'])
def show_all_goods():
    goods_list = Goods.query.all()
    data = [goods.to_dict() for goods in goods_list]
    return jsonify({'code': 200, 'msg': '请求成功', 'data': data})


# 删除商品
@goods_blue.route('/del_goods/', methods=['DELETE'])
def del_goods():
    goods_id = request.form.get('goods_id')
    goods = Goods.query.filter_by(id=goods_id).first()
    db.session.delete(goods)
    db.session.commit()
    return jsonify({'code': 200, 'msg': '删除成功'})


# 添加商品
@goods_blue.route('/add_goods/', methods=['POST'])
def add_goods():
    # 获取用户输入信息
    title = request.form.get('title')
    img = request.files.get('img')
    price = request.form.get('price')
    detail = request.form.get('detail')

    # 保存图片
    if img:
        # 获取项目根路径
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 获取媒体文件路径
        MEDIA_DIR = os.path.join(BASE_DIR, 'static/media')
        # 随机生成图片名称
        filename = str(uuid.uuid4())
        i = img.mimetype.split('/')[-1]
        image = filename + '.' + i
        # 拼接图片地址
        path = os.path.join(MEDIA_DIR, image)
        img.save(path)
        img_url = '/static/media/' + image
    else:
        img_url = ''

    # 存储到数据库
    goods = Goods()
    goods.title = title
    goods.img_url = img_url
    goods.price = price
    goods.detail = detail
    db.session.add(goods)
    db.session.commit()

    return jsonify({'code': 200, 'msg': '添加成功'})


# 按价格查询商品
@goods_blue.route('/select_by_price/', methods=['POST'])
def sel_goods_by_price():
    max_price = request.form.get('max_price')
    min_price = request.form.get('min_price')
    goods_list = Goods.query.filter(Goods.price > min_price, Goods.price < max_price).all()
    data = [goods.to_dict() for goods in goods_list]
    return jsonify({'code': 200, 'msg': '请求成功', 'data': data})


# 按品牌查询商品
@goods_blue.route('/select_by_title/', methods=['POST'])
def sel_goods_by_title():
    title = request.form.get('title')
    goods_list = Goods.query.filter(Goods.title.contains(title)).all()
    data = [goods.to_dict() for goods in goods_list]
    return jsonify({'code': 200, 'msg': '请求成功', 'data': data})