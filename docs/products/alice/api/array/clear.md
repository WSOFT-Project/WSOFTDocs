---
title: Clear
long_title : array.Clear
summary: 現在の配列からすべての要素を削除します
mt_type: method
mt_title: Clear()
---

### 定義
名前空間: Alice<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Core.Array.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Core/Extension/Alice.Core.Array.cs)

#### Clear()

現在の配列からすべての要素を削除します

```cs title="AliceScript"
class Alice.Array;
public void Clear();
```

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

### 説明
このメソッドは、現在の配列からすべての要素への参照を削除します。

この関数は配列に対して線形探索を行います。このため、この関数の計算量は$O(n)$です。ここで、$n$は配列の要素数です。
### 例
次の例では、配列内の要素をすべて削除しています。

```cs title="AliceScript"
var ary = [0,1,2];

ary.Clear();

print(ary.Length);// 出力:0
```
