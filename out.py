import json
import data


def textout(address):
    data = ''
    with open('%s'%address, 'r',encoding='UTF-8') as mem:
        data = mem.readlines()
        mem.close()
    print(data)
    return data


def jsonout(data):
    # json_dict = json.loads(json_dict)          #json转化成字典
    json_dict = data
    rcode = json_dict.pop('rcode')
    data1 = rcode.pop("sensors")
    data2 = rcode.pop("appList")
    data3 = rcode.pop("processList")
    json_dict.update({'rcode':rcode})
    json_dict = json.dumps(json_dict, indent=4)    #字典转换成json格式
    # print('-----------------------剔除的字段-----------------------')
    # print("sensors")
    # print("appList")
    # print("processList")
    return json_dict


def writeout(json,ad1):
    with open('%s'%ad1, 'w+', encoding='UTF-8') as lo:
        for i in range(0, len(json), 10):
            lo.write(json[i:i + 10])
    return json


if __name__ == '__main__':
    ad1='d:/我的文档/桌面/new.txt'
    ad2='d:/我的文档/桌面/fireye.txt'
    data1=data.data1
    json1=jsonout(data1)
    writeout(json1,ad1)
    data0=data.data0
    json0=jsonout(data0)
    writeout(json0,ad2)


