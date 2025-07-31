# コマンドラインからガチャを実行するためのスクリプト
from gacha import gacha_draw


def main():
    """Main function to run the gacha draw from the command line."""
    result = gacha_draw()
    print(f"ガチャの結果: {result}")


if __name__ == "__main__":
    main()
