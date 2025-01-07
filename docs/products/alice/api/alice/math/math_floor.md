---
title: math_floor
summary: 指定された数の小数点以下を切り捨てた整数を取得します。
mt_type: function
mt_title: math_floor(number)
mt_summary: 指定された数の指定された小数点以下を切り捨てた整数を取得します。
mt_title: math_floor(number,number)
mt_summary: 指定された数の指定された小数点以下を切り捨てた整数を取得します。
---

### 定義
名前空間: Alice.Math<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Math.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Alice.Math.cs)

#### math_floor(number)

指定された数の小数点以下を切り捨てた整数を取得します。

```cs title="AliceScript"
namespace Alice.Math;
public number math_floor(number value);
```

|引数| |
|-|-|
|`value`|切り捨てたい対象の数値|

|戻り値| |
|-|-|
|`number`|`value`の整数部|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

#### math_floor(number,number)



指定された数の指定された小数点以下を切り捨てた整数を取得します。

```cs title="AliceScript"
namespace Alice.Math;
public number math_floor(number value, number digits);
```

|引数| |
|-|-|
|`value`|切り捨てる値|
|`digits`|戻り値の小数部の桁数。`0`以上の整数である必要があります。|

|戻り値| |
|-|-|
|`number`|`value`の指定された小数点以下を切り捨てた数。|

???note "対応: Alice4以降"
    |対応||
    |---|---|
    |AliceScript|4|
    |AliceSister|4|
    |Losetta|0.11|

### 説明
`value`の値が[math_NaN](./math_nan.md)の場合、この関数は[math_NaN](./math_nan.md)を返します。また`value`の値が[math_Infinity](./math_infinity.md)の場合、この関数も[math_Infinity](./math_infinity.md)を返し、`value`の値が[math_NegativeInfinity](./math_negativeinfinity.md)の場合、この関数も[math_NegativeInfinity](./math_negativeinfinity.md)を返します。

小数部を切り上げたいときは[math_ceiling](./math_ceiling.md)を、四捨五入したいときは[math_round](./math_round.md)を使用してください。

この関数は、IEEE 754 セクション4に従った切り捨てを行います。
これは、一般に「負の無限大向きの丸め」と呼ばれています。

この関数の丸め方は、`value`の符号によって異なります。

- `value`が正の場合、小数部がすべて切り捨てられます。
- `value`が負の場合、小数部が存在する場合は負の無限大方向に丸めます。

この関数の動作は[math_truncate](./math_truncate.md)や[math_ceiling](./math_ceiling.md)とは異なることにご注意ください。

### 例
次の例では、いくつかの数の小数部を切り捨てています。

```cs title="AliceScript"
using Alice.Math;

print(math_floor(12.3));  //出力 : 12
print(math_floor(-12.3)); //出力 : -13
```