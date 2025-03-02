---
title: 数値型の計算誤差
summary: AliceScriptの数値型は、倍精度浮動小数点数数値型と定められており、この規格はIEEE754として標準化されています。 しかしこの数値型で小数の計算をしているとき、その計算結果が期待通りでないことがあります。この記事では、その理由について説明します。
date : 2022-04-12
---

### 計算誤差の例
次の式は`true`と評価されるでしょうか？それとも、`false`と評価されるでしょうか。

```cs title="AliceScript"
0.1 + 0.2 == 0.3
```
数学では、上記の式は正しく`true`と評価されますし、ほとんどの開発者も、それが正しいことを期待します。 では、AliceScriptでこの式を評価してみます。

```cs title="AliceScript"
print(0.1 + 0.2 == 0.3);
```
このコードを実行すると、`false`が出力されます。

### 理由
これらの計算誤差はバグではありません。AliceScriptの数値型のような浮動小数点数数値型は、値を2進数で格納していますが、ほとんどの10進数の小数は2進数で表すことができず、その近似値として表現されます。近似値の誤差が例に示したような計算誤差として現れます。

知的好奇心旺盛なあなたのために、もう少し説明します。たとえば10進数の`0.1`を2進数に変換すると`0.0001100110011…`となり、0011が永遠と循環します。そのため`0.1`を倍精度浮動小数点数数値型に格納するには、適当な桁で丸める必要があります。このとき、もっとも近い偶数に値を丸めます。その結果として`0.1`は数値型では2進数で`0.0001100110011001100110011001100110011001100110011001101`となります。これを10進数に戻すと`0.1000000000000000055511151231257827021181583404541015625`となり、`0.1`ではなくなります。

ただし整数は、有効桁数15桁の範囲内であれば、正確に格納できます。また小数であっても、$k/2^n$ (k,nは整数)で表すこともできる小数は2進数で表現できるため、正確に格納できます。

なおこのような誤差は、AliceScript固有のものではありません。IEEE 754の2進浮動小数点形式を採用しているシステムでは、同じことが起こりえます。

### 回避策
この問題を回避するためには、以下のような方法があります。

#### 許容範囲を決めて値を比較する
ふたつの浮動小数点数数値型数を比較するとき、たとえばそれらが等しいかを調べるときに==を使うのは危険です。両者がまったく等しい場合のみ等しいと判断するのではなく、「両者の差の絶対値がある程度であれば等しいと認める」など許容範囲を決めて比較する方が安全です。次の例は、許容範囲を定めt、`0.000001`未満の差の場合に等しいと判断します。

```cs title="AliceScript"
using Alice.Math;
//AliceGMならこう import "Alice.Math";

///二つの小数が等しいと認められるかどうかを評価します
///パラメータ a:一方の値
///         b:もう一方の値
/// tolerance:許容できる誤差の最大の値(この数値は常に正)     
bool NumEqual(number a, number b, number tolerance)
{
   return math_abs(a - b) < tolerance;
}

var numA = 0.1 + 0.2;
var numB = 0.3;
///許容範囲
var tolerance = 0.000001;
if(NumEqual(numA,numB,tolerance))
 {
    print("numAとnumBは等しいです。");
 }
```

Alice4.0以降では、[math_isRelativelyClose](../api/alice/math/math_isrelativelyclose.md)関数を使用します。
次に、この関数を使用して許容範囲を決めて値を比較する方法を示します。

```cs title="AliceScript"
using Alice.Math;

var numA = 0.1 + 0.2;
var numB = 0.3;

if(math_isRelativelyClose(numA, numB))
{
   print("numAとnumBは等しいです。");
}
```

#### 一度整数にした後変換する
他には、たとえば一度整数にしてから計算する方法も考えられます。次の例では、ふたつの数を整数にすることができる数`dis ** 10`を求めて二数を整数にした後、計算を行うことで誤差を防ぎます。ただしこの場合でも、有効数字15桁以上の数は正確に扱うことができません。

```cs title="AliceScript"
using Alice.Math;
//AliceGMならこう import "Alice.Math";

///与えられた数の小数点以下の桁数を取得します
function GetDisitsUnder1(number num)
 {
    var priceString = price.ToString().TrimEnd('0');
    int index = priceString.IndexOf('.');
    if (index == -1){return 0;}
    return priceString.Substring(index + 1).Length;
 }

///二つの小数が等しいかどうかを判断します
function NumEqual(number numA,numbner numB)
 {
    //numA,numBの小数点以下の桁数(すなわち、10の何乗倍すれば整数になるか)
    var nAd = GetDisitsUnder1(numA);
    var nBd = GetDisitsUnder1(numB);
    //二つの小数の小数点以下桁数のうち多い方
    var dis = math_max(nAd,nBd);
    
    //numA,numBを整数化したもの
    var rA = numA * (dis ** 10);
    var rB = numB * (dis ** 10);
    
    return (rA == rB);
 }

///二つの小数の和を求めます
function Sum(number numA,number numB)
 {
    //numA,numBの小数点以下の桁数(すなわち、10の何乗倍すれば整数になるか)
    var nAd = GetDisitsUnder1(numA);
    var nBd = GetDisitsUnder1(numB);
    //二つの小数の小数点以下桁数のうち多い方
    var dis = math_max(nAd,nBd);
    
    //numA,numBを整数化したもの
    var rA = numA * (dis ** 10);
    var rB = numB * (dis ** 10);
    //整数化されたものの計算結果
    var result = rA + rB;

    return (result / (dis ** 10));
 }

print(NumEqual(0.1+0.2,0.3));//出力例:true
print(Sum(0.1,0.2));//出力例:0.3
```
