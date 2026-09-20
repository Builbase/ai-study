---
marp: true
theme: deck
paginate: false
size: 16:9
html: true
title: Googleドキュメント・カレンダー・Meetを使いこなす
description: Builbase社内AI勉強会 第1回（90分）
author: seiji
---

<!-- _class: title -->

# 社内AI勉強会

<p>
第1回 Googleドキュメント・カレンダー・Meetを使いこなす<br>
2026-09-27（日）岡山大インキュベータ／90分
</p>

---

<!-- header: 'はじめに' -->
# 今日持ち帰る3つ

<div class="fig">
<div class="row c3">
<div class="card">
<div class="t">権限を選んで共有</div>
<div class="d">閲覧者・コメント可・編集者の使い分け</div>
</div>
<div class="card on">
<div class="t">Meet付き予定を送る</div>
<div class="d">空き時間を比べて、メールアドレスで招待</div>
</div>
<div class="card">
<div class="t">変えるのは主催者</div>
<div class="d">定例の曜日や周期は、作った人しか直せない</div>
</div>
</div>
</div>

---

# 今日の流れ

<div class="fig">
<div class="timeline">
<div class="seg g" style="flex:10"><b>10分</b>はじめに</div>
<div class="seg" style="flex:25"><b>25分</b>ドキュメント</div>
<div class="seg" style="flex:25"><b>25分</b>カレンダー</div>
<div class="seg" style="flex:15"><b>15分</b>Meet</div>
<div class="seg g" style="flex:10"><b>10分</b>予備</div>
<div class="seg g" style="flex:5"><b>5分</b>次回</div>
</div>

<div class="row c3">
<div class="card flat">
<div class="t">各ツール2テーマに絞る</div>
<div class="d">明日から使える操作を優先。<br>時間が余れば3つ目へ</div>
</div>
<div class="card flat">
<div class="t">自分の端末で操作する</div>
<div class="d">5人×2グループ。<br>隣と確認しながら進める</div>
</div>
<div class="card flat">
<div class="t">質問はいつでも</div>
<div class="d">気になったところは、その場で。<br>各ツールの最後に、使っている人の話も聞く</div>
</div>
</div>
</div>

---

<!-- _class: chapter -->
<!-- header: '1. Googleドキュメント' -->

<div class="n">CHAPTER 1</div>

# Googleドキュメント

共有権限、コメントと提案、@メニュー、Gemini

---

# 共有は「誰に」「何をしてもらうか」で権限を選ぶ

<div class="split">
<div class="pts">
<div class="pt"><b>閲覧者</b><span>読むだけ。<br>配布資料や決定済みの文書</span></div>
<div class="pt"><b>閲覧者（コメント可）</b><span>確認や意見出しを頼むとき</span></div>
<div class="pt ok"><b>編集者</b><span>本文を一緒に書く人だけ</span></div>
</div>
<div class="shotbox"><img class="shot" src="images/docs-01-share-dialog.png" alt="共有ダイアログで権限を選ぶ"></div>
</div>

---

# 「リンクを知っている全員」は安易に使わない

<div class="split">
<div class="pts">
<div class="pt ok"><b>基本は「制限付き」</b><span>業務上必要な相手だけを追加する</span></div>
<div class="pt warn"><b>社外への共有</b><span>事前に決めた確認手順に従う</span></div>
<div class="pt"><b>共有前にひと目</b><span>相手にアクセス権があるか、送る前に確認する</span></div>
</div>
<div class="shotbox"><img class="shot" src="images/docs-02-general-access.png" alt="一般的なアクセスの設定"></div>
</div>

---

# 確認はコメント、修正案は提案モード

<div class="vs2">
<div class="col">
<div class="lab">コメント</div>
<img class="shot" src="images/docs-05-comment.png" alt="コメントを付けた状態">
<div class="d">「ここは合っていますか」など確認したいこと。<br>本文は変わらない</div>
</div>
<div class="col">
<div class="lab">提案モード</div>
<img class="shot" src="images/docs-03-mode-menu.png" alt="編集・提案・閲覧の切り替え">
<div class="d">右上の鉛筆から切り替える。<br>修正案は元の文を消さずに残る</div>
</div>
</div>

---

