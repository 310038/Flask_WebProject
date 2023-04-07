from flask import Flask
import config
from exts import db  # db=SQLAlchemy()放在exts.py中
from models import UserModel  # UserModel放在models.py中
from blueprints.qa import bp as qa_bp  # 導入qa的bp進來跟app.py做串接
from blueprints.auth import bp as auth_bp  # 導入auth的bp進來跟app.py做串接
from flask_migrate import Migrate

app = Flask(__name__)
# 綁定配置文件
app.config.from_object(config)

# 下面這行用來讓 db 跟 app 做綁定。先創建，再進行綁定
db.init_app(app)

# 遷移資料庫
migrate = Migrate(app, db)

# 註冊藍圖，配合上面的 from blueprints.qa import~
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

# blueprint:用來做模塊區分的
# 電影、讀書、音樂、.....

# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute("select 1")
#         print(rs.fetchone())

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
