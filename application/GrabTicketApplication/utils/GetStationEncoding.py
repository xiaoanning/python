#coding=utf-8

#获取车站编码
def getStationEncoding(stationName):
    if stationName == "北京":
        return "%u5317%u4EAC%2CBJP"
    if stationName == "天津":
        return "%u5929%u6D25%2CTJP"
    if stationName == "上海":
        return "%u4E0A%u6D77%2CSHH"
    if stationName == "营口东" :
        return "%u8425%u53E3%u4E1C%2CYGT"
    if stationName == "邓州":
        return "%u9093%u5DDE%2CDOF"
    if stationName == "南阳":
        return "%u5357%u9633%2CNFF"
    if stationName == "十堰":
        return "%u5341%u5830%2CSNN"
    if stationName == "郑州":
        return "%u90D1%u5DDE%2CZZF"
    if stationName == "齐齐哈尔":
        return "%u9F50%u9F50%u54C8%u5C14%2CQHX"
    if stationName == "杭州东" :
        return "%u676D%u5DDE%u4E1C%2CHGH"
    if stationName == "杭州" :
        return "%u676D%u5DDE%2CHZH"
    if stationName == "广州" :
        return "%u5E7F%u5DDE%2CGZQ"
    if stationName == "武汉" :
        return "%u6B66%u6C49%2CWHN"
    if stationName == "南京" :
        return "%u5357%u4EAC%2CNJH"
    if stationName == "成都" :
        return "%u6210%u90FD%2CCDW"
    if stationName == "东莞" :
        return "%u4E1C%u839E%2CRTQ"
    if stationName == "宁波" :
        return "%u5B81%u6CE2%2CNGH"
    if stationName == "日照" :
        return "%u65E5%u7167%2CRZK"
    if stationName == "汕头" :
        return "%u6C55%u5934%2COTQ"
    if stationName == "呼和浩特" :
        return "%u547C%u548C%u6D69%u7279%2CHHC"
    if stationName == "乌鲁木齐" :
        return "%u4E4C%u9C81%u6728%u9F50%2CWAR"
    if stationName == "大庆" :
        return "%u5927%u5E86%2CDZX"
    if stationName == "兰州" :
        return "%u5170%u5DDE%2CLZJ"
    if stationName == "丽水" :
        return "%u4E3D%u6C34%2CUSH"
    if stationName == "深圳" :
        return "%u6DF1%u5733%2CSZQ"
    if stationName == "沈阳" :
        return "%u6C88%u9633%2CSYT"
    if stationName == "温州" :
        return "%u6E29%u5DDE%2CRZH"
    if stationName == "海宁" :
        return "%u6D77%u5B81%2CHNH"
    if stationName == "南昌" :
        return "%u5357%u660C%2CNCG"
    if stationName == "青岛" :
        return "%u9752%u5C9B%2CQDK"
    if stationName == "台州" :
        return "%u53F0%u5DDE%2CTZH"
    if stationName == "贵阳" :
        return "%u8D35%u9633%2CGIW"
    if stationName == "哈尔滨" :
        return "%u54C8%u5C14%u6EE8%2CHBB"
    if stationName == "黄山" :
        return "%u9EC4%u5C71%2CHKH"
    if stationName == "西安" :
        return "%u897F%u5B89%2CXAY"
    if stationName == "银川" :
        return "%u94F6%u5DDD%2CYIJ"
    if stationName == "重庆" :
        return "%u91CD%u5E86%2CCQW"
    if stationName == "天水" :
        return "%u5929%u6C34%2CTSJ"
    if stationName == "安阳" :
        return "%u5B89%u9633%2CAYF"
    if stationName == "新乡" :
        return "%u65B0%u4E61%2CXXF"
    if stationName == "合肥" :
        return "%u5408%u80A5%2CHFH"
    if stationName == "武昌" :
        return "%u6B66%u660C%2CWCN"
    if stationName == "开封" :
        return "%u5F00%u5C01%2CKFF"
    if stationName == "海口" :
        return "%u6D77%u53E3%2CVUQ"
    if stationName == "长沙" :
        return "%u957F%u6C99%2CCSQ"
    if stationName == "长春" :
        return "%u957F%u6625%2CCCT"
    if stationName == "福州" :
        return "%u798F%u5DDE%2CFZS"
    if stationName == "济南" :
        return "%u6D4E%u5357%2CJNK"
    if stationName == "昆明" :
        return "%u6606%u660E%2CKMM"
    if stationName == "拉萨" :
        return "%u62C9%u8428%2CLSO"
    if stationName == "南宁" :
        return "%u5357%u5B81%2CNNZ"
    if stationName == "石家庄" :
        return "%u77F3%u5BB6%u5E84%2CSJP"
    if stationName == "太原" :
        return "%u592A%u539F%2CTYV"
    if stationName == "西宁" :
        return "%u897F%u5B81%2CXNO"
    if stationName == "厦门" :
        return "%u53A6%u95E8%2CXMS"
    if stationName == "邢台" :
        return "%u90A2%u53F0%2CXTP"
    if stationName == "" :
        return ""
    if stationName == "" :
        return ""
    if stationName == "" :
        return ""
    if stationName == "" :
        return ""
    if stationName == "" :
        return ""
    if stationName == "" :
        return ""
    if stationName == "" :
        return ""
    if stationName == "" :
        return ""
    if stationName == "" :
        return ""
    if stationName == "" :
        return ""
    if stationName == "" :
        return ""
    if stationName == "" :
        return ""

    print "没有录入此城市的编码 ： {} ".format(stationName)

