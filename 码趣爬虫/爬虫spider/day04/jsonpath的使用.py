import jsonpath

"""
    jsonpath是信息抽取库 是从json中抽取想要信息的工具
    {{[{}]}}
     http://www.lagou.com/lbs/getAllCitySearchLabels.json
"""
data = {
    "store": {
        "author": "鲸落",
        "book": [{
            "category": "reference",
            "author": "Nigel Rees",
            "title": "Sayings of the Century",
            "price": 8.95
        }, {
            "category": "fiction",
            "author": "Evelyn Waugh",
            "title": "Sword of Honour",
            "price": 12.99
        }, {
            "category": "fiction",
            "author": "Herman Melville",
            "title": "Moby Dick",
            "isbn": "0-553-21311-3",
            "price": 8.99
        }, {
            "category": "fiction",
            "author": "J. R. R. Tolkien",
            "title": "The Lord of the Rings",
            "isbn": "0-395-19395-8",
            "price": 22.99
        }],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "price": '12321313123123',
}
# print(data["store"]["book"][0]["category"])

# $ 是根节点  .. 不管什么位置 选择符合条件的数据  .子节点  * 所有元素 @ 表示当前元素节点 ?()支持过滤的操作
print(jsonpath.jsonpath(data, "$..author"))  # 所有的author数据
print(jsonpath.jsonpath(data, '$.store.book[*].author'))  # 所有book的author节点
print(jsonpath.jsonpath(data, '$.store.*'))  # store下的所有节点，book数组和bicycle节点和author
print(jsonpath.jsonpath(data, '$.store..price'))  # store下的所有price节点
print(jsonpath.jsonpath(data, '$..book[2]'))  # 匹配第3个book节点
print(jsonpath.jsonpath(data, '$..book[(@.length-1)]'))  # 匹配倒数第1个book节点
print(jsonpath.jsonpath(data, '$..book[-1:]'))  # 匹配倒数第1个book节点
print(jsonpath.jsonpath(data, '$..book[:2]'))  # 匹配book的前两个
print(jsonpath.jsonpath(data, '$..book[?(@.isbn)]'))  # 过滤含isbn字段的节点
print(jsonpath.jsonpath(data, '$..book[?(@.price<10)]'))  # 过滤price<10的节点
