---
title: file_get_length
summary: 指定したファイルのサイズをバイト単位で取得します。
date : 2024-05-02

mt_type: function
mt_title: file_get_length(string)
---

### 定義
名前空間: Alice.IO<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.IO.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Alice.IO.cs)

#### file_get_length(string)



指定したファイルのサイズをバイト単位で取得します。

```cs title="AliceScript"
namespace Alice.IO;
public number file_get_length(string path);
```

|引数| |
|-|-|
|`path`|ファイルサイズを取得するファイルへのパス|

|戻り値| |
|-|-|
|`number`|`path`にあるファイルのファイルサイズ|

???note "対応: Alice4以降"
    |対応||
    |---|---|
    |AliceScript|4|
    |AliceSister|4|
    |Losetta|0.11|

### 説明

この関数が返すサイズの単位はバイト(B)です。ファイルサイズをキロバイト(KB)に換算するには戻り値を1024で、メガバイト(MB)に換算するには戻り値に1048576を除算します。

`path`には、相対パスと絶対パスのどちらでも指定できます。
相対パスを指定した場合、カレントディレクトリからの相対パスとして解釈します。
パスの大文字と小文字の区別は、環境およびファイルシステムに依存します。たとえば、NTFSでは大文字と小文字は区別されませんが、LFSでは大文字と小文字が区別されます。

### 例
次の例では、`test.txt`の長さをキロバイト単位で表示します。

```cs title="AliceScript"
using Alice.IO;

string fileName = "test.txt"
number size = file_get_length(fileName);

print($"{fileName}は、{size / 1024}キロバイトです。");
```
