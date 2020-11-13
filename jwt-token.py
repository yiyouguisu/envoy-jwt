import jwt
import string
import random
import time
import binascii
import uuid
import base64
import datetime


if __name__ == '__main__':
    # df_test_thumbprint = "FE:7C:EC:09:DC:64:92:8F:8A:95:6D:76:2D:0B:DE:06:8D:55:15:36"

    # thumbprint = df_test_thumbprint
    # thumbprint = thumbprint.lower().replace(' ', '').replace(':', '')
    # hex_val = binascii.a2b_hex(thumbprint)

    now = datetime.datetime.now()
    minutes = datetime.timedelta(0, 0, 0, 0, 365 * 24 * 60 * 60)
    expires = now + minutes

    header = {
        "alg": "RS256",
        "typ": "JWT",
        "kid": "test",
        # "x5t": base64.urlsafe_b64encode(hex_val).decode()
    }

    payload = {
        "aud": "http://www.service.com",
        # "aud": "https://login.chinacloudapi.cn/%s/oauth2/token" % (df_test_tenant,),
        "exp": int(time.mktime(expires.timetuple())),
        "iss": "www.service.com",
        "jti": str(uuid.uuid4()),
        "nbf": int(time.mktime(now.timetuple())),
        "sub": "www.service.com"
    }

    df_test_certificate = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAr6ng+DmStdyo/GJD/ngHUmrGKEIVOL/zFlO36m+OjsJYcJKU
BzNWhSO+lKWhNZ6cXn3DQg0ZbNMLkL90pih6+BvBSrS7vJDR2C9Oefjyr4oN2wU5
ZPIloECaxLF8hwMcnKkLDhobwJ1HOTB4V3WrkOZXgE5HjY119UZ1crwpdTka1gaT
PorvC2YlIo9/1nu7Vrt5Hp0DYp0JZVHFFhm1FNM8FIYw16BA2JcKjhQI89Pw/s65
hvAri6FgVappXzlj0nF4ShVTG/NA0W1Gw6dCv9ITrH43yAwy21PiCs0mi8NeDqd0
KRN33ucxrAq5na7VwgLhipic1FoX9iGnyuNwHwIDAQABAoIBAFZ8IuDTJ6IWE7S+
hI9idOhk3U6wylX4Wywg56mqZttuX7B82hh5dB10rb3tleMaRg5XiKyaWmwzs7v+
JuYvg+tnbtDjDpMWEdqH3/E5WfKG2697cPh8J34wkIJKh+7I32tZ5rF4tTUtugU0
EeutaVybq3TmFWBhxzONDwIAFcE6HPo9PmjoAVw7SXclRhLoGkuuBi8Gku0roRFj
46/xqxWLZAvHzrJ6C81ljhYqRR56YjpFfscaiNP8g1HstYony6N8H/dJJ9b4XAXO
ccJxwzEcxwNHkTrjOrirIvRs76jAZvi2q9ITOhEPzGYTPwB5WND+shksoq678HV4
lgbfbSECgYEAxv9SW/NDdtJagBT/vSLhV8lblw3mIpl+wOyQ31wvnRpb1gXljtGy
vUE9xYLJUxR45AU151jmJUkZyj+TqvAZS/IRI+7yWGYbLj7ai98nMvBDVNEb76L4
SlzLNwizaHQiqnbQ4HOcRXs1cvnDZlm49Zf84Oo5OUy5Dblz8zPpqtcCgYEA4ft3
9a2kaC2lpaL8TfVkDAaKcUAreistwKoYfx/bL3Qbgn/U5gwkZkmJYsh7/I8VObfD
LjXFuoyPPX3BQDZe1lzhFm1whI40NfDz8QL4hPU+nFPZkvmkpOmxNscitRTp71wA
n4pgG42OMFQvAbzHAcUjUWl2kr4NPC249buKQ/kCgYBuRTWCNn7/7PixWPGOATIV
z0KtpcoNCjmu9mghHZhU2jJhmsrmJVWCghCUzjB5lTKYSDrig+SkbKmZ5TkS1BFw
gCb3XoV0bsBJFBNOxs2V8IWfDnEIjapAqsMBMBUaoKBFDaoZdnb2GZw4piadJMLV
dO9wQtqK4fT5ofaaof2t6QKBgQDC7ZptZkoBvxY6yVtfl8OkB+RViie2qxY9MbwN
tBnqVfoA2Gl5wpGHVflXJ16j3XxOnC+VZbbYkrRgM2CGFiA6QkW6hc5f2RY6TUzu
4UQj1DQcvstX11VpF1fQy3cpwg+Ec9TpyX/bZIB5ObSOiBsVcMplSFaKf7uE5F++
P/YlaQKBgFWAGn8/YumNl6x5Uo8MfUOBCOqwNFajB8Z9oy2rUHqXC96RxAbSzW5I
T7sQ5u2pbJ0gIKwUWZX57vmqohKTTKvdP44Go8DgR+XIHoDNIOz8EY8+U6JBrbgb
yxiHlvfP5ezRYADogIBxaMPqlcSvgWc+PrPkAmhtg6xuqZBMNYcN
-----END RSA PRIVATE KEY-----"""

    

    certificate = df_test_certificate
    token = jwt.encode(payload=payload, key=certificate, algorithm='RS256', headers=header).decode()

    print token

