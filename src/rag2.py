# - Settings: llama-index全体の設定を管理
# - SimpleDirectoryReader: ディレクトリからドキュメントを読み込む
# - VectorStoreIndex: ドキュメントをベクトル化して検索可能にする
# - OllamaEmbedding: テキストを数値ベクトルに変換するモデル

from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
import os

def main():
    # モデルの設定
    Settings.llm = Ollama(model="schroneko/gemma-2-2b-jpn-it",)
    Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

    # インデックスの保存先ディレクトリ
    PERSIST_DIR = "./storage"

    # 既存のインデックスがあるかチェック
    if os.path.exists(PERSIST_DIR):
        print("📁 既存のインデックスを読み込んでいます...")
        # 保存済みのインデックスを読み込む
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
        print("✅ インデックスの読み込みが完了しました！")
    else:
        print("🔨 新しいインデックスを作成しています...")
        # ドキュメントの読み込み
        # 先ほど用意したテキストファイルを読み込んでもらう
        documents = SimpleDirectoryReader("./src/data").load_data()

        # ベクトルインデックスの作成
        # イメージとしては意味で検索できる辞書を作成してる
        # 従来（キーワード検索）：「休暇」で検索 → 「休暇」という文字がある文書だけ見つかる
        # ベクトル：「休暇」で検索 → 「有給」「休み」「リフレッシュ」も見つかる
        index = VectorStoreIndex.from_documents(documents)

        # インデックスを保存
        index.storage_context.persist(persist_dir=PERSIST_DIR)
        print("💾 インデックスを保存しました！")

    # クエリエンジンの作成
    # 検索と回答生成の機能を統合した検索エンジン
    query_engine = index.as_query_engine()

    while True:
        user_input = input("あなた: ")

        if user_input.lower() in ["exit", "終了"]:
            print("チャットボットを終了します。")
            break

        if not user_input.strip():
            continue
        # クエリエンジンを使って回答を生成するように変更する
        response = query_engine.query(user_input)
        print(f"🤖: {response.response.strip()}\n")

if __name__ == "__main__":
    main()