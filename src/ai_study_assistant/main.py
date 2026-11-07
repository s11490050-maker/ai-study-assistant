"""AI 學習助教：透過 Ollama 串流回答課程問題。"""

import os
import sys

import ollama
from dotenv import load_dotenv

SYSTEM_PROMPT = """
你是一位耐心的繁體中文 AI 學習助教。
請用清楚、正確、適合初學者的方式回答學生的課程問題。
回答時盡量使用：
1. 先給簡短結論
2. 再分步驟解釋
3. 必要時提供簡短範例
若題目資訊不足，請先指出缺少的資訊，不要編造事實。
"""


def ask_ollama(question: str, model: str, host: str) -> None:
    """呼叫 Ollama Chat API，並逐段輸出串流回應。"""
    client = ollama.Client(host=host)
    print("\nAI 助教回答：\n")

    try:
        stream = client.chat(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
            stream=True,
        )
        for chunk in stream:
            content = chunk.get("message", {}).get("content", "")
            print(content, end="", flush=True)
        print("\n")
    except ollama.ResponseError as exc:
        print(f"\nOllama 回應錯誤：{exc}")
        print(f"請確認模型已下載：ollama pull {model}")
        sys.exit(1)
    except Exception as exc:
        print(f"\n無法連線到 Ollama：{exc}")
        print("請先啟動 Ollama，並確認 OLLAMA_HOST 設定正確。")
        sys.exit(1)


def main() -> None:
    load_dotenv()
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")

    print("=" * 48)
    print("        AI 學習助教（Ollama 串流版）")
    print("=" * 48)
    print(f"使用模型：{model}")
    print("輸入課程問題即可提問；輸入 exit 或 q 結束。\n")

    while True:
        try:
            question = input("你的問題 > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再見！")
            break

        if question.lower() in {"exit", "quit", "q"}:
            print("再見！")
            break
        if not question:
            print("請先輸入問題。")
            continue

        ask_ollama(question, model, host)


if __name__ == "__main__":
    main()
