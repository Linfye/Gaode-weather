import requests
import pandas as pd
import os

def WeatherJsonGot(cityID):
    r = requests.get('https://restapi.amap.com/v3/weather/weatherInfo?city=' + cityID + '&extensions=base&key=e9e460555a9d45e7375444b513e0043b')
    w = r.json()
    return w

def WeatherGot(cityID):
    weather = WeatherJsonGot(cityID)
    provi = weather['lives'][0]['province']    #省份名
    cityn = weather['lives'][0]['city']        #城市名
    weath = weather['lives'][0]['weather']     #天气现象
    tempe = weather['lives'][0]['temperature'] #实时气温 
    windd = weather['lives'][0]['winddirection'] #风向描述
    windp = weather['lives'][0]['windpower']   #风力级别，单位：级
    humid = weather['lives'][0]['humidity']    #空气湿度
    repor = weather['lives'][0]['reporttime']  #数据发布的时间
    tempe=tempe.replace("-","零下")
    return "当前地区:\t\t{}\n当前天气:\t\t{}\n温度:\t\t\t{}度\n户外:\t\t\t刮{}风, 强度{}级\n空气湿度:\t\t{}\n数据更新时间:\t\t{}".format(cityn, weath, tempe, windd, windp, humid, repor)


def find(cityName):
    cityIDXLSX = pd.read_excel('E:\\documents\\Project\\Python\\release\\WEA\\cityID.xlsx', sheet_name='Sheet1')
    for i in range(cityIDXLSX.shape[1]):
        for j in range(cityIDXLSX.shape[0]):
            if cityIDXLSX.iloc[j, i] == cityName:
                return cityIDXLSX.iloc[j, i+1]

cityName = input("请输入城市区域名：")
os.system('cls') 
print(WeatherGot(str(find(cityName))))

x =input("\n按回车退出")
