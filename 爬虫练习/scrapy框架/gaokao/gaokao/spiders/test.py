import requests
import json
import jsonpath
import re

def getCode():
    url  = 'https://api.eol.cn/gkcx/api/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
    }
    for page in range(103, 144):
        param = {
            "access_token": "",
            "admissions": "",
            "central": "",
            "department": "",
            "dual_class": "",
            "f211": "",
            "f985": "",
            "is_doublehigh": "",
            "is_dual_class": "",
            "keyword": "",
            "nature": "",
            "page": page,
            "province_id": "",
            "e": "",
            "request_type": "1",
            "school_type": "",
            "signsafranktype": "",
            "size": "20",
            "sort": "view_total",
            "top_school_id": "[659]",
            "type": "",
            "uri": "apidata/api/gk/school/lists"
        }
    response = requests.post(url = url,headers=headers)
    code_dict = json.loads(response.text)
    address = jsonpath.jsonpath(code_dict, '$..address')

    admissions = jsonpath.jsonpath(code_dict, '$..admissions')

    answerurl = jsonpath.jsonpath(code_dict, '$..answerurl')

    belong = jsonpath.jsonpath(code_dict, '$..belong')

    central = jsonpath.jsonpath(code_dict, '$..central')

    city_id = jsonpath.jsonpath(code_dict, '$..city_id')

    city_name = jsonpath.jsonpath(code_dict, '$..city_name')

    code_enroll = jsonpath.jsonpath(code_dict, '$..code_enroll')

    colleges_level = jsonpath.jsonpath(code_dict, '$..colleges_level')

    county_id = jsonpath.jsonpath(code_dict, '$..county_id')

    county_name = jsonpath.jsonpath(code_dict, '$..county_name')

    department = jsonpath.jsonpath(code_dict, '$..department')

    doublehigh = jsonpath.jsonpath(code_dict, '$..doublehigh')

    dual_class = jsonpath.jsonpath(code_dict, '$..dual_class')

    dual_class_name = jsonpath.jsonpath(code_dict, '$..dual_class_name')

    f211 = jsonpath.jsonpath(code_dict, '$..f211')

    f985 = jsonpath.jsonpath(code_dict, '$..f985')

    id = jsonpath.jsonpath(code_dict, '$..id')

    is_recruitment = jsonpath.jsonpath(code_dict, '$..is_recruitment')

    is_top = jsonpath.jsonpath(code_dict, '$..is_top')

    level = jsonpath.jsonpath(code_dict, '$..level')

    level_name = jsonpath.jsonpath(code_dict, '$..level_name')

    name = jsonpath.jsonpath(code_dict, '$..name')

    nature = jsonpath.jsonpath(code_dict, '$..nature')

    nature_name = jsonpath.jsonpath(code_dict, '$..nature_name')

    province_id = jsonpath.jsonpath(code_dict, '$..province_id')

    province_name = jsonpath.jsonpath(code_dict, '$..province_name')

    rank = jsonpath.jsonpath(code_dict, '$..rank')

    rank_type = jsonpath.jsonpath(code_dict, '$..rank_type')

    school_id = jsonpath.jsonpath(code_dict, '$..school_id')

    school_type = jsonpath.jsonpath(code_dict, '$..school_type')

    #code_dict
    print(school_id)
    #print(len(school_id))
#getCode()
def getoo():
    st1 = '''
        "address": "山东省济南市山大南路27号",
        "admissions": 1,
        "answerurl": "",
        "belong": "教育部",
        "central": 2,
        "city_id": 3701,
        "city_name": "济南市",
        "code_enroll": 1042200,
        "colleges_level": "",
        "county_id": 370112,
        "county_name": "历城区",
        "department": 1,
        "doublehigh": 0,
        "dual_class": 38001,
        "dual_class_name": "双一流",
        "f211": 1,
        "f985": 1,
        "id": "gkschool126",
        "is_recruitment": 1,
        "is_top": 2,
        "level": 2001,
        "level_name": "普通本科",
        "name": "山东大学",
        "nature": 36000,
        "nature_name": "公办",
        "province_id": 37,
        "province_name": "山东",
        "rank": 12,
        "rank_type": 11,
        "school_id": 126,
        "school_type": 6000,'''
    #st2 = re.findall(r'"(.*?)": ', st1)
    g = lambda x: x+" = jsonpath.jsonpath(code_dict,'$.."+x+"')"
    st2 = list(map(g,re.findall(r'"(.*?)": ', st1)))
    #address = jsonpath.jsonpath(code_dict, '$..address')
    for i in st2:
        print(i+'\n')
    #
getCode()