---
title: Slice
long_title : array.Slice
summary: 現在の配列内の、ある範囲の要素の簡易コピーを作成します。
mt_type: method
mt_title: Slice(number)
mt_summary: 現在の配列内の、指定された場所以降の要素の簡易コピーを作成します。
mt_title: Slice(Range)
mt_summary: 現在の配列内の、Rangeオブジェクトで指定された範囲の要素の簡易コピーを作成します。
mt_title: Slice(number,number)
mt_summary: 現在の配列内の、指定された範囲の要素の簡易コピーを作成します。

---

### 定義
名前空間: Alice<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Core.Array.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Core/Extension/Alice.Core.Array.cs)



#### Slice(number)

現在の配列内の、指定された場所以降の要素の簡易コピーを作成します。

```cs title="AliceScript"
class Alice.Array;
public array Slice(number start);
```

|引数| |
|-|-|
|`start`|要素の簡易コピーの作成を開始する位置。詳しくは**説明**を参照してください。|

|戻り値| |
|-|-|
|`array`|現在の配列の、指定された範囲の要素の簡易をコピーを格納する新しい配列|

???note "対応: Alice4以降"
    |対応||
    |---|---|
    |AliceScript|4|
    |AliceSister|4|
    |Losetta|0.11|

#### Slice(Range)

現在の配列内の、Rangeオブジェクトで指定された範囲の要素の簡易コピーを作成します。

```cs title="AliceScript"
class Alice.Array;
public array Slice(Range range);
```

|引数| |
|-|-|
|`range`|要素の簡易コピーの作成を行う範囲。詳しくは**説明**を参照してください。|

|戻り値| |
|-|-|
|`array`|現在の配列の、指定された範囲の要素の簡易をコピーを格納する新しい配列|

???note "対応: Alice4以降"
    |対応||
    |---|---|
    |AliceScript|4|
    |AliceSister|4|
    |Losetta|0.11|

#### Slice(number,number)

現在の配列内の、指定された範囲の要素の簡易コピーを作成します。

```cs title="AliceScript"
class Alice.Array;
public array Slice(number start, number end);
```

|引数| |
|-|-|
|`start`|要素の簡易コピーの作成を開始する位置。詳しくは**説明**を参照してください。|
|`end`|要素の簡易コピーの作成を終了する位置。詳しくは**説明**を参照してください。|

|戻り値| |
|-|-|
|`array`|現在の配列の、指定された範囲の要素の簡易をコピーを格納する新しい配列|

???note "対応: Alice4以降"
    |対応||
    |---|---|
    |AliceScript|4|
    |AliceSister|4|
    |Losetta|0.11|

### 説明
このメソッドは、現在の配列の一部を簡易コピーした新しい配列を作成します。

`start`および`end`は配列中のインデックスを指定します。
ただし、負の値を指定した場合は配列の末尾のインデックスにその値を加算したインデックスとして扱われます。例えば、配列の長さが`5`で、値を`-1`にしたとき、`5+(-1)`より、インデックスは`4`と解されます。

このメソッドの計算量は$O(n)$です。ここで、$n$は配列の要素数です。

### 例
次の例では、配列の一部をコピーして表示しています。

```cs title="AliceScript"
var ary = [1, 2, 3, 4, 5];

// 2番目(インデックス=1)から4番目(インデックス=3)の手前までを取得する
print(ary.Slice(1, 3)); //出力: [2,3]
```
