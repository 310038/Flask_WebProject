# exts.py:這個文件的存在，是為了解決循環引用的問題。

# flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()