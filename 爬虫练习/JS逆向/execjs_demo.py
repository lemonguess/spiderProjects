import execjs

#方式一：eval直接执行JS代码（适合简单且有返回值的少量JS代码）
res = execjs.eval('"maqu edu yige".split(" ")')
print(type(res),res)

#方式二：compile加载JS代码，call调用，类似于re正则，先compile定义，再call调用

js_code = """
    var a = 5
    function add(x,y){
        return x+y;
    }
"""
js_ex = execjs.compile(js_code) #加载JS代码,返回编译后的JS对象，JS代码可以没有返回值
res = js_ex.call('add',1,2) #要执行的函数名，传入函数的参数，多个用逗号隔开
print(res)