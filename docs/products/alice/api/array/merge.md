---
title: Merge
long_title : array.Merge
summary: 現在の配列の末尾に値を追加した新しい配列を返します
mt_type: method
mt_title: Merge(params variable)
mt_summary: 現在の配列の末尾に値を追加した新しい配列を返します
mt_title: Merge(params array)
mt_summary: 現在の配列の末尾に配列を結合した新しい配列を返します。
---

### 定義
名前空間: Alice<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Core.Array.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Core/Extension/Alice.Core.Array.cs)

#### Merge(params variable)

現在の配列の末尾に値を追加した新しい配列を返します

```cs title="AliceScript"
class Alice.Array;
public array Merge(params variable item);
```

|引数| |
|-|-|
|`item`|追加する変数。この引数は複数個指定できます。|

|戻り値| |
|-|-|
|`array`|結合された配列|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

#### Merge(params array)

現在の配列の末尾に配列を結合した新しい配列を返します。

```cs title="AliceScript"
class Alice.Array;
array Merge(params array ary);
```

|引数| |
|-|-|
|`ary`|末尾で結合する配列。この引数は複数個指定できます。|

|戻り値| |
|-|-|
|`array`|結合された配列|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

### 例
以下は、`1`、`2`、`3`がある配列に`4`、`5`、`6`を追加した新しい配列を作成します。

```cs title="AliceScript"
var a = [1,2,3];
var b = [4,5,6];
var c = a.Add(b);
print(c); // 出力例 : [1,2,3,4,5,6]
```
