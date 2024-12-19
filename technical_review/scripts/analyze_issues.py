#!/usr/bin/env python3

import os
import re
import yaml
from collections import defaultdict
from datetime import datetime
from pathlib import Path

def parse_markdown_frontmatter(content):
    """Extract YAML frontmatter from markdown files if present."""
    pattern = r'^---\n(.+?)\n---\n'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return {}
    return {}

def parse_markdown_headers(content):
    """Extract headers and their content from markdown."""
    headers = {}
    current_header = None
    current_content = []
    
    for line in content.split('\n'):
        if line.startswith('## '):
            if current_header:
                headers[current_header] = '\n'.join(current_content).strip()
            current_header = line[3:].strip()
            current_content = []
        elif current_header:
            current_content.append(line)
            
    if current_header:
        headers[current_header] = '\n'.join(current_content).strip()
        
    return headers

def analyze_technical_reviews(base_path):
    """Analyze all technical review documents and generate a summary."""
    categories = ['code_quality', 'technical_debt', 'architecture', 
                 'performance', 'security', 'scalability']
    
    summary = {
        'total_issues': 0,
        'by_category': defaultdict(list),
        'by_severity': defaultdict(list),
        'by_risk': defaultdict(list)
    }
    
    for category in categories:
        category_path = Path(base_path) / category
        if not category_path.exists():
            continue
            
        for file_path in category_path.glob('*.md'):
            if file_path.name == 'README.md':
                continue
                
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Parse the document
            metadata = parse_markdown_frontmatter(content)
            headers = parse_markdown_headers(content)
            
            # Extract key information
            issue_data = {
                'title': file_path.stem,
                'category': category,
                'path': str(file_path),
                'severity': headers.get('Impact', '').split('\n')[0] if 'Impact' in headers else 'Unknown',
                'risk': headers.get('Risk', '').split('\n')[0] if 'Risk' in headers else 'Unknown',
                'overview': headers.get('Overview', ''),
                'recommendations': headers.get('Recommendations', '')
            }
            
            # Update summary statistics
            summary['total_issues'] += 1
            summary['by_category'][category].append(issue_data)
            summary['by_severity'][issue_data['severity']].append(issue_data)
            summary['by_risk'][issue_data['risk']].append(issue_data)
    
    return summary

def generate_report(summary, output_file):
    """Generate a markdown report from the analysis."""
    report = f"# Technical Review Summary\n\n"
    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    # Overall statistics
    report += f"## Overview\n\n"
    report += f"Total Issues Identified: {summary['total_issues']}\n\n"
    
    # Issues by category
    report += f"## Issues by Category\n\n"
    for category, issues in summary['by_category'].items():
        report += f"### {category.replace('_', ' ').title()} ({len(issues)})\n\n"
        for issue in issues:
            report += f"- [{issue['title']}]({issue['path']}) - {issue['severity']} severity\n"
        report += "\n"
    
    # High severity issues
    high_severity = summary['by_severity'].get('High', [])
    if high_severity:
        report += f"## High Severity Issues ({len(high_severity)})\n\n"
        for issue in high_severity:
            report += f"### {issue['title']}\n"
            report += f"Category: {issue['category']}\n\n"
            report += f"{issue['overview']}\n\n"
            if issue['recommendations']:
                report += f"Recommendations:\n{issue['recommendations']}\n\n"
    
    with open(output_file, 'w') as f:
        f.write(report)

def main():
    base_path = Path('technical_review')
    summary = analyze_technical_reviews(base_path)
    generate_report(summary, base_path / 'SUMMARY.md')

if __name__ == '__main__':
    main()