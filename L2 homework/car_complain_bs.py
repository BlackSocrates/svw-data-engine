import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_page_concent(request_url):
    # 请求URL
    url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1.shtml'
    # 得到页面的内容
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=10)
    content = html.text
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup

# 分析当前界面的投诉
def analysis(soup):
    temp = soup.find('div', class_ = 'tslb_b')

    # 创建DataFrame
    df = pd.DataFrame(columns= ['id','brand','car_model','type','desc','problem','datetime','status'])

    tr_list = temp.find_all('tr')
    for tr in tr_list:
        # 提取汽车投诉信息
        temp = {}
        td_list = tr.find_all('td')
        if len(td_list) > 0:
            id, brand, car_type, model, desc, problem, datetime, status = td_list[0].string, td_list[
                1].string, td_list[2].string, td_list[3].string, td_list[4].string, td_list[5].string, td_list[6].string, \
                                                                                                td_list[7].find('em').string
            temp['id'], temp['brand'], temp['car_model'], temp['type'], temp['desc'], temp['problem'], \
            temp['complain_time'], temp[
                'status'] = id, brand, car_type, model, desc, problem, datetime, status
            df = df.append(temp, ignore_index=True)
    return df

'''df = analysis(soup)
print(df)'''

page_num = 20
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1'
result = pd.DataFrame(columns= ['id','brand','car_model','type','desc','problem','datetime','status'])
for i in range(page_num):
    request_url = base_url + str(i+1) + '.shtml'
    soup = get_page_concent(request_url)
    df = analysis(soup)
    print(df)
    result = result.append(df)

# 导出
result.to_csv('car_complain_bs.csv',index = False)
