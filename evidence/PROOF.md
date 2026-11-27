# Fixture implementation evidence

Command: `python3 -B -m unittest discover -s tests -v`.

## Baseline

```text
test_empty (test_normalizer.NormalizeTests.test_empty) ... ok
test_internal_whitespace (test_normalizer.NormalizeTests.test_internal_whitespace) ... ok
test_order_duplicates_and_case (test_normalizer.NormalizeTests.test_order_duplicates_and_case) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

## RED

```text
test_empty (test_normalizer.NormalizeTests.test_empty) ... ok
test_internal_whitespace (test_normalizer.NormalizeTests.test_internal_whitespace) ... ok
test_order_duplicates_and_case (test_normalizer.NormalizeTests.test_order_duplicates_and_case) ... ok
test_trim_and_omit_blank_entries (test_normalizer.NormalizeTests.test_trim_and_omit_blank_entries) ... FAIL

======================================================================
FAIL: test_trim_and_omit_blank_entries (test_normalizer.NormalizeTests.test_trim_and_omit_blank_entries)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests/test_normalizer.py", line 16, in test_trim_and_omit_blank_entries
    self.assertEqual(normalize(["  North ", "", "\t ", " west", "  North ", " C  d "]),
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                     ["North", "west", "North", "C  d"])
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: ['  North ', '', '\t ', ' west', '  North ', ' C  d '] != ['North', 'west', 'North', 'C  d']

First differing element 0:
'  North '
'North'

First list contains 2 additional elements.
First extra element 4:
'  North '

- ['  North ', '', '\t ', ' west', '  North ', ' C  d ']
?   --     -    ------------        --     -    -    -

+ ['North', 'west', 'North', 'C  d']

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=1)
```

## GREEN

```text
test_empty (test_normalizer.NormalizeTests.test_empty) ... ok
test_internal_whitespace (test_normalizer.NormalizeTests.test_internal_whitespace) ... ok
test_order_duplicates_and_case (test_normalizer.NormalizeTests.test_order_duplicates_and_case) ... ok
test_trim_and_omit_blank_entries (test_normalizer.NormalizeTests.test_trim_and_omit_blank_entries) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