# 提案は「承認」で本文になる

<div class="full">
<img class="shot" src="images/docs-04-suggestion.png" alt="提案の吹き出しと承認ボタン">
<div class="cap">提案された箇所は色つきで残る。<br>✓で反映、×で取り下げ。<br>誰が何を直したかが追える</div>
</div>

---

# @を打つと、人・日付・ファイルを埋め込める

<div class="vs2">
<div class="col">
<div class="lab">@を打つ</div>
<img class="shot" src="images/docs-06-at-menu.png" alt="@メニュー">
<div class="d">ユーザー、日付、ファイルなどが一覧で出る</div>
</div>
<div class="col">
<div class="lab">入れた結果</div>
<img class="shot" src="images/docs-07-smart-chip.png" alt="日付と担当者のスマートチップ">
<div class="d">日付と担当者がチップになる。<br>載せると詳細が出て、表記もそろう</div>
</div>
</div>

---

# 要約と下書きはGeminiに頼める

<div class="split">
<div class="pts">
<div class="pt"><b>長い文書の要約</b><span>会議前に「要点を3つに」で把握する</span></div>
<div class="pt"><b>下書きと書き換え</b><span>箇条書きから案内文を作る、丁寧語に直す</span></div>
<div class="pt warn"><b>そのまま確定にしない</b><span>生成された文は、人が読んでから使う</span></div>
</div>
<div class="shotbox"><img class="shot" src="images/docs-08-gemini.png" alt="Geminiのサイドパネル"></div>
</div>

---

# 演習1・ドキュメント（10分）

<div class="fig">
<div class="steps">
<div class="s"><i></i><div>研修用のサンプル文書を開く<small>講師が共有する。<br>まず自分の権限が「編集者」か確かめる</small></div></div>
<div class="s"><i></i><div>気になる1文にコメントを付ける<small>隣の人を@で呼ぶ</small></div></div>
<div class="s"><i></i><div>提案モードに切り替えて、1語だけ直す<small>元の文が消えないことを見る</small></div></div>
<div class="s"><i></i><div>隣の人の提案を承認する<small>✓を押した側が「反映した人」になる</small></div></div>
<div class="s"><i></i><div>@で今日の日付チップを入れる</div></div>
</div>
<p class="note" style="margin-top: 14px;">演習のあとに2分: 普段から使っている人に、実務での使い方をひとこと聞く</p>
</div>

---

<!-- _class: chapter -->
<!-- header: '2. Googleカレンダー' -->

<div class="n">CHAPTER 2</div>

# Googleカレンダー

予定を作って招待する、変更する、主催者の役割

---

# 「時間を探す」で、参加者の空きを一度に見る

<div class="split">
<div class="pts">
<div class="pt"><b>ゲストを入れてから開く</b><span>予定の作成画面の「時間を探す」タブ</span></div>
<div class="pt"><b>週表示で並べる</b><span>全員の予定が横に並ぶ。<br>空いている帯を選ぶ</span></div>
<div class="pt ok"><b>往復のメールが減る</b><span>候補日を聞いて回らなくてよい</span></div>
</div>
<div class="shotbox"><img class="shot" src="images/cal-03-find-time.png" alt="時間を探す"></div>
</div>

---

# Meet付きの予定を作り、メールアドレスで招待する

<div class="split">
<div class="pts">
<div class="pt"><b>タイトルと時間</b><span>「担当者MTG」のように、後で探せる名前にする</span></div>
<div class="pt"><b>ゲストを追加</b><span>メールアドレスを入れてEnter。<br>社外や別ドメインも同じ</span></div>
<div class="pt"><b>Google Meetを追加</b><span>ボタン1つで会議リンクが付く。<br>保存時に招待メールが届く</span></div>
</div>
<div class="shotbox"><img class="shot" src="images/cal-01-editor.png" alt="予定の作成画面"></div>
</div>

---

# 保存すると招待メールが届く。社外の人は確認が出る

