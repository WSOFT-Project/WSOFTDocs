---
title: file_get_creationTime
summary: 指定したファイルまたはディレクトリの作成日時を取得します。
date : 2024-05-02

mt_type: function
mt_title: file_get_creationTime(string)
mt_summary: 指定したファイルまたはディレクトリの作成日時を取得します。
mt_title: file_get_creationTime(string,bool)
mt_summary: 日時をUTCで取得するか、現地時間で取得するかを指定して、指定したファイルまたはディレクトリの作成日時を取得します。
---

### 定義
名前空間: Alice.IO<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.IO.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Alice.IO.cs)

#### file_get_creationTime(string)



指定したファイルまたはディレクトリの作成日時を取得します。

```cs title="AliceScript"
namespace Alice.IO;
public DateTime file_get_creationTime(string path);
```

|引数| |
|-|-|
|`path`|作成日時を取得するファイルまたはディレクトリへのパス|

|戻り値| |
|-|-|
|`DateTime`|ファイルまたはディレクトリの現地時間で表した作成日時|

???note "対応: Alice4以降"
    |対応||
    |---|---|
    |AliceScript|4|
    |AliceSister|4|
    |Losetta|0.11|

#### file_get_creationTime(string,bool)



日時をUTCで取得するか、現地時間で取得するかを指定して、指定したファイルまたはディレクトリの作成日時を取得します。

```cs title="AliceScript"
namespace Alice.IO;
public DateTime file_get_creationTime(string path, bool getByUTC);
```

|引数| |
|-|-|
|`path`|作成日時を取得するファイルまたはディレクトリへのパス|
|`getByUTC`|作成日時を協定世界時(UTC)で取得する場合は`true`、現地時間で取得する場合は`false`|

|戻り値| |
|-|-|
|`DateTime`|ファイルまたはディレクトリの`getByUTC`で指定した方式で表した作成日時|

???note "対応: Alice4以降"
    |対応||
    |---|---|
    |AliceScript|4|
    |AliceSister|4|
    |Losetta|0.11|

### 説明

`path`にファイルまたはディレクトリが存在しない場合、この関数は1601年1月1日 午前0時12分(UTC)を返します。`getByUTC`を指定していないか`false`の場合は、現地時間に調整して返します。

ファイルの作成日時は書き換えることができるため、この関数が不正確な値を返す可能性があることにご注意ください。また、ファイルシステムやオペレーティングシステムによっては、その他の理由で不正確な値を返す可能性があります。

`path`には、相対パスと絶対パスのどちらでも指定できます。
相対パスを指定した場合、カレントディレクトリからの相対パスとして解釈します。
パスの大文字と小文字の区別は、環境およびファイルシステムに依存します。たとえば、NTFSでは大文字と小文字は区別されませんが、LFSでは大文字と小文字が区別されます。

### 例
次の例では、`test.txt`の作成日時を表示しています。

```cs title="AliceScript"
using Alice.IO;

print(file_get_creationTime("test.txt"));
```
