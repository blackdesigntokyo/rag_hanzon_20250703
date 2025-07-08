# RAGハンズ プロジェクト

## 概要
本プロジェクトは、RAG（Retrieval-Augmented Generation）および大規模言語モデル（LLM）を活用した日本語チャット・情報検索システムのサンプル実装です。  
Ollamaを用いたローカルLLM推論、社内規約や社員プロフィール等のダミーデータを使ったRAG処理、対話型チャットなど、実践的なAI活用例を含みます。

## ディレクトリ構成
```
src/
├── chat1.py          # LLMへの単発質問・応答サンプル
├── chat2.py          # 対話型チャットサンプル（プロンプト入力可）
├── rag1.py           # RAG（検索拡張生成）処理サンプル
├── rag2.py           # 追加RAG機能サンプル
└── data/
    └── sample.txt    # 社内規約・社員プロフィール等のダミーデータ
storage/
├── default__vector_store.json  # ベクトルストア（検索用埋め込みデータ）
├── image__vector_store.json    # 画像ベクトルストア
├── graph_store.json            # グラフストア
├── docstore.json               # ドキュメントストア
└── index_store.json            # インデックス情報
README.md                       # このファイル
.gitattributes                  # Git属性設定
```

## 主な機能
- Ollamaを利用した日本語LLMチャット
- RAG（検索拡張生成）による社内文書検索・要約
- サンプルデータによる社内規約・社員情報の検索
- ベクトルストア・インデックス管理

## セットアップ

### 必要なパッケージ
```bash
pip install llama-index
```

### Ollamaのインストール
1. [Ollama公式サイト](https://ollama.ai/)からOllamaをダウンロード・インストール
2. 日本語モデルを取得
```bash
ollama pull schroneko/gemma-2-2b-jpn-it
```

### 仮想環境の有効化（推奨）
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 使い方

### LLMチャット（単発質問）
```bash
python src/chat1.py
```
- 例：「東京スカイツリーの高さは？」と質問し、LLMの回答を表示

### 対話型チャット
```bash
python src/chat2.py
```
- 任意の日本語プロンプトを入力し、LLMの返答を得る
- "exit"または"終了"で終了

### RAGによる検索・要約
- rag1.py, rag2.pyを参照（詳細は各スクリプト内コメント参照）

## データについて
- `src/data/sample.txt`：社内規約・社員プロフィール・会社概要などのダミーデータ
- `storage/`配下：ベクトルストアやインデックス等、検索用の中間データ

## 注意事項
- Ollamaが起動している必要があります（`ollama serve`）
- モデルの初回ダウンロードには時間がかかる場合があります
- インターネット接続が必要です

## トラブルシューティング
- インポートエラー：`pip install llama-index`
- Ollama未起動：`ollama serve`
- モデルが見つからない：`ollama pull schroneko/gemma-2-2b-jpn-it`

---

このREADMEはプロジェクト全体の構成・機能・使い方を網羅的に説明しています。  
さらに詳しい使い方やカスタマイズ方法が必要な場合はご指示ください。
