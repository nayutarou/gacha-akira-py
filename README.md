# ガチャシミュレーター (Python)

このプロジェクトは、Pythonで実装されたシンプルなガチャシミュレーターです。コマンドラインツールとして、またFastAPIを使用したWeb APIとしてガチャ機能を提供します。

## 🚀 機能

- 設定された確率に基づいてアイテムを抽選
- コマンドラインからのガチャ実行
- FastAPIによるWeb API提供
- 確率分布、境界値、エラーハンドリング、性能に関する包括的なテスト

## 🛠️ セットアップ

プロジェクトをローカルで実行するには、以下の手順に従ってください。

### 1. リポジトリのクローン

```bash
git clone https://github.com/your-username/gacha-akira-py.git
cd gacha-akira-py
```

### 2. 仮想環境の作成とアクティベート

Pythonの依存関係を管理するために仮想環境を使用することを推奨します。

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
```

### 3. 依存関係のインストール

`pip-tools`を使用して依存関係をインストールします。

```bash
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```

## 🏃 実行方法

### コマンドラインツールとして実行

```bash
python main.py
```

### Web APIサーバーとして実行

FastAPIサーバーを起動します。

```bash
python server.py
```

サーバーが起動したら、以下のURLにアクセスできます。

- **ルート**: `http://127.0.0.1:8000/`
- **ガチャ実行**: `http://127.0.0.1:8000/gacha`

## 🧪 テストの実行

プロジェクトのテストは`pytest`を使用して実行できます。

```bash
pytest
```

## ✨ コードの改善点

このプロジェクトは、以下の点においてコードの可読性と保守性が向上しています。

- **Docstringとコメント**: 関数やAPIエンドポイントの目的、引数、戻り値が明確になり、コードの意図が理解しやすくなりました。日本語のコメントも追加されています。
- **設定の一元化**: ポート番号などの設定値が`settings.py`に集約され、設定の管理と変更が容易になりました。
- **ロギングの導入**: `print`文がPythonの`logging`モジュールに置き換えられたことで、ログの管理が柔軟になり、デバッグや運用時の情報収集がしやすくなりました。
- **テストコードの品質**: テストコードはPytestの機能を効果的に利用し、非常に高い可読性と網羅性を持っています。