# ガチャシミュレーターバックエンド

このプロジェクトは、ガチャシミュレーターのバックエンドAPIを提供します。FastAPIフレームワークを使用しており、ガチャの抽選ロジックと確率設定を管理します。

## 機能

- **ガチャ抽選**: 設定された確率に基づいてアイテムを抽選します。
- **CORS対応**: フロントエンドからのリクエストを許可するためにCORSが設定されています。

## プロジェクト構造

- `main.py`: アプリケーションのエントリーポイント。
- `server.py`: FastAPIアプリケーションの定義とAPIエンドポイント。
- `gacha.py`: ガチャの抽選ロジックを実装。
- `settings.py`: ガチャの確率設定を定義。
- `tests/`: テストコードを格納。
  - `test_boundary.py`: 確率設定の境界値テスト。
  - `test_distribution.py`: ガチャ結果の分布テスト。
  - `test_error_handling.py`: エラーハンドリングテスト。
  - `test_mock.py`: モックを使用したテスト。
  - `test_performance.py`: 性能テスト。
- `pytest.ini`: pytestの設定ファイル。

## セットアップ

1.  **リポジトリのクローン**:

    ```bash
    git clone https://github.com/your-username/gacha-akira-py.git
    cd gacha-akira-py
    ```

2.  **仮想環境の作成とアクティベート**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **依存関係のインストール**:

    ```bash
    pip install -r requirements.txt
    ```

## 実行方法

APIサーバーを起動します。

```bash
python server.py
```

サーバーはデフォルトで `http://localhost:8000` で起動します。

## APIエンドポイント

### ガチャを引く

- **エンドポイント**: `/gacha`
- **メソッド**: `GET`
- **説明**: ガチャを1回引き、抽選結果を返します。
- **レスポンス**: `{"result": "[抽選されたアイテム]"}`

**例**:

```
GET http://localhost:8000/gacha
```

## テスト

テストを実行するには、プロジェクトのルートディレクトリで以下のコマンドを実行します。

```bash
pytest
```

詳細なテスト結果と`print`文の出力を表示するには、`-v -s`オプションを使用します。

```bash
pytest -v -s
```

## 貢献

貢献を歓迎します！バグ報告や機能リクエストは、GitHubのIssueトラッカーをご利用ください。

## ライセンス

[LICENSE](LICENSE)ファイルを参照してください。
