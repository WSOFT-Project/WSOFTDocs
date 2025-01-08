---
title: math_min
summary: 指定された複数の数値のうち、もっとも小さい数値を返します。
mt_type: function
mt_title: math_min(number,params number)
---

### 定義
名前空間: Alice.Math<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Math.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Alice.Math.cs)

#### math_min(number,params number)

指定された複数の数値のうち、もっとも小さい数値を返します。

```cs title="AliceScript"
namespace Alice.Math;
public number math_min(number value,params number values);
```

|引数| |
|-|-|
|`value`|比較する整数の最初の数値。|
|`values`|比較する整数の残りの値。|

|戻り値| |
|-|-|
|`number`|引数の中でもっとも小さい数値。|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|
