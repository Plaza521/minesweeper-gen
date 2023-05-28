import field
from sys import argv


def main() -> None:
    if len(argv) != 3:
        raise SystemExit(
            f"Usage: {argv[0]} <mines amount> <length of field>"
        )
    try:
        mines_amount = int(argv[1])
        field_size = int(argv[2])
    except ValueError:
        raise SystemExit(
            f"Usage: {argv[0]} <mines amount> <length of field>"
        )
    minesweeper_field = field.Field(field_size, mines_amount)
    minesweeper_field.generate()
    print(minesweeper_field)


if __name__ == '__main__':
    main()