<div class="vs2">
<div class="col">
<div class="lab">保存したとき</div>
<img class="shot" src="images/cal-06-invite-mail.png" alt="招待メールを送信するかの確認">
<div class="d">「送信」でゲスト全員に招待メールが届く。<br>返答もメールで戻る</div>
</div>
<div class="col">
<div class="lab g">社外のアドレスを入れたとき</div>
<img class="shot" src="images/cal-14-external-guest.png" alt="組織外からのゲストの確認">
<div class="d">Builbase以外のアドレスは、この確認が出る。<br>相手を見てから招待する</div>
</div>
</div>

---

# 定例は「繰り返し」で作る。周期はカスタムで変えられる

<div class="vs2">
<div class="col">
<div class="lab">繰り返しの選択</div>
<img class="shot" src="images/cal-04-recurrence-menu.png" alt="繰り返しのメニュー">
<div class="d">毎週・毎月・平日など。<br>決まった曜日の会議はここ</div>
</div>
<div class="col">
<div class="lab">カスタム</div>
<img class="shot" src="images/cal-05-recurrence-custom.png" alt="カスタムの繰り返し">
<div class="d">「2週間ごと」「終了日あり」はカスタムで指定する</div>
</div>
</div>

---

# 招待された側は、出欠と「新しい時間を提案」ができる

<div class="split">
<div class="pts">
<div class="pt"><b>はい・いいえ・未定</b><span>主催者に返答が届く。<br>放置しないのが最初のルール</span></div>
<div class="pt"><b>新しい時間を提案</b><span>出られないときは、別の日時を予定から送る</span></div>
<div class="pt ok"><b>主催者が承認すると更新</b><span>全員の予定がその日時に書き換わる</span></div>
</div>
<div class="shotbox"><img class="shot" src="images/cal-07-guest-popup.png" alt="ゲスト側の予定の詳細"></div>
</div>

---

# 提案画面では、相手の予定を見ながら候補を選べる

<div class="full">
<img class="shot" src="images/cal-08-propose-time.png" alt="新しい時間を提案する画面">
<div class="cap">左で日時とひとことを入れ、右で参加者の予定を確かめる。<br>「提案を送信」で主催者へ届く</div>
</div>

---

# 曜日・周期・時刻を変えられるのは、主催者だけ

<div class="vs2">
<div class="col">
<div class="lab">主催者（作った人）</div>
<img class="shot" src="images/cal-09-organizer-edit-top.png" alt="主催者の編集画面">
<div class="d">日時も繰り返しもドロップダウンで変えられる</div>
</div>
<div class="col">
<div class="lab g">ゲスト（招待された人）</div>
<img class="shot" src="images/cal-10-guest-edit-top.png" alt="ゲストの編集画面">
<div class="d">日時と「2週間ごと 月曜日」が文字のまま。<br>変えられるのは自分の通知や色だけ</div>
</div>
</div>

---

# 定例を「毎週」から「2週間に1回」にしたいとき

<div class="split wide">
<div class="pts">
<div class="pt warn"><b>ゲストからは変えられない</b><span>周期の変更は主催者だけの操作</span></div>
<div class="pt"><b>主催者に頼む</b><span>「新しい時間を提案」かSlackで依頼する</span></div>
<div class="pt ok"><b>主催者が保存すると全員に通知</b><span>変更内容がメールで届く</span></div>
</div>
<div class="shotbox"><img class="shot" src="images/cal-12-update-mail.png" alt="変更内容をゲストにメールで送信する確認"></div>
</div>

---

# 主催者が変わるときは「主催者を変更」で引き継ぐ

<div class="vs2">
<div class="col">
<div class="lab">主催者を変更</div>
<img class="shot" src="images/cal-11-organizer-menu.png" alt="主催者を変更のメニュー">
<div class="d">異動や退職の前に。<br>放置すると誰も直せない定例が残る</div>
</div>
<div class="col">
<div class="lab">ゲストの権限</div>
<img class="shot" src="images/cal-13-guest-permission.png" alt="ゲストの権限の設定">
<div class="d">「予定を変更する」を付ければゲストも編集できる。<br>既定はオフ</div>
</div>
</div>

---

# 演習2・カレンダー（12分）

