# author:lyr time:2019-11-01
import requests
rp=requests.get('http://ci.ytesting.com/api/3school/school_classes?'
                'vcode=<vode>&action=list_classes_by_schoolgrade')
print(rp.status_code)
print(rp.url)
print(rp.text)
print(rp.content)
print(rp.headers)
1111
