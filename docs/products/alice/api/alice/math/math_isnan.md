---
title: math_isNaN
summary: 指定した数値が非数(NaN)であるかを表す値を取得します。
mt_type: function
mt_title: math_isNaN(number)
---

### 定義
名前空間: Alice.Math<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Math.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Alice.Math.cs)

#### math_isNaN(number)

指定した数値が非数(NaN)であるかを表す値を取得します。

```cs title="AliceScript"
namespace Alice.Math;
public bool math_isNaN(number value);
```

|引数| |
|-|-|
|`value`|判定対象の数値。|

|戻り値| |
|-|-|
|`number`|`value`が非数であれば`true`、それ以外の場合は`false`。|

???note "対応: Alice3.0以降"
    |対応||
    |---|---|
    |AliceScript|3.0、4|
    |AliceSister|3.0、4|
    |Losetta|0.10、0.11|

### 説明

数学演算の結果、演算結果が数学において定義されていない場合に、`NaN`を返します。たとえば、以下の例のように$0/0$は`NaN`です。

```cs title="AliceScript"
using Alice.Math;

number result = 0/0;

print(math_isNan(result));
```