<div class="fig">
<div class="steps">
<div class="s"><i></i><div>グループで主催者役を1人決める</div></div>
<div class="s"><i></i><div>主催者が「時間を探す」で全員の空きを見て、Meet付きの予定を作る<small>グループ全員をメールアドレスで招待。<br>繰り返しは「毎週」</small></div></div>
<div class="s"><i></i><div>招待された人は出欠を返す。1人が「新しい時間を提案」する</div></div>
<div class="s"><i></i><div>主催者が提案を承認する。全員の予定が変わったか見る</div></div>
<div class="s"><i></i><div>ゲストが繰り返しを「2週間ごと」に変えようとしてみる<small>変えられないことを確かめてから、主催者が変える</small></div></div>
</div>
<p class="note" style="margin-top: 14px;">演習のあとに2分: 普段から使っている人に、実務での使い方をひとこと聞く</p>
</div>

---

<!-- _class: chapter -->
<!-- header: '3. Google Meet' -->

<div class="n">CHAPTER 3</div>

# Google Meet

会議の機能と保存先、画面共有の使い分け

---

# 録画・文字起こし・字幕は、右下の「会議ツール」から

<div class="split">
<div class="pts">
<div class="pt"><b>録画</b><span>会議ツール→録画。<br>保存先はドライブの「Meet Recordings」。<br>押せないときは管理者設定で有効にする</span></div>
<div class="pt"><b>字幕</b><span>下のバーの「CC」。<br>自分の画面だけに出る</span></div>
<div class="pt warn"><b>Geminiの会議メモ</b><span>カレンダーの予定で「Geminiを使用して会議メモを作成する」をオン。<br>要約は人が確認する</span></div>
</div>
<div class="shotbox"><img class="shot" src="images/meet-03-tools.png" alt="Meetの会議ツール"></div>
</div>

---

# 画面共有は「タブ」「ウィンドウ」「画面全体」を使い分ける

<div class="share3">
<div class="sc on">
<div class="t">Chromeタブ</div>
<div class="mac"><div class="bar"></div><div class="win"><div class="tabs"><i class="cur"></i><i></i><i></i></div><div class="page"><i class="h"></i><i></i><i class="s"></i><i></i></div></div><div class="app2"><i></i><i></i><i></i></div><div class="noti"></div><div class="hl tab"></div></div>
<div class="use"><b>資料を1つ見せる</b>ときに。<br>そのタブだけが映る。音声も送れる</div>
</div>
<div class="sc">
<div class="t">ウィンドウ</div>
<div class="mac"><div class="bar"></div><div class="win"><div class="tabs"><i class="cur"></i><i></i><i></i></div><div class="page"><i class="h"></i><i></i><i class="s"></i><i></i></div></div><div class="app2"><i></i><i></i><i></i></div><div class="noti"></div><div class="hl w"></div></div>
<div class="use"><b>アプリを1つ見せる</b>ときに。<br>切り替えたタブも映る。通知は出ない</div>
</div>
<div class="sc">
<div class="t">画面全体</div>
<div class="mac"><div class="bar"></div><div class="win"><div class="tabs"><i class="cur"></i><i></i><i></i></div><div class="page"><i class="h"></i><i></i><i class="s"></i><i></i></div></div><div class="app2"><i></i><i></i><i></i></div><div class="noti"></div><div class="hl all"></div></div>
<div class="use"><b>操作を実演する</b>ときに。<br>別のアプリも通知も、全部映る</div>
</div>
</div>
<p class="note" style="text-align:center; margin-top: 14px;">青い枠が相手に見える範囲。下のバーの「画面を共有」→3つから選ぶ→共有したいものをクリック</p>

---

# 演習3・Meet（8分）

<div class="fig">
<div class="steps">
<div class="s"><i></i><div>演習2で作った予定のMeetリンクから、グループ全員が入る<small>マイクとスピーカーはオフ。<br>同じ部屋なのでハウリングを防ぐ</small></div></div>
<div class="s"><i></i><div>1人ずつ「タブ」で資料を共有する<small>共有できたら次の人へ交代</small></div></div>
<div class="s"><i></i><div>1人が「画面全体」で共有し、違いを見る</div></div>
<div class="s"><i></i><div>講師が録画・字幕・Geminiの会議メモの場所を見せる</div></div>
</div>
<p class="note" style="margin-top: 14px;">演習のあとに2分: 普段から使っている人に、実務での使い方をひとこと聞く</p>
</div>

---

