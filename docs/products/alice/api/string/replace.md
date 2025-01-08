---
title: Replace
long_title: string.Replace
summary: 現在の文字列内に出現する特定の文字列をすべて指定した文字列に置き換えた新しい文字列を取得します。
date : 2021-12-09
mt_type: method
mt_title: Replace(string,string)
mt_summary: 現在の文字列内に出現する特定の文字列をすべて指定した文字列に置き換えた新しい文字列を取得します。
mt_title: Replace(string,string,number,number)
mt_summary: 現在の文字列内の指定した範囲に出現する特定の文字列をすべて指定した文字列に置き換えた新しい文字列を取得します。
mt_title: Replace(string,string,bool)
mt_summary: 指定した一致ルールを使用して、現在の文字列内に出現する特定の文字列をすべて指定した文字列に置き換えた新しい文字列を取得します。
mt_title: Replace(string,string,bool,bool)
mt_summary: 指定した一致ルールを使用して、現在の文字列内の指定した範囲に出現する特定の文字列をすべて指定した文字列に置き換えた新しい文字列を取得します。
mt_title: Replace(string,string,string,bool,bool,bool,bool,bool)
mt_summary: カルチャの名前と文字列比較に関するオプションを指定して、現在の文字列内の指定した範囲に出現する特定の文字列をすべて指定した文字列に置き換えた新しい文字列を取得します。
---

### 定義
名前空間: Alice<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Core.String.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Core/Extension/Alice.Core.String.cs)

#### Replace(string,string)

現在の文字列内に出現する特定の文字列をすべて指定した文字列に置き換えた新しい文字列を取得します。

```cs title="AliceScript"
class Alice.String;
public string Replace(string oldValue, string newValue);
```

|引数| |
|-|-|
|`oldValue`|置換する場所の文字列|
|`newValue`|置換後の文字列|

|戻り値| |
|-|-|
|`string`|実行後の文字列|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

#### Replace(string,string,number,number)

現在の文字列内の指定した範囲に出現する特定の文字列をすべて指定した文字列に置き換えた新しい文字列を取得します。

```cs title="AliceScript"
class Alice.String;
public string Replace(string oldValue, string newValue, number startIndex, number length);
```

|引数| |
|-|-|
|`oldValue`|置換する場所の文字列|
|`newValue`|置換後の文字列または`null`|
|`startIndex`|置換を実行する部分の開始位置|
|`count`|置換を実行する部分の長さ|

|戻り値| |
|-|-|
|`string`|実行後の文字列|

???note "対応: Alice2.3以降"
    |対応||
    |---|---|
    |AliceScript|2.3、3.0、4|
    |AliceSister|2.3、3.0、4|
    |Losetta|0.9、0.10、0.11|

#### Replace(string,string,bool)

指定した一致ルールを使用して、現在の文字列内に出現する特定の文字列をすべて指定した文字列に置き換えた新しい文字列を取得します。

```cs title="AliceScript"
class Alice.String;
public string Replace(string oldValue, string newValue, bool ignoreCase);
```

|引数| |
|-|-|
|`oldValue`|置換する場所の文字列|
|`newValue`|置換後の文字列または`null`|
|`ignoreCase`|一致しているかを評価するときに大文字小文字を区別する場合は`true`、それ以外の場合は`false`|

|戻り値| |
|-|-|
|`string`|実行後の文字列|

???note "対応: Alice3.0以降、AliceScriptとLosettaのみ"
    |対応||
    |---|---|
    |AliceScript|3.0、4|
    |AliceSister|該当なし|
    |Losetta|0.10、0.11|

    この関数はAliceSisterでは実装されていません。

    実装されていない環境では`0x034 NOT_IMPLEMENTED`例外がスローされます。

#### Replace(string,string,bool,bool)

指定した一致ルールを使用して、現在の文字列内の指定した範囲に出現する特定の文字列をすべて指定した文字列に置き換えた新しい文字列を取得します。

