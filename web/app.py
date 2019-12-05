from web.utils import load_config
from web.logger import setup_log
from flask import Flask, request, render_template, session, redirect, url_for
from web.utils import mysql
import math

config = load_config()
logger = setup_log(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = '87787763@qq.com'
mysql = mysql(config['mysql'])

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    主要介绍页面
    """
    login_status, user_id = False, ''

    # 登录状态检测
    if 'user_id' in session:
        login_status, user_id = True, session['user_id']

    return render_template('Index.html',
                           login=login_status,
                           userid=user_id,
                           name="index")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录页面
    """
    return render_template()


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    注册
    :return: Register.html
    """
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            age = request.form['age']

            try:
                sql = "insert into User (UserID,Location,Age) values ('{}','{}','{}')".format(username, password, age)
                mysql.exe(sql)
                logger.info("username:{},password:{},age:{} register success".format(username, password, age))
            except Exception as e:
                mysql.rollback()
                logger.exception("username:{},password:{},age:{} register filed".format(username, password, age))
            return render_template('Login.html')
    except Exception as e:
        logger.exception("register function error: {}".format(e))
        return render_template('Register.html', error='注册出错')


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    """
    推荐页面
    """
    return render_template()


@app.route('/selfInfo', methods=['GET', 'POST'])
def selfInfo():
    """
    个人信息页面
    """

    return render_template()


if __name__ == '__main__':
    app.run()
