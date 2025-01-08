---
title: CompareTo
long_title: variable.CompareTo
summary: 変数ともう一方の値を比較し、並べ替えたとき変数が前か、後か、または同じかを判断します。
mt_type: method
mt_title: CompareTo(variable)
---

### 定義
名前空間: Alice<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Core.General.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Core/Extension/Alice.Core.General.cs)

#### CompareTo(variable)

変数ともう一方の値を比較し、並べ替えたとき変数が前か、後か、または同じかを判断します。

```cs title="AliceScript"
namespace Alice;
public number CompareTo(variable other);
```

|引数| |
|-|-|
|`other`| この変数と比較する値。|

|戻り値| |
|---|---|
|`number`|この変数がもう一方の値と比べてどの位置にあるかを表す値。|

???note "対応: Alice3.0以降"
    |対応||
    |---|---|
    |AliceScript|3.0、4|
    |AliceSister|3.0、4|
    |Losetta|0.10、0.11|

### 説明
このメソッドは、変数の型ともう一方の型が同一で、かつ比較可能な場合に比較を実行します。

戻り値は並べ替え位置によって次のいずれかの値をとります。

|値|説明|
|---|---|
|`0`より小さい値|並べ替えたときこの変数が、`other`よりも前にきます。|
|`0`|並べ替えたときこの変数が`other`と同じ位置にくるか、または並べ替えできません。|
|`0`より大きい値|並べ替えたときこの変数が、`other`よりも後ろにきます。|

### 例
以下は、`15`と`50`のどちらが前に来るかを判定しています。

```cs title="AliceScript"
number a = 15;
number b = 50;

switch(a.CompareTo(b))
{
    case -1:
    {
        print($"{a}は{b}より前にきます");
        break;
    }
    
    case 0:
    {
        print($"{a}は{b}と同じ位置にきます");
        break;
    }

    case 1:
    {
        print($"{a}は{b}より後ろにきます");
        break;
    }
}
```
