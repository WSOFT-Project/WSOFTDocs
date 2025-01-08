---
title: delay
summary: 指定した時間の間プログラムを中断します
date : 2024-01-08
mt_type: function
mt_overloads: 2
mt_title: delay()
mt_summary: 無期限にスレッドを中断します。
mt_title: delay(number)
mt_summary: 指定した時間の間スレッドを中断します。
---

### 定義
名前空間: Alice<br/>
アセンブリ: Losetta.Runtime.dll<br/>
ソースコード: [Alice.Core.Utils.cs](https://github.com/WSOFT-Project/Losetta/blob/master/Losetta.Runtime/Core/Alice.Core.Utils.cs)

#### delay()

無期限にスレッドを中断します。

```cs title="AliceScript"
namespace Alice;
public void delay();
```

???note "対応: AliceScript RC1以降"
    |対応||
    |---|---|
    |AliceScript|RC1、RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

#### delay(number)

指定した時間の間スレッドを中断します。

```cs title="AliceScript"
namespace Alice;
public void delay(number timeout);
```

|引数| |
|-|-|
|`timeout`|プログラムが中断される時間(ミリ秒単位)。この値を`-1`にしたとき、スレッドは無期限に中断します。また、この値を`0`にしたとき、スレッドは自らに割り当てられた時間を放棄し、実行する準備ができている同じ優先順位の他のスレッドに渡します。優先順位が同じで他に実行する準備ができているスレッドが存在しない場合は、プログラムは終了されません。|

???note "対応: AliceScript RC2以降"
    |対応||
    |---|---|
    |AliceScript|RC2、GM、2.0、2.1、2.2、2.3、3.0、4|
    |AliceSister|GM、2.0、2.1、2.2、2.3、3.0、4|
    |Losetta|0.8、0.9、0.10、0.11|

### 説明
この関数はプログラム全体を一時的に中断するのではなく、現在のスレッドを中断します。
つまり、`task_run`関数などで別スレッドでもプログラムを実行している場合、現在のスレッドのみ中断します。

`timeout`を`-1`に指定すると、スレッドは無期限に中断します。

また、`timeout`を`0`に指定したとき、他のスレッドに実行を譲らない限りスレッドは中断しません。

この関数は、クロック解像度と呼ばれるレートにしたがって処理を中断します。
この処理はOS依存のため、指定された時間と実際に中断する時間は厳密には一致しない可能性があります。

### 例
以下は、`delay`関数を使用してプログラムを10秒(10000ミリ秒)停止します。

```cs title="AliceScript"
delay(10000);
```

以下は、`delay`関数を使用して1秒ごとにメッセージを表示します。

```cs title="AliceScript"
for(var i = 0; i< 10; i++)
{
    print("Hello!");
    delay(1000);
}
```