---
title: path_get_fileName
summary: 指定したパスのファイル名を取得します。
date : 2024-05-01

mt_type: function
mt_title: path_get_fileName(string)
mt_summary: 指定したパスのファイル名を取得します。
mt_title: path_get_fileName(string,bool)
mt_summary: ファイル名から拡張子を取り除いて、指定したパスのファイル名を取得します。
---

### 定義
名前空間: Alice.IO<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.IO.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Alice.IO.cs)

#### path_get_fileName(string)

指定したパスのファイル名を取得します。

```cs title="AliceScript"
namespace Alice.IO;
public string path_get_fileName(string path);
```

|引数| |
|-|-|
|`path`|調べるパス|

|戻り値| |
|-|-|
|`string`|指定したパスのファイル名。ただし、`path`の末尾がディレクトリの区切り文字の場合、空文字列を返します。|

???note "対応: AliceScript RC2以降"
    |対応||
    |---|---|
    |AliceScript|RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|


#### path_get_fileName(string,bool)



ファイル名から拡張子を取り除いて、指定したパスのファイル名を取得します。

```cs title="AliceScript"
namespace Alice.IO;
public string path_get_fileName(string path, bool withoutExtension);
```

|引数| |
|-|-|
|`path`|調べるパス|
|`withoutExtension`|ファイル名から拡張子を取り除く場合は`true`、それ以外の場合は`false`|

|戻り値| |
|-|-|
|`string`|指定したパスのファイル名。ただし、`path`の末尾がディレクトリの区切り文字の場合、空文字列を返します。また、`withoutExtension`が`true`の場合は拡張子を含みません。|

???note "対応: Alice4以降"
    |対応||
    |---|---|
    |AliceScript|4|
    |AliceSister|4|
    |Losetta|0.11|


### 説明
この関数は、指定したパスのファイル名を取得します。
`withoutExtension`を`true`にしない限り、戻り値にはファイル拡張子を含みます。
`path`には必ずしも存在するファイルやディレクトリへのパスを指定する必要はありません。

Unixでは、`\`が有効なファイル名のため、`C:\Directory`のようなWindowsのパスを正しく返すことはできませんが、Windowsでは`/tmp/test.txt`のようなUnixのパスも正しく返せます。この点で、UnixとWindowsでは動作が若干異なります。

### 例
次の例では、`test.txt`のファイル名を表示しています。

```cs title="AliceScript"
using Alice.IO;

print(path_get_fileName("dir\\test.txt"));
//出力: test.txt
```