# 社内AI勉強会 第1回（2026-09-27 / 90分）

Googleドキュメント・カレンダー・Meetの3本立て。対象は全社員（非エンジニア中心）。
本編29枚＋予備4枚（各ツールの3つ目。時間が余ったときだけ使う）。

| ファイル | 中身 |
|---|---|
| `slides.md` | Marp本体 |
| `theme/deck.css` | テーマ（engineer-studyから流用＋実画面用のクラス追加） |
| `content-notes.md` | 話す内容の正本 |
| `docs/shot-list.md` | 撮影する実画面の一覧 |
| `images/` | 実画面のスクリーンショット（モザイク済み。原本は `images/raw/`） |
| `scripts-mask.py` | 原本にモザイクをかけて `images/` を再生成 |
| `session1-plan-revised.md` | 企画書＋Slack要件を整理した改訂案 |
| `proposal.md` | 9/3時点の企画共有（Gmail前提・旧） |

## ビルド

```sh
marp slides.md -o build/slides.html --theme theme/deck.css --html --allow-local-files < /dev/null
marp slides.md -o build/slides.pdf  --theme theme/deck.css --html --allow-local-files < /dev/null
marp slides.md --images png -o build/png/s.png --theme theme/deck.css --html --allow-local-files < /dev/null
python3 scripts-check-margins.py
ffmpeg -y -pattern_type glob -i 'build/png/s.0*.png' -vf "scale=512:288,tile=4x7" -frames:v 1 build/sheet/contact.png
```
