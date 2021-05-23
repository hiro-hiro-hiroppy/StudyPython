if True:
    print('hoge')
    print('fuga')

val = 10
val = val + 10
print(val)

# コメント

'''
コメント
複数行
'''

# 演算
val1 = 1 + 2
val2 = 10 - 5
val3 = 10 * 2
val4 = 2 ** 3
val5 = 10 / 3
val6 = 10 // 3
val7 = 10 % 3

# 比較演算子
# ==
# !=
# >
# >=
# <
# <=
# is     同一オブジェクト
# is not 異なるオブジェクト
# in     aがbに含まれる
# not in aがbに含まれない

# 論理演算子
# and
# or
# not

# ビット演算子
# &  論理積
# |  論理和
# ^  排他的論理和
# << 左シフト
# >> 右シフト
# -  ビット反転

# 三項演算
val = 1
print('OK' if val > 0 else 'NG')

# 文字列演算
# +       文字列の連結
# *       文字列を繰り返し結合する
# [n]     n番目の文字を切り出す
# [n:m]   n~m-1番目の文字を切り出す
# [n:]    n番目以降の文字を切り出す
# [:m]    m-1番目までの文字を切り出す
# [n:m:s] n~m-1番目の文字をs個飛ばしで切り出す

# 数値型
# 整数型 Integer
# 浮動小数点数 Float
# 複素数 数値に添字「j」 c1 = 1 + 1j

# 真偽値
# False 0
# True 1

# 文字列
# '   シングルクォートで囲う
# "   ダブルクォートで囲う
# ''' 3重のシングルクォートで囲う 複数行
# """ 3重のダブルクォートで囲う   複数行

# 末尾にバックスラッシュを使用すると改行が無効になる

# リスト型
lst = ['hoge', 10, True]
print(lst[1])
lst[1] = 999

# 負数の場合は末尾から
lst[-1] # True

# 辞書型
dict1 = {'key1': 'value1', 'key2': 'value2','key3': 'value3'}

# タプル型（リスト型に似ているが要素の変更が行えない）
tuple1 = ('hoge', 999, False)
tuple2 = ('hoge',)

# 集合型（重複した値を持たない）
# ({ }) set
sets1 = {'hoge', 999, True}
sets2 = set(['hoge', 999, True])
sets3 = set('hogehoge')

# None
None

# ifelse
val1 = 1
val2 = 2
if val1 == val2:
    print('hoge')
elif val1 > val2:
    print('fuga')
else:
    print('boo')

# 範囲指定も可能
if 1 < val2 < 3:
    print('foo')

# switch文ライクな書き方
val3 = 3
if val3 == 1:
    print('hoge')
elif val3 in (2, 3):
    print('fuga')
else:
    print('boo')

# Noneの比較には「is」や「is not」を使う
data = None
if data is None:
    print('OK')

# 繰り返し
# while文
val1 = 1
while val1 < 3:
    print(val1)
    val1 += 1

# for文とrange関数
for i in range(2):
    print(i)

# for文と文字列(リストや辞書なども使用可能)
for c in 'hoge':
    print(c)

# 関数
def fnc(a, b=1):
    return a + b

def fnc1(a, b=[]):
    b.append(a)
    return b

def fnc2(a, b=None):
    if b is None:
        b = []

    b.append(a)
    return b

def fnc3(a,b,c):
    print(a,b,c)
fnc3(c=3, a=1, b=2) # 1 2 3

# 例外処理
# try~except~else~finally
try:
    x = 10 / 0
except Exception as e:
    print(e)
else:
    # 例外が発生しなかった場合に行う処理
    print('hoge')
finally:
    print('fuga')

try:
    raise Exception('hoge')
except Exception as e:
    print(e)

# pass文（何もしない）
for i in range(10):
    if(i % 2) == 0:
        print(i)
    else:
        pass

def hogehoge():
    pass

# モジュールのインポート
# sub.pyをインポート
# import sub

# sub.pyのsubFncをインポート
# from sub import subFnc

import calendar
print(calendar.month(1999,12))

# ビルトインスコープ
# モジュールスコープ
# ローカルスコープ

# クラス
class Member:
    # クラス変数
    LANG = 'JP'

    # コンストラクタ
    def __init__(self):
        self.name = ''

    # ゲッタ
    def getName(self):
        return self.name

    # セッタ
    def setName(self, name):
        self.name = name

taro = Member()
taro.setName('太郎')
print(taro.getName())
print(Member.LANG)

# クロージャ
# 関数のローカル変数を参照するような関数
# nonlocalによって一つ外側のスコープに属する変数の代入が可能
def counter():
    count = 0

    def inner_counter():
        nonlocal count
        count += 1
        return count
    
    return inner_counter

