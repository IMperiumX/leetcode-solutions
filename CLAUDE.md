# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a LeetCode solutions repository organized for learning and reference. It contains Python solutions to various algorithmic problems with detailed documentation and explanations.

## Repository Structure

### Core Directories

- **`problems/`**: Each LeetCode problem has its own folder named with format `{number}-{problem-name}/`
  - Each problem folder contains:
    - `README.md`: Problem description, constraints, examples, and solution explanation
    - `solution.py` or `solution_{approach}.py`: Python implementation(s) with different algorithmic approaches
    - Multiple solution files may exist for different techniques (e.g., `solution_two_pointers.py`, `solution_hashset.py`)

- **`topics/`**: Markdown files documenting data structures and algorithms
  - Each topic file explains concepts and references related problems
  - Files include: `array.md`, `Binary-Search.md`, `Dynamic Programming.md`, etc.

### Key Files

- **`README.md`**: Auto-generated main documentation with problem tables and progress tracking
- **`update_readme.py`**: Script that automatically updates the README.md with new problems and statistics
- **`.github/workflows/update_readme.yml`**: GitHub Action that runs `update_readme.py` on every push to main

## Development Workflow

### Adding New Problems

1. Create problem folder: `problems/{number}-{kebab-case-name}/`
2. Add `README.md` with problem description following existing format:
   - Title: `# {number}. {Problem Name}, Difficulty: {Easy|Medium|Hard}`
   - Problem link and description
   - Solution approach explanation
3. Add solution file(s): `solution.py` or `solution_{approach}.py`
4. Update relevant topic files in `topics/` directory if needed

### Solution File Conventions

- Use `class Solution:` structure with LeetCode method signatures
- Multiple approaches should have descriptive suffixes (e.g., `_two_pointers`, `_binary_search`)
- Include docstrings and comments explaining algorithm approach
- Follow Python naming conventions

### README Management

- **Never manually edit the main README.md** - it's auto-generated
- The `update_readme.py` script parses problem folders and generates statistics tables
- GitHub Actions automatically updates README on pushes to main
- Script dependencies: `beautifulsoup4`, `requests`

### Running Individual Solutions

Use VS Code's Python debugger configuration or run directly:
```bash
cd problems/{problem-folder}/
python solution.py
```

### Testing Solutions

- No formal test framework is configured
- Test cases are typically included in solution files using `if __name__ == "__main__":` blocks
- Solutions can be run directly to verify output

## Code Standards

- Follow LeetCode class structure: `class Solution:` with appropriate method signatures
- Use clear, descriptive variable names
- Include complexity analysis in README files
- Document different algorithmic approaches when multiple solutions exist
- Maintain consistent file naming conventions

## Topic Documentation

When adding problems related to specific data structures or algorithms:
1. Update or create the relevant topic file in `topics/`
2. Link the problem in the topic's problem list
3. Ensure topic files explain core concepts and reference related problems

## Branch Strategy

- Work directly on `main` branch
- GitHub Actions will automatically update README on commits
- No specific testing or build requirements beyond Python execution