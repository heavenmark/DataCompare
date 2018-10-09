import difflib
import out
import data


def compare_html(ad1,ad2):                             #输出html的对比结果
    hd = difflib.HtmlDiff()
    loads = ''
    with open('%s'%ad1,'r') as load:
        loads = load.readlines()
    mems = ''
    with open('%s'%ad2, 'r') as mem:
        mems = mem.readlines()
    with open('htmlout.html','w+',encoding='UTF-8') as fo:
        fo.write(hd.make_file(loads,mems))


def compare_kong(data0, data1,kong,key):              #检查空字段
    if data1[key] == '' and data0[key] != data1[key]:
        kong.append({key: data1[key]})


def compare_bool(data0, data1, booL, key):              #检查值为布尔类型的字段
    if type(data1[key]) == bool and data0[key] != data1[key]:
        booL.append({key: data1[key]})


def compare_num(data0, data1,num,key):                #检查所有不同字段
    if data0[key] != data1[key]:
        num.append(key)


def compare_typo(data0, data1,typo,key):              #检验字段类型
    if type(data1[key]) != type(data0[key]):
        typo.append({key: data1[key]})


def compare_plus(data0, data1,key):              #新增字段
    if key not in data0:
        print('新增字段：'+str({key: data1[key]}))


def compare_less(data0, data1,key):              #缺失字段
    if key not in data1:
        print('缺失字段：'+str({key: data0[key]}))


def compare_data(data0, data1):
    kong=[]
    booL=[]
    num=[]
    typo=[]
    for key in data1:
        try:
            compare_kong(data0,data1,kong,key)
            compare_bool(data0, data1, booL, key)
            compare_num(data0,data1,num,key)
            compare_typo(data0,data1,typo,key)
        except KeyError:
            pass
        compare_plus(data0,data1,key)
    for key in data0:
        compare_less(data0,data1,key)
    if len(kong)>0:
        print('不相同的空字段:'+str(kong))
    if len(booL)>0:
        print('不相同的布尔型字段:'+str(booL))
    if len(num)>0:
        print('所有不相同的字段:'+str(num))
    if len(typo)>0:
        print('类型不同的字段:'+str(typo))
    L=kong+booL+num+typo
    return L


def compare_out():
    data0 = data.data0      #参考数据
    data1 = data.data1      #待测数据
    print('----------------rcode外字段---------------')
    compare_data(data0, data1)
    print('\n'+'----------------rcode内字段-----------------')
    compare_data(data0['rcode'], data1['rcode'])


if __name__ == '__main__':
    ad1='d:/我的文档/桌面/new.txt'
    ad2='d:/我的文档/桌面/fireye.txt'
    data1=data.data1
    json1=out.jsonout(data1)
    out.writeout(json1,ad1)
    data0=data.data0
    json0=out.jsonout(data0)
    out.writeout(json0,ad2)
    compare_out()
    compare_html(ad1,ad2)


