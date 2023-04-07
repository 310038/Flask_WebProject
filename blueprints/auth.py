from flask import Blueprint, render_template, redirect, url_for
from .forms import RegisterForm
from models import UserModel
from werkzeug.security import generate_password_hash
# 因為url_prefix(前綴)，所以以後在訪問此【auth】blueprint的網頁時，都要加上"/auth"這樣的前綴
bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login")
def login():
    return "這是登錄頁面"


# GET: 從服務器上獲取數據
# POST: 將客戶端的數據提交給服務器
@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        # form.validate() 會回傳 true/false
        if form.validate():
            username = form.username.data
            password = form.password.data
            UserModel(username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))
