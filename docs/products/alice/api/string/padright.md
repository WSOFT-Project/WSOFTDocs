---
title: PadRight
long_title : string.PadRight
summary: 指定された文字数になるまで右側に指定された文字を埋め込むことで、この文字列を左寄せした新しい文字列を取得します
date : 2021-12-09
mt_type: method
mt_title: PadRight(number)
mt_summary: 指定された文字数になるまで左側に空白文字を埋め込むことで、この文字列を右寄せした新しい文字列を取得します。
mt_title: PadRight(number,bool)
mt_summary: 指定された文字数になるまで左側に空白文字を埋め込むことで、この文字列を右寄せした新しい文字列を取得します。
mt_title: PadRight(number,string,bool)
mt_summary: 指定した文字数になるまで左側に指定した文字を埋め込み、必要に応じて切り詰めることで、指定した文字数内でこの文字列を右寄せした新しい文字列を取得します。
---

### 定義
名前空間: Alice<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Core.String.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Core/Extension/Alice.Core.String.cs)

#### PadRight(number)

指定された文字数になるまで左側に空白文字を埋め込むことで、この文字列を右寄せした新しい文字列を取得します。

```cs title="AliceScript"
namespace Alice;
public string PadRight(number totalWidth);
```

|引数| |
|-|-|
|`totalWidth`|結果の文字列の文字数|

|戻り値| |
|-|-|
|`string`|実行した結果の文字列|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

#### PadRight(number,bool)



指定された文字数になるまで左側に空白文字を埋め込むことで、この文字列を右寄せした新しい文字列を取得します。

```cs title="AliceScript"
namespace Alice;
public string PadRight(number totalWidth, bool truncate = false);
```

|引数| |
|-|-|
|`totalWidth`|結果の文字列の文字数|
|`truncate`|対象の文字列の長さが`totalWidth`より長い場合に文字列を切り詰める場合は`true`、切り詰めずすべて表示する場合は`false`。規定値は`false`です。|

|戻り値| |
|-|-|
|`string`|実行した結果の文字列|

???note "対応: Alice4以降"
    |対応||
    |---|---|
    |AliceScript|4|
    |AliceSister|4|
    |Losetta|0.11|

#### PadRight(number,string)

指定された文字数になるまで右側に指定された文字を埋め込むことで、この文字列を左寄せした新しい文字列を取得します。

```cs title="AliceScript"
namespace Alice;
public string PadRight(number totalWidth, string paddingChar, bool truncate = false);
```

|引数| |
|-|-|
|`totalWidth`|結果の文字列の文字数|
|`paddingChar`|埋め込む文字を含む文字列。この文字列の最初の文字が使用されます。|
|`truncate`|対象の文字列の長さが`totalWidth`より長い場合に文字列を切り詰める場合は`true`、切り詰めずすべて表示する場合は`false`。規定値は`false`です。|

|戻り値| |
|-|-|
|`string`|実行した結果の文字列|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

#### PadRight(number,string,bool)



指定した文字数になるまで左側に指定した文字を埋め込み、必要に応じて切り詰めることで、指定した文字数内でこの文字列を右寄せした新しい文字列を取得します。

```cs title="AliceScript"
namespace Alice;
public string PadRight(number totalWidth, string paddingChar, bool truncate = false);
```

|引数| |
|-|-|
|`totalWidth`|結果の文字列の文字数|
|`paddingChar`|埋め込む文字を含む文字列。この文字列の最初の文字が使用されます。|
|`truncate`|対象の文字列の長さが`totalWidth`より長い場合に文字列を切り詰める場合は`true`、切り詰めずすべて表示する場合は`false`。規定値は`false`です。|

|戻り値| |
|-|-|
|`string`|実行した結果の文字列|

???note "対応: Alice4以降"
    |対応||
    |---|---|
    |AliceScript|4|
    |AliceSister|4|
    |Losetta|0.11|

### 説明
この関数は、文字列を特定の文字数の中で左寄せします。

左寄せとは、その文字列が全体のあたかも左端にあるかのように、指定された長さになるまで右に文字を追加することです。追加される文字は`paddingChar`で指定できます。この引数に長さが2以上の文字列が指定された場合は、先頭の1文字目が使用されます。

規定ではこの関数は、文字列の長さが`totalWidth`より大きい場合は、そのままの文字列を返します。文字列を`totalWidth`まで切り詰めたい場合は、`truncate`に`true`を指定してください。ただし、この切り詰めは文字列の左側に適用されます。

次の表は、`totalWidth`を`5`に、`paddingChar`に`*`を指定したとして、文字列がどのように中央揃えされるかを表しています。

対象の文字列|`truncate`の値|結果
----------|--------------|----
ABC|関係なし|\*\*ABC
ABCDEF|`true`|ABCDE
ABCDEF|`false`|ABCDEF

文字列を中央寄せするには[string.PadCenter](./padcenter.md)メソッドを、右寄せするには[string.PadLeft](./padleft.md)メソッドを使用してください。

### 例
以下は、ABCを5文字になるまで左寄せします。

```cs title="AliceScript"
var str = "ABC";
print(str.PadRight(5));
//出力例:"ABC  "
```
