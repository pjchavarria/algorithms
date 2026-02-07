# CLAUDE.md

## Project Overview

This is a collection of algorithm and data structure implementations in Python, organized by problem source. The repository serves as a learning and interview preparation reference. All solutions are self-contained single-file scripts with no external dependencies.

## Repository Structure

```
algorithms/
├── general/           # Fundamental algorithms and data structures (sorting, heaps, trees, graphs)
├── interviewCake/     # Solutions from Interview Cake problems
├── leetcode/          # Solutions to LeetCode problems (~41 files)
├── project euler/     # Solutions to Project Euler math problems
├── README.md
└── CLAUDE.md
```

## Language and Runtime

- **Language**: Python (primarily Python 2 syntax)
- **Python version**: Code uses Python 2 conventions (`print` as statement, `xrange()`, `raw_input`, integer division with `/`). Some files may need Python 2 to run as-is.
- **Dependencies**: Standard library only (`collections`, `heapq`, `math`, `Queue`, `sets`). No external packages.

## Running Code

There is no build system, package manager, or test framework. Each file is a standalone script:

```bash
python <directory>/<filename>.py
```

For example:
```bash
python general/merge-sort.py
python leetcode/two-sum.py
```

## Testing

There is no formal test suite. Each file contains inline test cases at the bottom using `print` statements that output the result alongside the expected value. Verification is done by visual inspection:

```python
print mergeSort([2,63,67,7,85]), [2,7,63,67,85]
```

To verify a solution, run the file and compare the printed actual vs expected values.

## File Conventions

### Naming
- Files use **kebab-case**: `two-sum.py`, `merge-k-sorted-lists.py`
- File names match the problem name from the source platform
- Exception: Project Euler uses `<number>.<PascalCaseName>.py` format (e.g., `34.Digitfactorials.py`)

### File Structure
Each file follows this pattern:
1. **Source link** as a comment (URL to LeetCode, Interview Cake, etc.)
2. **Problem description** in comments
3. **Optional complexity analysis** (`# Time: O(n)`, `# Space: O(n)`)
4. **Implementation** — either standalone functions or a `Solution` class
5. **Inline test cases** — `print` statements at the bottom

### Code Style
- Functions use **camelCase** (`mergeSort`, `highest_product_of_three`) or **snake_case** — no strict convention enforced
- LeetCode solutions typically use a `class Solution:` wrapper matching LeetCode's interface
- General algorithm files use plain functions
- Comments explain algorithmic logic inline
- No type hints or docstring standard enforced

## Adding New Solutions

1. Place the file in the appropriate directory based on its source (`leetcode/`, `general/`, `interviewCake/`, `project euler/`)
2. Name the file in kebab-case matching the problem name
3. Include the source URL as a comment at the top
4. Include the problem description in comments
5. Add test cases as `print` statements at the bottom of the file
6. Use only Python standard library — no external packages

## Key Categories of Problems

| Directory | Focus Areas |
|---|---|
| `general/` | Sorting (merge sort, quick sort), heaps, DFS, BFS, tree traversals, top-K |
| `interviewCake/` | Greedy algorithms, array manipulation |
| `leetcode/` | Arrays, strings, linked lists, trees, graphs, dynamic programming, tries, binary search, math |
| `project euler/` | Mathematical/number theory problems |

## CI/CD

There is no CI/CD pipeline, linter configuration, or automated testing setup.
