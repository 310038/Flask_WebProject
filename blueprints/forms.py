import wtforms
from wtforms.validators import Email, Length, EqualTo

# Form: 主要用來驗證前端送過來的數據是否符合要求
class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="username格式錯誤!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="password格式錯誤!")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password",message="兩次密碼不一致!")])

