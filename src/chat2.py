# llama_indexライブラリを使って、Ollamaでホストされている大規模言語モデル（LLM）と対話型のチャットを行うためのプログラム
# ユーザーが対話的にプロンプト（質問や指示）を入力し、それに対してLLMが応答を返すループが追加
from llama_index.llms.ollama import Ollama

def main():
    # Ollamaクラスを、schroneko/gemma-2-2b-jpn-itというモデルで初期化
    llm = Ollama(
        model="schroneko/gemma-2-2b-jpn-it"
    )

    # 終了条件を満たすまで、無限ループでの対話を続ける
    while True:
        # ユーザーからの入力を待ち、それをuser_input変数に格納
        user_input = input("あなた: ")

        # 終了条件：ユーザーが「exit」または「終了」とキーワードを入力したら対話を終了
        if user_input.lower() in ["exit", "終了"]:
            print("チャットボットを終了します。")
            break

        # ユーザーが何も入力せずにEnterキーを押した場合、その入力をスキップして次のループに進む
        # strip()メソッドは、文字列の先頭と末尾にある空白文字（スペース、タブ、改行など）をすべて削除するPythonの組み込み関数。
        if not user_input.strip():
            continue

        # ユーザーの入力をLLMに送信し、その応答をresponse変数に格納します。
        response = llm.complete(user_input)
        # LLMからの応答を表示
        # また、チャットボットの応答であることを示すために「🤖:」というプレフィックスを付けています。
        # 応答の末尾に余分な空白文字がある場合があるため、strip()メソッドで削除。
        print(f"🤖: {response.text.strip()}\n")

if __name__ == "__main__":
    main()