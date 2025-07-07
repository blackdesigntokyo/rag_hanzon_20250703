# - Settings: llama-index全体の設定を管理
# - SimpleDirectoryReader: ディレクトリからドキュメントを読み込む
# - VectorStoreIndex: ドキュメントをベクトル化して検索可能にする
# - OllamaEmbedding: テキストを数値ベクトルに変換するモデル

from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

def main():
    # モデルの設定:使用するAIモデルを設定します。
    # ユーザーの質問に対して回答を生成するAIモデルを設定
    Settings.llm = Ollama(model="schroneko/gemma-2-2b-jpn-it",)
    # ドキュメントや質問のテキストを「数値のベクトル」（埋め込みベクトル）に変換するためのモデルを設定
    # この変換により、テキストの意味的な類似性を計算できるようになります。
    Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

    # ドキュメントの読み込み:特定のディレクトリにあるテキストファイルを読み込みます。
    # ./src/data というディレクトリの中にあるすべてのファイル（テキストファイルなどを想定）を読み込む準備をしています
    # .load_data() 実際にファイルを読み込み、documents変数に格納。チャットボットが参照する知識ベースとなります。
    documents = SimpleDirectoryReader("./src/data").load_data()

    # ベクトルインデックスの作成:
    # documentsの内容をベクトル化し、「ベクトルインデックス」を作成し、「意味」で検索できるように変換。
    # 従来（キーワード検索）：「休暇」で検索 → 「休暇」という文字がある文書だけ見つかる
    # ベクトル：「休暇」で検索 → 「有給」「休み」「リフレッシュ」も見つかる読み込んだ
    index = VectorStoreIndex.from_documents(documents)

    # クエリエンジンの作成:質問を受け付け、検索し、回答を生成する仕組みを準備します。
    # ベクトルインデックスから関連する情報を検索し、その情報に基づいてAIモデルが回答を生成
    query_engine = index.as_query_engine()

    while True:
        # ユーザーからの入力を受け取ります。
        user_input = input("あなた: ")

        # ユーザーが「exit」または「終了」と入力したら、チャットボットを終了します。
        if user_input.lower() in ["exit", "終了"]:
            print("チャットボットを終了します。")
            break

        # ユーザーが何も入力せずにEnterを押した場合（空白のみの場合）、何もせず次のループに進みます。
        if not user_input.strip():
            continue
        
        # ユーザーの質問 user_input をクエリエンジンに渡し、回答を生成させます。
        # クエリエンジンが生成した回答（response.response）を表示。
        response = query_engine.query(user_input)
        print(f"🤖: {response.response.strip()}\n")
        # .strip() は回答の前後の空白を取り除くために使われます。

#このPythonスクリプトが直接実行された場合にのみ main() 関数を呼び出す、Pythonの一般的なお約束です。
if __name__ == "__main__":
    main()