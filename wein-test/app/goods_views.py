from flask import Blueprint, render_template, session, jsonify, request

from app.models import Goods


goods_blue = Blueprint('goods', __name__)


