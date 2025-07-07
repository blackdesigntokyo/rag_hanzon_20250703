# RAGハンズ プロジェクト

## 概要
このプロジェクトは、LLM（Large Language Model）を使用したチャット機能を提供します。

## ファイル構成
```
src/
├── chat1.py          # LLMチャット機能
├── chat2.py          # 追加チャット機能
├── rag.py            # RAG機能
├── rag2.py           # 追加RAG機能
└── data/
    └── sample.txt    # サンプルデータ
```

## セットアップ

### 必要なパッケージ
```bash
pip install llama-index
```

### Ollamaのインストール
1. [Ollama公式サイト](https://ollama.ai/)からOllamaをダウンロード・インストール
2. 日本語対応モデルをダウンロード：
```bash
ollama pull schroneko/gemma-2-2b-jpn-it
```

## 使用方法

### chat1.py
LLMを使用して質問に回答を得る基本的なチャット機能です。

```bash
python src/chat1.py
```

#### 機能
- Ollamaモデル（schroneko/gemma-2-2b-jpn-it）を使用
- 日本語での質問応答
- シンプルなテキスト出力

#### コードの説明
```python
# LLMの初期化
llm = Ollama(model="schroneko/gemma-2-2b-jpn-it")

# 質問の実行
response = llm.complete('東京スカイツリーの高さは？')
print(response)
```

## 注意事項
- Ollamaが起動していることを確認してください
- 初回実行時はモデルのダウンロードに時間がかかる場合があります
- インターネット接続が必要です

## トラブルシューティング

### インポートエラーが発生する場合
```bash
pip install llama-index
```

### Ollamaが起動していない場合
```bash
ollama serve
```

### モデルが見つからない場合
```bash
ollama list
ollama pull schroneko/gemma-2-2b-jpn-it
```

## 仮想環境を有効化する
source .venv/bin/activate

## chat1.py

「東京スカイツリーの高さは？」という質問に回答し、その回答がコンソールに表示されます。

python3 src/chat1.py

## chat2.py

プロンプトを入力し、返答してもらう。終了するには　"exit"もしくは"終了"　と入力。

python3 src/chat2.py
