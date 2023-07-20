import logging
import datetime

from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.user.model import User

# 初始化日志
logger = logging.getLogger('log')


def update_user_last_login_time(openid):
    try:
        user = User.query.filter(User.openid == openid).first()
        if user:
            user.logined_at = datetime.now()
        else:
            new_user = User(openid=openid)
            db.session.add(new_user)
        db.session.commit()
        return 
    except OperationalError as e:
        logger.info("update_user_last_login_time errorMsg= {} ".format(e))
        return None