import argparse
from rich.console import Console
from rich.style import Style
from calculator.formula import addition, subtraction, multiplication, division


def main():
    console = Console()

    style = Style(color="purple")
    style_title = Style(
        color="green",
        bold=True,
    )

    console.print("Calc CLI\n", style=style_title)

    parser = argparse.ArgumentParser(description="Calculadora CLI")

    parser.add_argument(
        "-a", "--addition", nargs="+", type=float, help="Realizar uma adição"
    )
    parser.add_argument(
        "-s", "--subtraction", nargs="+", type=float, help="Realizar uma subtração"
    )
    parser.add_argument(
        "-m",
        "--multiplication",
        nargs="+",
        type=float,
        help="Realizar uma multiplicação",
    )
    parser.add_argument(
        "-d", "--division", nargs=2, type=float, help="Realizar uma divisão"
    )

    args = parser.parse_args()

    result = None
    operation = None

    if args.addition:
        result = addition(*args.addition)
        operation = "adição"
    elif args.subtraction:
        result = subtraction(*args.subtraction)
        operation = "subtração"
    elif args.multiplication:
        result = multiplication(*args.multiplication)
        operation = "multiplicação"
    elif args.division:
        result = division(args.division[0], args.division[1])
        operation = "divisão"

    if result is not None:
        if result % 1 == 0:
            formated_result = int(result)
        else:
            formated_result = float(result)

        if operation == "adição":
            console.print(
                f"Operação de {operation}: {args.addition} = {formated_result}",
                style=style,
            )
        elif operation == "subtração":
            console.print(
                f"Operação de {operation}: {args.subtraction} = {formated_result}",
                style=style,
            )
        elif operation == "multiplicação":
            console.print(
                f"Operação de {operation}: {args.multiplication} = {formated_result}",
                style=style,
            )
        elif operation == "divisão":
            console.print(
                f"Operação de {operation}: {args.division} = {formated_result}",
                style=style,
            )
        else:
            console.print(
                "Nenhuma operação especificada. Use -h para obter ajuda.", style=style
            )


if __name__ == "__main__":
    main()
