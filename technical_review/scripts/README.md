# Technical Review Analysis Scripts

## analyze_issues.py

This script analyzes the technical review markdown files and generates a summary report.

### Features

- Aggregates issues across all categories
- Generates statistics by severity and risk
- Creates a summary markdown report
- Highlights high-severity issues

### Usage

```bash
# Run from the repository root
python technical_review/scripts/analyze_issues.py
```

### Output

The script generates `technical_review/SUMMARY.md` containing:

1. Overall statistics
2. Issues by category
3. High severity issues with details
4. Recommendations summary

### Requirements

- Python 3.6+
- PyYAML

### Adding New Analysis

The script is modular and can be extended by:

1. Adding new parsing functions
2. Creating additional report sections
3. Implementing different output formats