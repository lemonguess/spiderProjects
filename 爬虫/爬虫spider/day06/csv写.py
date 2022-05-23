"""
    csv 文件是大数据文件存储格式的文件  结构与excel不同。
CSV是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用。最广泛的应用是在程序之间转移表格数据，而这些程序本身是在不兼容的格式上进行操作的（往往是私有的和/或无规范的格式）。
因为大量程序都支持某种CSV变体，至少是作为一种可选择的输入/输出格式。
例如，一个用户可能需要交换信息，从一个以私有格式存储数据的数据库程序，到一个数据格式完全不同的电子表格。最可能的情况是，该数据库程序可以导出数据为“CSV”，然后被导出的CSV文件可以被电子表格程序导入。
"""
import csv

headers = ('name', 'age', 'height')
# student = [
#     ["马尔扎哈", 2000, 110],
#     ("古力娜扎", 18, 180),
#     ("鲸落", 18, 200),
#     ("努纳札札", 118, 100),
#     ("小鬼哈哈", 618, 120),
#     ("北斗", "78岁", 10),
# ]
# student2 = ("努尔哈赤", 111, 175)
# # newline=""解决空行
# with open("student.csv", 'w', encoding="utf-8",newline="")as f:
#     writer = csv.writer(f)
#     writer.writerow(headers)
#     writer.writerows(student)
#     # writer.writerows(student2) # 报错
#     # writer.writerow(student2)

student3 = [
    {"name": "马尔扎哈", "age": 1111, "height": 198},
    {"name": "鲸落", "age": 18, "height": 200},
    {"name": "北斗", "age": "7888888888岁", "height": 10}
]
with open("student.csv", 'w', encoding="utf-8", newline="")as f:
    writer = csv.DictWriter(f, headers)
    # 虽然DictWriter创建的时候有一个headers，但是想要写入数据进去，还是需要调用
    # writer.writeheader()方法，否则，表头数据写入不进去
    writer.writeheader()
    writer.writerows(student3)