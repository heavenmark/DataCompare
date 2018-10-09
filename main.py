import compare
import data
import out

'''
火眼上报数据校验，其中剔除了"sensors"、"appList"、"processList"三个内容比较冗余的字段
'''


if __name__ == '__main__':
    ad1='d:/我的文档/桌面/new.txt'
    ad2='d:/我的文档/桌面/fireye.txt'
    data1=data.data1
    json1=out.jsonout(data1)
    out.writeout(json1,ad1)
    data0=data.data0
    json0=out.jsonout(data0)
    out.writeout(json0,ad2)
    compare.compare_out()
    compare.compare_html(ad1,ad2)


