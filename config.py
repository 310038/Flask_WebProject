# 資料庫配置訊息

# MySQL所在的主機名稱
HOSTNAME = "127.0.0.1"
# MySQL監聽的端口號，莫認為3306
PORT = 3306
# 連結MySQL的用戶名，讀者用自己設置的
USERNAME = "root"
# 連結MySQL的密碼，自己設置的
PASSWORD = "p0928956056"
# MySQL上創建的數據庫名稱
DATABASE = "qa"

# f"mysql+pymysql:~ 如果要連結其他資料庫，就自行把mysql改成其他資料庫的名稱
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI