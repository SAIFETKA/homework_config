import sys
import argparse
from parser import parser
from transformer import ConfigTransformer
import toml
from lark.exceptions import LarkError

def main():
    arg_parser = argparse.ArgumentParser(description="Конфигурационный транслятор")
    arg_parser.add_argument("--output", "-o", required=True, help="Выходной TOML файл")
    args = arg_parser.parse_args()

    text = sys.stdin.read()
    try:
        tree = parser.parse(text)
        transformer = ConfigTransformer()
        transformer.transform(tree)

        with open(args.output, "w", encoding="utf-8") as f:
            toml.dump(transformer.vars, f)

        print(f"TOML успешно записан в {args.output}")
    except LarkError as e:
        print(f"Синтаксическая ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
