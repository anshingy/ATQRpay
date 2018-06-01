#-*- coding: utf-8 -*-
from flask import Flask,redirect,render_template,request
from urllib.parse import quote
app = Flask(__name__)
def pureStr(s):
    after=(s.strip()).lstrip()
    return after
@app.route('/')
def ATpay():
    UA=request.headers.get('USer-Agent')
    if('MicroMessenger' in UA):
        linktype='wepay'
        name='微信支付'
        Ourl="f2f0k4UBKRJSvJtZm0FHZOtLlqXuQw0adQ_P"
        Rurl=pureStr(str(Ourl.encode(encoding="UTF-8")))
        qr_img='img src="http://qr.liantu.com/api.php?text="'+Rurl+'"'
        icon_img='img src="http://ww2.sinaimg.cn/large/005zWjpngy1fojrwgr20oj303k03kglg.jpg" width="48px" height="48px" alt="'+name+'"'
    elif('AlipayClient' in UA):
        QRurl="HTTPS://QR.ALIPAY.COM/FKX06606HNZBHPXVJ5QMB8?t=1527829614642"
        return redirect(QRurl)
    elif('QQ/' in UA):
        linktype='qq'
        name='QQ钱包支付'
        Ourl="https://i.qianbao.qq.com/wallet/sqrcode.htm?m=tenpay&f=wallet&u=545260251&a=1&n=Trickster&ac=C781D9E156290EA0981B8735450DAD57E68961EA8F03F5162704323CF897BF2C"
        icon_img = 'img src="http://ww2.sinaimg.cn/large/005zWjpngy1fojrvmp427j303k03kjrb.jpg" width="48px" height="48px"  alt="'+name+'"'
        Rurl=pureStr(str(Ourl.encode(encoding="UTF-8")))
        qr_img='img src="http://qr.liantu.com/api.php?text="'+Rurl+'"'
    else:
        linktype='other'
        name='打赏作者'
        Ourl='www.baidu.com'
        Rurl=pureStr(str(Ourl.encode(encoding="UTF-8")))
        qr_img='img src="http://qr.liantu.com/api.php?text="'+Rurl+'"'
        icon_img='img src="http://ww2.sinaimg.cn/large/005zWjpngy1fojs089x6tj303k03kjr6.jpg" width="48px" height="48px" alt="'+name+'"'
    return render_template('index.html',name=name,linktype=linktype,icon_img=icon_img,qr_img=qr_img)
if __name__ == '__main__':
    app.run()
