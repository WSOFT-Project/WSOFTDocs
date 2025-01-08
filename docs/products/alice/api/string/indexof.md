---
title: IndexOf
long_title : string.IndexOf
summary: 指定された文字列が現在の文字列内で最初に見つかった位置のインデックスを返します
date : 2021-12-09
mt_type: method
mt_title: IndexOf(string,number)
mt_summary: 指定された文字列が現在の文字列内で最初に見つかった位置のインデックスを返します。検索は、指定されたインデックスから開始され、見つからなかった場合は-1を返します。
---

### 定義
名前空間: Alice<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Core.String.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Core/Extension/Alice.Core.String.cs)

#### IndexOf(string,number)

指定された文字列が現在の文字列内で最初に見つかった位置のインデックスを返します。検索は、指定されたインデックスから開始され、見つからなかった場合は`-1`を返します。

```cs title="AliceScript"
namespace Alice;
public number IndexOf(string item, number startIndex = 0);
```

|引数| |
|-|-|
|`item`|検索する対象の値|
|`startIndex`|検索を開始するインデックス。既定値は`0`です。|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

!!!note "情報"
    インデックスとは、配列の最初の項目から順に`0,1,2...`と番号を割り当てたものです。たとえば、3番目の要素のインデックスは`2`です。

### 説明
インデックスとは、配列の最初の項目から順に`0,1,2...`と番号を割り当てたものです。たとえば、3番目の要素のインデックスは`2`です。`startIndex`には、0から文字列の長さまでの範囲の値を指定できます。

このメソッドは、現在のカルチャを使用して検索を行います。
このため、`item`に無視できる文字が含まれている場合、その文字を無視した検索を行います。

### 例
以下は、Hello,Worldという文字列から`,`のインデックスを取得します。

```cs title="AliceScript"
var a = "Hello,World";
print(a.IndexOf(",")); // 出力例 : 5
```
