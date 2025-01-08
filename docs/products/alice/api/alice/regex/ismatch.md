---
title: IsMatch
long_title : string.IsMatch
summary: 指定された正規表現に一致する箇所が、指定された文字列内に見つかるかどうかを調べます。
mt_type: method
mt_title: IsMatch(this string,string)
---

### 定義
名前空間: Alice.Regex<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Regex.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Alice.Regex.cs)

#### IsMatch(this string,string)

指定された正規表現に一致する箇所が、指定された文字列内に見つかるかどうかを調べます。

```cs title="AliceScript"
namespace Alice.Regex;
public bool IsMatch(this string input, string pattern);
```

|引数| |
|-|-|
|`input`|検索する文字列|
|`pattern`|検索する正規表現のパターン|

|戻り値| |
|-|-|
|`bool`|正規表現と一致する箇所が見つかった場合は`true`、それ以外の場合は`false`|

???note "対応: AliceScript RC2以降"
    |対応||
    |---|---|
    |AliceScript|RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

### 説明
このメソッドを呼び出すことは、[regex_match](./regex_match.md)関数を呼び出すことと同義です。

このメソッドは、文字列が正しい形かどうかを検証する場合に使用します。一般に、正規表現の検索は時間がかかる操作です。そのため、"特定の文字列から始まる"や、"特定の長さ以内"などの簡単な調査には[string.StartsWith](../../string/startswith.md)や`string.Length`を使用してください。

### 例
次の例では、文字列がUrlかを判定します。

```cs title="AliceScript"
using Alice.Regex;

bool IsUrl(string text)
{
    const URL_PATTERN = "https?://[\\w/:%#\\$&\\?\\(\\)~\\.=\\+\\-]+";
    return text.IsMatch(URL_PATTERN);
}

print(IsUrl("hoge@fuga.com"));
//出力: false

print(IsUrl("https://wsoft.ws/"));
//出力: true
```