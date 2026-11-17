# Refactoring examples

This repository contains small Python examples for practicing clear, behavior-preserving refactoring.

## Simple refactoring exercise

[`simple.py`](simple.py) is the starting point for a short refactoring exercise. It works, but its names and structure could be clearer.

1. Run the program and note its output.
2. Refactor it without changing the calculation or printed output. Look for unclear names, repeated code, and unnecessary indirection.
3. Run it again and compare the results.

With Python 3, run:

```powershell
python simple.py
```

Expected output:

```text
Total: 120.0
Total: 240.0
```

Check that the program still produces this output after refactoring:

```powershell
python -m unittest -v test_simple
```

The test checks the example output, not every possible amount or tax rate.

Once you have tried it, compare your approach with [`simple_solution.py`](simple_solution.py). This is one possible solution: it uses descriptive names, a shared tax-rate constant, a loop, and a direct call to `main`. Run it with `python simple_solution.py`; it should produce the same output. Other solutions are welcome.

## Checkout refactoring exercise

[`checkout.py`](checkout.py) is a deliberately repetitive checkout application. The exercise asks you to characterize its behavior with tests, refactor its design without changing that behavior, and explain the techniques you used.

Read [`exercise.md`](exercise.md) for the full instructions. Run the tests from this folder with:

```powershell
python -m unittest -v
```
