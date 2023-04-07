from flask import Blueprint

bp = Blueprint("qa", __name__, url_prefix="/")

# qa跟首頁是同一個頁面，所以不再設定新的頁面給qa
@bp.route("/")
def index():
    return "hello world"