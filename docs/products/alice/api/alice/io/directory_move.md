---
title: directory_move
summary: 指定したファイルまたはディレクトリを別の場所に移動します。
mt_type: function
mt_title: directory_move(string,string)
---

### 定義
名前空間: Alice.IO<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.IO.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Alice.IO.cs)

#### directory_move(string,string)

指定したファイルまたはディレクトリを別の場所に移動します。

```cs title="AliceScript"
namespace Alice.IO;
public void directory_move(string source, string destination);
```

|引数| |
|-|-|
|`source`|移動元のファイルやディレクトリへのパス|
|`destination`|移動先のファイルやディレクトリへのパス|

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

### 説明
この関数を使用して、ファイルまたはディレクトリの名前を変更できます。この関数では、`destination`で指定された新しいディレクトリを作成し、`source`にある内容を再帰的に新しく作成されたディレクトリに移動します。その後、`source`を削除します。

この関数では、ディレクトリを別のボリュームに移動することはできません。

`path`には、相対パスと絶対パスのどちらでも指定できます。
相対パスを指定した場合、カレントディレクトリからの相対パスとして解釈します。
パスの大文字と小文字の区別は、環境およびファイルシステムに依存します。たとえば、NTFSでは大文字と小文字は区別されませんが、LFSでは大文字と小文字が区別されます。

`path`には、ファイル名を指定してはいけません。また、末尾の空白文字は自動的に削除されます。
### 例
次の例では、`test`というディレクトリが存在するか確認します。

```cs title="AliceScript"
using Alice.IO;

directory_exists("test");
```