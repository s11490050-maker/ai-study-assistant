# AI 學習助教（Ollama 串流版）

一個使用 Python 與 Ollama 建立的命令列 AI 學習助教。使用者輸入課程或程式設計問題後，程式會呼叫本機大型語言模型，並以**串流（streaming）**方式逐段顯示回答。

## 功能特色

- 使用 Python 3.10+ 與 `uv` 管理專案及套件。
- 透過 Ollama 呼叫本機 LLM，不需要雲端 API Key。
- 使用 `stream=True`，模型產生內容時即時顯示，不必等待整篇回答完成。
- 使用繁體中文系統提示詞，要求模型以初學者容易理解的方式解釋。
- 可在 `.env` 設定 Ollama 主機與模型名稱。

## 專案結構

```text
ai-study-assistant/
├── .github/
│   └── workflows/
│       └── deploy-pages.yml
├── docs/
│   └── index.html
├── src/
│   └── ai_study_assistant/
│       ├── __init__.py
│       └── main.py
├── .env.example
├── .gitignore
├── .python-version
├── pyproject.toml
└── README.md
```

## 執行環境

- Python 3.10 或更新版本
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/)

## 安裝與執行

### 1. 安裝 Ollama 並下載模型

先安裝 Ollama，啟動 Ollama 後，在終端機執行：

```bash
ollama pull qwen2.5:3b
```

也可以改用其他已安裝的 Ollama 對話模型。

### 2. 複製專案並建立環境

```bash
git clone https://github.com/你的GitHub帳號/ai-study-assistant.git
cd ai-study-assistant
uv sync
```

### 3. 設定環境變數

將 `.env.example` 複製成 `.env`：

Windows PowerShell：

```powershell
Copy-Item .env.example .env
```

macOS / Linux：

```bash
cp .env.example .env
```

預設設定如下：

```env
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=qwen2.5:3b
```

若使用不同模型，修改 `OLLAMA_MODEL` 即可。`.env` 已加入 `.gitignore`，不可將含有個人設定或金鑰的 `.env` 上傳到 GitHub。

### 4. 啟動程式

```bash
uv run study-assistant
```

輸入問題即可開始對話；輸入 `q` 或 `exit` 結束。

## 執行結果範例

以下為示意對話，實際回答會依模型版本與問題而不同。

```text
================================================
        AI 學習助教（Ollama 串流版）
================================================
使用模型：qwen2.5:3b
輸入課程問題即可提問；輸入 exit 或 q 結束。

你的問題 > Python 的 list 和 tuple 有什麼差別？

AI 助教回答：

簡單來說，list（串列）可以修改，tuple（元組）建立後不能修改。
1. list 使用中括號，例如：scores = [80, 90, 100]
2. tuple 使用小括號，例如：scores = (80, 90, 100)
3. 如果資料需要新增、刪除或修改，通常使用 list；
   如果資料固定不變，可以考慮 tuple。
...
```

## GitHub Pages 作品頁

本專案的作品介紹頁位於 `docs/index.html`。GitHub Actions 會在推送至 `main` 分支時自動部署 GitHub Pages。

啟用方式：

1. 將專案推送到 GitHub，預設分支命名為 `main`。
2. 進入 GitHub 專案的 **Settings → Pages**。
3. 在 **Build and deployment → Source** 選擇 **GitHub Actions**。
4. 推送一次新的 commit，或到 **Actions** 分頁手動執行 `Deploy GitHub Pages`。
5. Workflow 顯示綠色勾勾後，回到 **Settings → Pages** 查看網站網址。

## AI 使用說明

- **使用工具：** Ollama，本機大型語言模型執行工具。
- **使用位置：** Python 程式的 `ask_ollama()` 函式，透過 `ollama` Python 套件呼叫本機服務。
- **使用能力：** 串流輸出（Streaming）。程式設定 `stream=True`，並逐段讀取 `chunk` 的 `message.content`，即時印出模型回答。
- **自行撰寫／修改：** 自行設計「AI 學習助教」主題、繁體中文系統提示詞、互動式輸入流程、環境變數讀取、錯誤處理與 README。
- **自行驗證：** 下載模型後實際執行，測試一般問題、空白輸入、結束指令及 Ollama 未啟動時的錯誤提示。模型回答可能有誤，重要資訊仍需自行查證。

## 注意事項

- 本專案預設使用本機 Ollama，不需 API 金鑰，也不會將問題送至雲端服務。
- `.env` 不可提交至 GitHub；只提交 `.env.example`。
- AI 回答僅供學習參考，請自行確認正確性。
