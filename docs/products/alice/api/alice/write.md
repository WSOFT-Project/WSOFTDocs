---
title: write
summary: 文字列または、指定されたオブジェクトの文字列表現を標準出力に書き込みます。
date : 2021-11-09
mt_type: function
mt_overloads: 3
mt_title: write(string)
mt_summary: 指定された文字列を標準出力に書き込みます。
mt_title: write(variable)
mt_summary: 指定されたオブジェクトの文字列表現を標準出力に書き込みます。
mt_title: write(string,params variable)
mt_summary: 与えられた複合書式指定子`format`を使用して後続の変数を成形し、その結果を出力します。
---

### 定義
名前空間: Alice<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Core.Utils.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Core/Alice.Core.Utils.cs)

#### write(variable)

与えられた変数`value`の文字列表現を出力します。

```cs title="AliceScript"
namespace Alice;
public void write(variable value);
```

|引数| |
|-|-|
|`value`| 出力したい変数|

???note "対応: AliceScript RC2以降"
    |対応||
    |---|---|
    |AliceScript|RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

#### write(string)

与えられた文字列`text`を出力します。

```cs title="AliceScript"
namespace Alice;
public void write(string text);
```

|引数| |
|-|-|
|`text`| 出力したい文字列|

???note "対応: AliceScript RC2以降"
    |対応||
    |---|---|
    |AliceScript|RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

#### write(string,params variable)

与えられた複合書式指定子`format`を使用して後続の変数を成形し、その結果を出力します。

```cs title="AliceScript"
namespace Alice;
public void write(string format,params variable args);
```

|引数| |
|-|-|
|`format`| 出力の成形に用いる複合書式指定子|
|`params args`| 出力に使用する変数|

???note "対応: AliceScript RC2以降"
    |対応||
    |---|---|
    |AliceScript|RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

### 例
次の例は、Print関数を使用してHello,Worldを表示するコードです。

```cs title="AliceScript"
write("Hello,World");
```

次の例は、aとbの加算の結果を表示するコードです。

```cs title="AliceScript"
a = 1;
b = 2;
write("a+b="+(a+b));

//出力:a+b=3
```

上記の例は、複合書式指定子を使用して、次のように記述することも可能です。

```cs title="AliceScript"
a = 1;
b = 2;

write("a+b={0}",a+b);
```
