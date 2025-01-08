---
title: web_htmlDecode
summary: HTMLでエンコードされた文字列をでコードされた文字列に変換します。
date : 2021-08-26
mt_type: function
mt_title: web_htmlDecode(string)
---

### 定義
名前空間: Alice.Net<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Net.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Alice.Net.cs)

#### web_htmlDecode(string)

HTMLでエンコードされた文字列をでコードされた文字列に変換します。

```cs title="AliceScript"
namespace Alice.Net;
public string web_htmlDecode(string text);
```

|引数| |
|-|-|
|`text`| デコードする文字列|

|戻り値| |
|-|-|
|`string`| デコードされた文字列|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

### 例
次の例では、[web_htmlEncode](../web_htmlencode)関数を使用して文字列をHTMLエンコードし、その後[web_htmlDecode](../web_htmldecode)関数を使用してHTMLデコードしたものを表示します。

```cs title="AliceScript"
using Alice.Net;

var text = "<div class=\"row\">";

print("HTMLエンコード前のテキスト:{0}",text);

//HTMLエンコードする
text = web_htmlencode(text);

print("HTMLエンコード後のテキスト:{0}",text);

//HTMLデコードする（元の文字列に戻る）
text = web_htmldecode(text);

print("HTMLデコード後のテキスト:{0}",text);
```