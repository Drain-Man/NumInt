import sympy as sp
from numint.numint import num_int
import argparse
import sys

VERSION = "1.0"
x = sp.symbols('x')
locals_dict = {"pi": sp.pi, "Pi": sp.pi, "PI": sp.pi, "e": sp.E, "E": sp.E}

def get_function(cli_input=None):
    """Return a valid callable f(x) and sympy expression"""
    while True:
        if cli_input:
            expr = cli_input.replace("^", "**")
        else:
            expr = input("Enter a function f(x): ").replace("^", "**")

        try:
            sym_expr = sp.sympify(expr, locals=locals_dict)
            undefined_symbols = sym_expr.free_symbols - {x}
            if undefined_symbols:
                raise ValueError(f"Expression contains undefined symbols: {', '.join(str(s) for s in undefined_symbols)}")
            f = sp.lambdify(x, sym_expr, "math")
            # Test evaluation at 0
            f(0)
            return f, sym_expr
        except Exception as e:
            if cli_input:
                print("Invalid function:", e)
                sys.exit(1)
            else:
                print("Invalid function. Use a proper expression like sin(x)+x**2")

def get_limit(value, name):
    """Return a float limit from CLI or prompt interactively"""
    while True:
        try:
            val = float(sp.N(sp.sympify(value.lower() if isinstance(value, str) else value, locals=locals_dict)))
            return val
        except Exception:
            if value is not None:
                print(f"Invalid {name} limit")
                sys.exit(1)
            value = input(f"Enter the {name} boundary of the interval: ")

def get_subintervals(cli_value=None):
    while True:
        try:
            n = cli_value if cli_value is not None else int(input("Enter the number of subintervals: "))
            if n <= 0:
                raise ValueError
            return n
        except Exception:
            if cli_value is not None:
                print("Invalid number of subintervals")
                sys.exit(1)
            cli_value = None
            print("Invalid number of subintervals")

def get_method(cli_value=None, subintervals=None):
    mapping = {"1":"left", "2":"right", "3":"center", "4":"trapezoid", "5":"simpson"}
    valid_methods = set(mapping.values())
    while True:
        method = cli_value.lower() if cli_value else input(
            "Enter the type of approximation\n1: Left\n2: Right\n3: Center\n4: Trapezoid\n5: Simpson\n(Enter number or name): "
        ).strip()
        if method in mapping:
            method = mapping[method]
        if method.lower() in valid_methods:
            if method == "simpson" and subintervals % 2 != 0:
                print("Simpson's Rule requires an even number of subintervals")
                if cli_value:
                    sys.exit(1)
                cli_value = None
                continue
            return method
        print("Invalid method")
        if cli_value:
            sys.exit(1)
        cli_value = None

def main():
    parser = argparse.ArgumentParser(description="Approximate definite integrals using numerical methods.")
    parser.add_argument("--version", action="version", version=f"NumInt {VERSION}")
    parser.add_argument("--function", type=str, help="Function f(x), e.g., sin(x)+x**2")
    parser.add_argument("--lower", type=str, help="Lower boundary of the interval")
    parser.add_argument("--upper", type=str, help="Upper boundary of the interval")
    parser.add_argument("--n", type=int, help="Number of subintervals")
    parser.add_argument("--method", type=str,
                        choices=["left", "right", "center", "trapezoid", "simpson"],
                        help="Approximation method")
    args = parser.parse_args()

    while True:
        f, sym_expr = get_function(args.function)
        lower_limit = get_limit(args.lower, "lower")
        upper_limit = get_limit(args.upper, "upper")
        if upper_limit <= lower_limit:
            print("Upper limit must be greater than lower limit")
            if args.upper:
                sys.exit(1)
            args.upper = None
            continue
        subintervals = get_subintervals(args.n)
        method = get_method(args.method, subintervals=subintervals)
        typedisp = method.capitalize()

        try:
            result = num_int(f, lower_limit, upper_limit, subintervals, method)
        except (ZeroDivisionError, ValueError):
            print("\nFunction is undefined somewhere in the interval. Try again.\n")
            if args.function:
                sys.exit(1)
            continue
        except TypeError:
            print("\nInvalid function.\n")
            if args.function:
                sys.exit(2)

        try:
            exact_val = float(sp.N(sp.integrate(sym_expr, (x, lower_limit, upper_limit))))
            error = abs(exact_val - result)
            print(f"\n{typedisp} approximation: {result:.10g}")
            print(f"Exact value:           {exact_val:.10g}")
            print(f"Absolute error:        {error:.3e}\n")
        except Exception:
            print(f"{typedisp} approximation: {result:.10g}")
            print("Exact value unavailable.\n")

        if args.function:
            break

        continue_prompt = input("Perform another calculation? (y/n): ").strip().lower()
        if continue_prompt != "y":
            break

if __name__ == "__main__":
    main()