<!-- _class: chapter -->
<!-- header: 'まとめ' -->

<div class="n">WRAP UP</div>

# 社内で守ること

今日から使う、2つのルール

---

# 今日決めた運用ルール

<div class="rules">
<div class="r">
<div class="t">ドキュメントの共有</div>
<ul>
<li>基本は「制限付き」。必要な相手だけ追加する</li>
<li>読むだけなら閲覧者、確認はコメント可、一緒に書くなら編集者</li>
<li>確認はコメント、修正案は提案モード。承認する担当者を決める</li>
<li>社外への共有は、決めた確認手順に従う</li>
</ul>
</div>
<div class="r">
<div class="t">カレンダーの主催者</div>
<ul>
<li>招待が届いたら、はい・いいえ・未定を返す</li>
<li>定例は、主催者が誰か分かるようにしておく</li>
<li>周期・時刻・Meetリンクの変更は主催者が行う</li>
<li>ゲストは「新しい時間を提案」かSlackで主催者に頼む</li>
<li>主催者が異動・退職する前に「主催者を変更」で引き継ぐ</li>
</ul>
</div>
</div>

---

# 次回までにやること

<div class="fig">
<div class="row c3">
<div class="card">
<div class="t">1回、提案モードで直す</div>
<div class="d">誰かの文書に、コメントではなく提案で修正案を送る</div>
</div>
<div class="card on">
<div class="t">1回、Meet付きで招待する</div>
<div class="d">「時間を探す」を使って、メールアドレスで招待する</div>
</div>
<div class="card">
<div class="t">自分が主催の定例を確認</div>
<div class="d">主催者が誰か、ゲストに分かる状態になっているか見る</div>
</div>
</div>
<p class="note" style="text-align:center; margin-top: 24px;">次回は10月。使ってみて困ったことを、そのまま持ってきてください</p>
</div>

---

<!-- _class: chapter -->
<!-- header: '予備' -->

<div class="n">EXTRA</div>

# 時間があれば、3つ目

各ツールにもう1つ。当日の進み具合で使う

---

<!-- header: '予備 1. Googleドキュメント' -->
# 消しても戻せる。変更履歴で「誰がいつ何を」が分かる

<div class="split">
<div class="pts">
<div class="pt"><b>ファイル→変更履歴</b><span>右上の時計マークでも開く</span></div>
<div class="pt"><b>版を選ぶと差分が色で出る</b><span>人ごとに色が違う。<br>誰がどこを変えたかが分かる</span></div>
<div class="pt ok"><b>「この版を復元」で戻せる</b><span>戻しても履歴は消えない。<br>安心して共同編集できる</span></div>
</div>
<div class="shotbox"><img class="shot" src="images/docs-09-version-history.png" alt="変更履歴の画面"></div>
</div>

---

<!-- header: '予備 2. Googleカレンダー' -->
# 社外の人との日程調整は「予約ページ」で相手に選んでもらう

<div class="split">
<div class="pts">
<div class="pt"><b>作成→予約スケジュール</b><span>受け付ける曜日・時間帯・1枠の長さを決める</span></div>
<div class="pt"><b>リンクを送る</b><span>相手は空いている枠を選ぶだけ。<br>Meet付きの予定が自動で入る</span></div>
<div class="pt ok"><b>「時間を探す」との使い分け</b><span>社内は時間を探す、社外・お客様は予約ページ</span></div>
</div>
<div class="shotbox"><img class="shot" src="images/cal-16-booking-page.png" alt="予約スケジュールの設定画面"></div>
</div>

---

<!-- header: '予備 3. Google Meet' -->
# 同じ部屋から入るときは「コンパニオンモード」

<div class="vs2">
<div class="col">
<div class="lab">参加前</div>
<img class="shot" src="images/meet-04-companion.png" alt="その他の参加方法とコンパニオンモード">
<div class="d">「その他の参加方法」→「コンパニオンモードを使用」</div>
</div>
<div class="col">
<div class="lab">参加後</div>
<img class="shot" src="images/meet-05-companion-incall.png" alt="コンパニオンモードで参加中の画面">
<div class="d">マイクとスピーカーが最初から切れる。<br>画面共有・チャット・挙手はできる</div>
</div>
</div>
