# NumInt

**NumInt** is a Python tool to approximate definite integrals using standard numerical methods: Left-hand, Right-hand, Midpoint, Trapezoid, and Simpson. It supports both interactive input and CLI commands.

---

## Features

- Approximate definite integrals with 5 standard numerical methods.
- Compute absolute error compared to the exact integral (when possible).
- Supports constants like `pi` and `e`.
- Interactive prompts or CLI arguments.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Drain-Man/NumInt.git
cd NumInt
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

Interactive Mode:
Run the program and follow the prompts:

```bash
python main.py
```

You will be asked for:
- Function `f(x)` (e.g., `sin(x)+x^2`)
- Lower and upper bounds
- Number of subintervals
- Approximation method

CLI Mode:

```bash
python main.py --function "sin(x)" --lower 0 --upper pi --n 100 --method simpson
```

Parameters:

- `--function`: Function to integrate (supports `^` for exponentiation)
- `--lower`: Lower bound of interval
- `--upper`: Upper bound of interval
- `--n`: number of subintervals
- `--method`: Approximation method (`left`, `right`, `center`, `trapezoid`, `simpson`)
- `--version`: Show program version and exit


Pre-built Windows Executable:
Windows users can run **NumInt** without installing Python

1. Download the pre-built `.exe` from the `releases/` folder:

```text
releases/NumInt.exe
```


2. Run from the command line with CLI arguments:

```bash
...\NumInt.exe --function "x^2" --lower 0 --upper 1 --n 10 --method trapezoid
```

3. Run the `.exe` without CLI Arguments to use in interactive mode.
**Note:** This Version is v1.0. Future releases may include updated binaries.

Building the Windows Executable Yourself:
If you prefer to build the `.exe` locally (e.g. for a newer version):

```bash
# Install PyInstaller if not installed
pip install pyinstaller

#From the project root
pyinstaller --onefile --name NumInt --icon Resources\NumInt.ico main.py
```

The `.exe` will appear in the `dist/` folder.

---

## Examples
Interactive Example:

```text
Enter a function f(x): sin(x)
Enter the lower boundary of the interval: 0
Enter the upper boundary of the interval: pi
Enter the number of subintervals: 8
Enter the type of approximation
1: Left
2: Right
3: Center
4: Trapezoid
5: Simpson
(Enter the method's number or name as it appears here): simpson

Simpson approximation: 2.00026917
Exact value:           2
Absolute error:        2.692e-04
```

---

### **Optional**: Add NumInt to PATH (Windows)
If you want to run `NumInt.exe` from any folder without typing the full path:

1. Move `NumInt.exe` to a permanent location (e.g. `C:\Program Files\NumInt\`)
2. Open Environment Variables with `sysdm.cpl` -> Advanced -> Environment Variables.
3. Under "User variables" or "System variables", edit the `Path` variable and add the folder containing `NumInt.exe`.
4. Ok -> Ok -> Ok
5. Open a new Command Prompt and test:

```bash
NumInt.exe --version
```

---

## Credits / Dependencies

- **SymPy** – Python library for symbolic mathematics. [https://www.sympy.org/](https://www.sympy.org/)
