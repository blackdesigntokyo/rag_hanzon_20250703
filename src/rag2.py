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
    # 作成したインデックスを保存するディレクトリの名前を定義。次回以降、このディレクトリにインデックスがあれば再利用できます。
    PERSIST_DIR = "./storage"

    # 既存のインデックスがあるかチェック
    # 指定された保存先にインデックスが既に存在するかを確認。
    if os.path.exists(PERSIST_DIR):
        # 存在する場合、既存のインデックスを読み込み
        print("📁 既存のインデックスを読み込んでいます...")
        # 保存済みのインデックスを読み込む
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
        print("✅ インデックスの読み込みが完了しました！")
    else:
        # インデックスが存在しない場合、新しいインデックスを作成
        print("🔨 新しいインデックスを作成しています...")
        # ドキュメントの読み込み
        # ディレクトリ内にあるすべてのテキストファイルなどのドキュメントを読み込み。
        # これらのドキュメントが、チャットボットが質問に答えるための「知識ベース」となります。
        documents = SimpleDirectoryReader("./src/data").load_data()

        # ベクトルインデックスの作成（読み込んだドキュメントを元に）
        # イメージとしては意味で検索できる辞書を作成してる
        # 従来（キーワード検索）：「休暇」で検索 → 「休暇」という文字がある文書だけ見つかる
        # ベクトル：「休暇」で検索 → 「有給」「休み」「リフレッシュ」も見つかる
        index = VectorStoreIndex.from_documents(documents)

        # インデックスを保存
        index.storage_context.persist(persist_dir=PERSIST_DIR)
        print("💾 インデックスを保存しました！")

    # クエリエンジンの作成
    # 作成したインデックスを使って、ユーザーの質問を処理し、回答を生成するための「クエリエンジン」を作成。
    # このエンジンは、インデックスからの情報検索と、LLM（大規模言語モデル）による回答生成の両方を担当します。
    query_engine = index.as_query_engine()

    while True:
        user_input = input("あなた: ")

        if user_input.lower() in ["exit", "終了"]:
            print("チャットボットを終了します。")
            break

        if not user_input.strip():
            continue
        # クエリエンジンを使って回答を生成するように変更する
        # ユーザーの入力（質問）を query_engine に渡し、回答を生成。
        # query_engine は、インデックスから関連情報を検索し、その情報とユーザーの質問を基にLLMが回答を作成します。
        response = query_engine.query(user_input)
        print(f"🤖: {response.response.strip()}\n")
        # .strip() は、回答の先頭や末尾の不要な空白文字を取り除くために使われます。

if __name__ == "__main__":
    main()