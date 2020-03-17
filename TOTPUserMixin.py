import pyotp
import qrcode


class TOTPUserMixin(object):
    # 生成 secret_key函数

    @staticmethod
    def get_secret_key(self):
        gtoken = pyotp.random_base32()
        return gtoken

    # 生成二维码的函数
    @staticmethod
    def get_qrcode(self, data, user_name):
        qr_uri = pyotp.totp.TOTP(data).provisioning_uri(user_name)  # 获取二维码 URI
        img = qrcode.make(qr_uri)  # 生成二维码
        return img

    # 验证token模块
    @staticmethod
    def check_token(self, secret_key, user_token):
        totp = pyotp.TOTP(secret_key)
        return totp.verify(user_token)


user = TOTPUserMixin()

'''
功能说明：

1、get_secret_key：
调用get_secret_key会返回一个secret_key,例：ICD7YRTNF5EXZ3EW
    用户可根据自身条件选择在移动设备上输入此字符串或者等待扫描二维码
    传入参数：无
调用格式：secret_key = user.get_secret_key(

2、get_qrcode：
调用get_qrcode会生成二维码并返回二维码，同时为了区分还要传入用户名以达到
    用户在手持设备上可清晰辨认出属于此项目的token，
    传入参数：用户的secret_key,用户名:user_name
调用格式：images = user.get_qrcode(secret_key,user_name)

3、Verification：
调用Verification会进行验证某一用户的token，返回值有两种情况，1、True 2、False,
    传入参数：用户的secret_key、用户输入的token
    调用格式：user.Verification(secret_key=secret_key,user_token=us_token)

测试范例：

# user = TOTPUserMixin()
# 生成key
secret_key = user.get_secret_key()

user_name = 'andy.zhao'
# 加载key 生成二维码
images = user.get_qrcode(secret_key,user_name)
images.show()

us_token = int(input("请输入你的6位数token--->"))
if user.check_token(secret_key=secret_key,user_token=us_token):
    print("验证成功")
else:
    print("验证失败")

测试结果:

安卓端APP:Google Authenticator（Google身份验证器）
结果:安卓端不可扫描二维码,可输入secret_key,验证成功

安卓端:FreeOTP
结果:可扫描二维码,可输入secret_key,验证成功

安卓端;Authy
结果:可扫码,可输入secret_key,验证成功,
'''
