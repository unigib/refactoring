# Refactoring a bloated checkout application

## Overview

**Audience:** learners who can write Python functions, use dictionaries and lists, and run tests  
**Duration:** 90 minutes, with a 60-minute minimum core exercise  
**Format:** pairs or individuals  
**Materials:** Python 3 and the files in this folder; no external packages are required

The checkout application in `checkout.py` calculates totals for three fulfillment methods. It works, but its calculation logic is repeated and mixes several responsibilities. Your job is to improve the design **without changing observable behavior**.

## Learning objectives

By the end, you should be able to:

- Use tests to characterize existing behavior before changing code.
- Identify duplication, long methods, and mixed responsibilities.
- Apply named refactoring techniques in small, testable steps.
- Explain design decisions and demonstrate that behavior was preserved.

## Setup

From this folder, run:

```powershell
python -m unittest -v
```

Read `checkout.py` and `test_checkout.py`. The tests should pass before you start. If they do not, tell the instructor rather than changing the expected results to make them pass.

## Public behavior to preserve

The public entry point is `calculate_order(items, customer_type, coupon, fulfillment)`. Preserve its name, parameters, return shape, error type, and behavior:

- Each item is a dictionary containing `name`, `price_cents`, and `quantity`. Prices and quantities are nonnegative and positive integers, respectively. An order must have at least one item.
- Customer type is `regular` or `vip`. A VIP receives a discount of 10% of the subtotal, rounded down to whole cents.
- The coupon is `None` or `SAVE5`. `SAVE5` discounts up to 500 cents of the amount remaining after the customer discount. Total discounts cannot exceed the subtotal.
- Fulfillment is `standard`, `express`, or `pickup`. Standard shipping costs 500 cents, except that it is free when the amount after discounts is at least 10,000 cents. Express costs 1,200 cents; pickup is free.
- Tax is 8% of the amount after discounts, rounded to the nearest cent with half cents rounded up. Shipping is not taxed.
- Return a dictionary with integer values for `subtotal_cents`, `discount_cents`, `shipping_cents`, `tax_cents`, and `total_cents`.
- Invalid inputs currently raise `ValueError`. Do not mutate the caller's item list or item dictionaries.

The existing tests illustrate the contract, but they are not exhaustive. Preserve other existing behavior too; inspect the code before changing it. The individual fulfillment functions can be reorganized, but keep the public entry point above.

## Schedule

| Time | Activity | Deliverable |
|---|---|---|
| 0–10 min | Read the code and run the baseline tests. Identify at least three smells and their locations. | Brief smell list |
| 10–25 min | Add characterization tests for missing cases. Include threshold, rounding, validation, and non-mutation cases. Run them against the original implementation. | Passing new tests |
| 25–55 min | Refactor in small steps, running tests after each step. Apply at least three named techniques. | Improved code and passing tests |
| 55–60 min | Review the public contract and run the entire suite. | Verified core submission |
| 60–75 min | Review with a partner or instructor. Challenge each other's boundary cases and design choices; improve the solution if needed. | Review notes and any fixes |
| 75–90 min | Prepare and present a short explanation of the changes, trade-offs, and test evidence. | Reflection and demonstration |

## Tasks

1. **Investigate.** Find duplicated calculations, conditional logic, and responsibilities that could be separated. Explain why each is a problem, not merely where it appears.
2. **Protect behavior.** Add tests before changing production code. Cover at least:
   - standard shipping immediately below and at the free-shipping threshold *after discounts*;
   - VIP discount rounding down and tax rounding at a half-cent;
   - a coupon on an order worth less than 500 cents;
   - invalid inputs and caller-owned data remaining unchanged.
3. **Refactor.** Use at least three techniques, such as **Extract Function**, **Replace Magic Number with Named Constant**, **Consolidate Duplicate Conditional Fragments**, or **Replace Conditional with Polymorphism** where justified. Avoid adding abstractions that make this small application harder to understand.
4. **Verify.** Run the full test suite and check the documented public behavior. Do not remove or weaken existing tests. No new checkout features or changes to prices, rounding, or validation rules.
5. **Reflect.** Submit a short note naming the smells, the techniques used, the reason for each, and a trade-off or remaining limitation. Include the command and result of the final test run.

## Submission

Submit the refactored `checkout.py`, the expanded `test_checkout.py`, and the reflection. The reflection may be submitted as a separate document or as text in your learning platform. Be ready to demonstrate the tests and explain one boundary case.

## Assessment rubric (100 points)

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Behavior preservation | 25 | Public interface, results, errors, rounding, and non-mutation are preserved; baseline and added tests pass. |
| Characterization and boundary tests | 25 | Tests are added before the refactor, independently check expected results, and cover all four requested areas including both sides of the shipping threshold. |
| Refactoring techniques | 25 | At least three appropriate named techniques are applied; duplication and mixed responsibilities are meaningfully reduced without needless complexity. |
| Code clarity and maintainability | 15 | Names and structure communicate intent; constants and responsibilities are clear; changes remain focused and consistent. |
| Reflection and communication | 10 | Smells, techniques, rationale, trade-off, and final test command/result are explained accurately. |

For each criterion, award full points when all evidence is present, roughly half for a partially correct submission, and zero when evidence is absent or behavior is substantially broken. Use intermediate scores where appropriate. Tests passing alone do not demonstrate that the requested refactoring techniques were applied.

## Instructor notes

- The first 60 minutes form the minimum complete exercise; allow 90 minutes for review and discussion.
- Before learners edit production code, verify that their new characterization tests pass on the starting application. This establishes that the tests describe existing behavior rather than intended changes.
- Accept multiple reasonable designs. A solution does not need classes or polymorphism to earn full credit.
- Ask learners to explain why shipping uses the discounted amount and why the tax calculation uses integer arithmetic.
- Keep the starting files available separately if you need to reset the exercise for another group.
