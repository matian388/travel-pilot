import config
import requests
from flask import blueprints, request
from wxcloudrun.response import make_succ_response

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
    return make_succ_response(resp)
