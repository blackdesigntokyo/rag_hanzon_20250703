# LLMに回答してもらう
from llama_index.llms.ollama import Ollama

def main():
    # Ollamaモデルの初期化: Ollamaクラスをschroneko/gemma-2-2b-jpn-itというモデル名で初期化。
    # llama_indexのOllamaクラスのインスタンスを作成し、llmという変数に代入。Ollamaと連携するためのオブジェクトが生成
    llm = Ollama(
        # 初期化するOllamaモデルの名前を指定
        model="schroneko/gemma-2-2b-jpn-it"
    )

    # LLMへの問い合わせ
    response = llm.complete('東京スカイツリーの高さは？')
    # LLMからの応答を変数responseに格納し、出力
    print(response)

# Pythonスクリプトで非常によく使われるおまじないのようなもの
# 「このファイルが直接実行された時にだけ、特定のコード（ここではmain()関数）を動かす」ための条件分岐
if __name__ == "__main__":
    main()