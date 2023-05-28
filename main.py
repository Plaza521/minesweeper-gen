import field


def main() -> None:
    minesweeper_field = field.Field(9, 10)
    minesweeper_field.generate()
    print(minesweeper_field.field)


if __name__ == '__main__':
    main()
