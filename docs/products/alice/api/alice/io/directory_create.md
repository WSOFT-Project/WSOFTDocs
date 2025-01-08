---
title: directory_create
summary: ディレクトリを作成します。
date : 2021-07-28
mt_type: function
mt_title: directory_create(string)
---

### 定義
名前空間: Alice.IO<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.IO.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Alice.IO.cs)

#### directory_create(string)

指定したパスにディレクトリを作成します。
すでにディレクトリが存在する場合は何もしません。

```cs title="AliceScript"
namespace Alice.IO;
public void directory_create(string path);
```

|引数| |
|-|-|
|`path`|作成するディレクトリのパス|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

### 説明
`path`には、相対パスと絶対パスのどちらでも指定できます。
相対パスを指定した場合、カレントディレクトリからの相対パスとして解釈します。
パスの大文字と小文字の区別は、環境およびファイルシステムに依存します。たとえば、NTFSでは大文字と小文字は区別されませんが、LFSでは大文字と小文字が区別されます。

この関数は、`path`で指定されたディレクトリの親ディレクトリがない場合、再帰的に作成します。つまり、`a/b`を指定した場合、存在しない場合はディレクトリ`a`を作成しその中にディレクトリ`b`を作成します。

`path`には、ファイル名を指定してはいけません。また、末尾の空白文字は自動的に削除されます。

`:`(コロン)のみのディレクトリを作成することはできません。
### 例
次の例では、`test`というディレクトリを作成します。

```cs title="AliceScript"
using Alice.IO;

directory_create("test");
```