'''
請撰寫一程式，輸入四個分別含有小數1到4位的浮點數，然後將這四個浮點數以欄寬為7、欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

提示：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
四個浮點數

輸出說明
格式化輸出

輸入輸出範例
範例輸入
23.12
395.3
100.4617
564.329

範例輸出
|  23.12  395.30|
| 100.46  564.33|
|23.12   395.30 |
|100.46  564.33 |
'''
# TODO
num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
num4 = eval(input())
# 靠右對齊
# TODO
print("|%7.2f %7.2f|" % (num1, num2))
print("|%7.2f %7.2f|" % (num3, num4))
# 靠左對齊
# TODO
print("|%-7.2f %-7.2f|" % (num1, num2))
print("|%-7.2f %-7.2f|" % (num3, num4))