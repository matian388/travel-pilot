import config
import requests
from flask import blueprints, request
from wxcloudrun.user.dao import update_user_last_login_time
from wxcloudrun.response import make_succ_response, make_err_response

user_api = blueprints.Blueprint('user_api', __name__)


@user_api.route('/code2session', methods=['GET'])
def code2session():
    js_code = request.args.get('code')
    resp = requests.get('https://api.weixin.qq.com/sns/jscode2session', params={
        'grant_type': 'authorization_code',
        'appid': config.appid,
        'secret': config.secret,
        'js_code': js_code,
    }).json()
    if resp.get('errcode', 0) != 0:
        return make_err_response(resp['errmsg'])
    update_user_last_login_time(resp['openid'])
    return make_succ_response(resp)
        
@user_api.route('/error', methods=['GET'])
def error_test():
    return make_err_response('test')
        