cnt = counter()
print(cnt())

# ファイル操作 open関数
f = open('text/hoge.txt', 'w', encoding="UTF-8")

f.write('fugafuga')

f.close()

# リスト、辞書、タプル、集合の活用

# リスト
print(['a', 'b', 'c'] + [1, 2, 3])
print(len(['a', 'b', 'c']))
lst = ([1, 2], [3, 4], [5, 6])

# 辞書
dict1 = {
    'apple':'red'
    , 'grape':'purple'
    , 'banana':'yellow'
    }

dict2 = dict(one=1, two=2, three=3)

# キーの存在確認
print('apple' in dict1)
print('zero' in dict2)

# 操作いろいろ
for k, v in dict1.items():
    print(k, v)

for k in dict2.keys():
    print(k, dict2[k])

for v in dict1.values():
    print(v)

# タプルの生成
key1 = ('まさる', '10-18')
key2 = ('まなぶ', '05-01')

dict = {key1:38, key2:25}

# 集合
lst = ['hoge', 'fuga', 'boo', 'fuga', 'boo']

sets = set(lst) #重複が削除される

# 集合の演算
sets1 = {'A', 'B', 'C', 'D'}
sets2 = {'A', 'C'}

# A - B
# A & B
# A ^ B
# A | B
# A <= B
# A >= B


# さまざまな引数
# 通常の引数
def fnc(a):
    print(a)
    
# デフォルト値付き
def fnc2(a=1):
    print(a)

# 可変調の引数
def fnc3(a,b,*args):
    print(a,b,args)

# キーワード付きの可変調引数
def fnc4(a,b,**args):
    print(a,b,args)
    
# 利用頻度の高い組み込み関数
# コンソール出力だけでなく、ファイルに書き出したりできる
# end引数で末尾を変更できる
print('hoge', end='■')

# 区切り文字の指定(sep)
print('hoge', 'fuga', 'boo', sep=',')

# ファイルに出力する
f = open('hoge.txt', 'w', encoding='UTF-8')
# hoge.txtに「hogefuga」と出力される
print('hogefuga', file=f)
f.close()

# フォーマット出力
# hoge-fuga-boo
print('%s-%s-%s-' % ('hoge','fuga','boo'))

# len
# オブジェクトの要素数
# 文字列
str = 'あいうえおaiueo'
print(len(str)) # 10

# リスト
lst = ['a',1,False]
print(len(lst)) # 3

# 辞書
dict = {'a':'a', 'b':'b', 'c':'c'}
print(len(dict))

# タプル
tpl = (1,2,3,4,5)
print(len(tpl))

# 集合
sets = set('hoge')
print(len(sets))

# min(),max()
# 数値
min(1,2,3,4,5) #1
max(1,2,3,4,5) #5

# リスト
lst = [1,2,3]
min(lst) # 1
max(lst) # 3

# 辞書(keyが対象となる)
dict = {1:9, 2:8, 3:7}
min(dict) # 1
max(dict) # 3

# タプル
tpl = (1,2,3,4,5)
min(tpl) # 1
max(tpl) # 5

# 集合
sets = set('hoge')
min(sets) # e
max(sets) # o

# sum()
# リスト
lst = [9,11,0]
print(sum(lst)) # 20

# 辞書(keyが対象となる)
dict = {1:9, 2:8, 3:7}
print(sum(dict)) # 6

# タプル
tpl = (6,2,1,9,10)
print(sum(tpl)) # 28

# 集合
sets = {1,2,3,4,5}
print(sum(sets)) # 15

# sorted()
# ソートする
# 文字列
print(sorted('abAB12&あ'))
 # ['&', '1', '2', 'A', 'B', 'a', 'b', 'あ']

# リスト
lst = [9, 11, 0]
print(sorted(lst)) # [0, 9, 11]

# 辞書(keyが対象となる)
dict = {1:9, 2:8, 3:7}
print(sorted(dict)) # [1,2,3]

# タプル
tpl = (6,2,1,9,10)
print(sorted(tpl)) # [1,2,6,9,10]

# 集合
sets = set('hoge')
print(sorted(sets)) # ['e', 'g', 'h', 'o']

# type() 引数のデータ型を返却する
type(123)  # <class 'int'>
type('abc')  # <class 'str'>
type(['a', 'b', 'c'])  # <class 'list'>
type({'a':'a', 'b':'b', 'c':'c'}})  # <class 'dict'>
type(('a', 'b', 'c'))  # <class 'tuple'>
type(set('hoge'))  # <class 'set'>

# floor(), ceil(), round()
import math
# 切り捨て
math.floor(3.14) # 3
# 切り上げ
math.ceil(3.14) # 4
# 四捨五入
math.round(3.14) # 3






