```cs title="AliceScript"
class Alice.String;
public string Replace(string oldValue, string newValue, bool ignoreCase, bool considerCulture);
```

|引数| |
|-|-|
|`oldValue`|置換する場所の文字列|
|`newValue`|置換後の文字列または`null`|
|`ignoreCase`|一致しているかを評価するときに大文字小文字を区別する場合は`true`、それ以外の場合は`false`|
|`considerCulture`|一致しているかを評価するときに現在のカルチャのルールを使用する場合は`true`、それ以外の場合は`false`|

|戻り値| |
|-|-|
|`string`|実行後の文字列|


???note "対応: Alice3.0以降、AliceScriptとLosettaのみ"
    |対応||
    |---|---|
    |AliceScript|3.0、4|
    |AliceSister|該当なし|
    |Losetta|0.10、0.11|

    この関数はAliceSisterでは実装されていません。

    実装されていない環境では`0x034 NOT_IMPLEMENTED`例外がスローされます。

#### Replace(string,string,string,bool,bool,bool,bool,bool)



カルチャの名前と文字列比較に関するオプションを指定して、現在の文字列内の指定した範囲に出現する特定の文字列をすべて指定した文字列に置き換えた新しい文字列を取得します。

```cs title="AliceScript"
namespace Alice;
public bool Replace(string oldValue,string newValue, string cultureName, bool ignoreCase = false, bool ignoreNonSpace = false, bool ignoreSymbols = false, bool ignoreWidth = false, bool ignoreKanaType = false);
```

|引数| |
|-|-|
|`oldValue`|置換する場所の文字列|
|`newValue`|置換後の文字列または`null`|
|`cultureName`|文字列比較に使用するカルチャの名前。ただし、カルチャに依存しない処理を行う場合は`null`|
|`ignoreCase`|判定時に大文字小文字を区別しない場合は`true`、区別する場合は`false`|
|`ignoreNonSpace`|非スペーシング記号文字(`Nonspacing mark`)の有無を区別しない場合は`true`、区別する場合は`false`|
|`ignoreSymbols`|空白や記号の有無を区別しない場合は`true`、区別する場合は`true`|
|`ignoreWidth`|全角文字と半角文字を区別しない場合は`true`、区別する場合は`false`|
|`ignoreKanaType`|ひらがなとカタカナを区別しない場合は`true`、区別する場合は`false`|

|戻り値| |
|-|-|
|`bool`|現在の文字列が指定した文字列で終わっていれば`true`、それ以外の場合は`false`。|

???note "対応: 未実装、Losettaのみ"
    |対応||
    |---|---|
    |AliceScript|該当なし|
    |AliceSister|該当なし|
    |Losetta|0.11|

    この関数はAliceScriptとAliceSisterでは実装されていません。

    実装されていない環境では`0x034 NOT_IMPLEMENTED`例外がスローされます。

### 例
以下は、`にわにはにわにわとりがいる`という文字列を読みやすく置換します。

```cs title="AliceScript"
string str = "にわにはにわにわとりがいる";

//「にわとり」を「庭」に置換する
str = str.Replace("にわとり","鶏");
//先頭から2文字までの「にわ」を「庭」に置換する
str = str.Replace("にわ","庭",0,2);

print(str);//出力例:庭にはにわ鶏がいる
```

次の例では、全角および半角のカタカナとひらがなの「こんにちは」を「こんばんは」に置換します。

```cs title="AliceScript"
string str = "こんにちは〜コンニチハ〜ｺﾝﾆﾁﾊ〜";

string oldValue = "こんにちは";
string newValue = "こんばんは";

// 全角半角とひらがなカタカナを同一視したいので、
// ignoreWidthとignoreKanaTypeをfalseにする
string replaced = str.Replace(oldValue, newValue, "ja-jp", false, false, false, true, true);

// 置き換えた文字列を表示
print(replaced);

// テスト
string actually = "こんばんは〜こんばんは〜こんばんは〜";
Diagnostics.assert(replaced == actually);
```
