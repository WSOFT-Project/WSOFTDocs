---
title: interpreter_namespaces
summary: 現在のインタプリタに登録されている名前空間名を列挙します。
date : 2021-11-19
mt_type: function
mt_title: interpreter_namespaces()
---

### 定義
名前空間: Alice.Interpreter<br/>
アセンブリ: Losetta.dll<br/>
ソースコード: [Alice.Interpreter.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta/NameSpaces/Alice.Interpreter.cs)

#### interpreter_namespaces()

現在のインタプリタに登録されている名前空間名を列挙します。

```cs title="AliceScript"
namespace Alice.Interpreter;
public string[] interpreter_namespaces();
```

|戻り値| |
|-|-|
|`string[]`|現在のインタプリタに登録されている名前空間の名前を含む配列。|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

### 例
次の例では、現在のインタプリタに登録されている名前空間名を取得します。

```cs title="AliceScript"
using Alice.Interpreter;

var ns = interpreter_namespaces();
```