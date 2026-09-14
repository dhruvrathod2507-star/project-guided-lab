"""
Report Generator
================
Generates formatted security incident reports as plain text.

YOUR TASKS:
1. Implement generate_report() to produce a formatted report string
2. Support multiple report types: daily summary, threat analysis, model performance
"""

from datetime import datetime


def generate_report(report_type, data=None):
    """
    Generate a formatted incident report.

    The report should include:
    - Header with date and report type
    - Executive summary (2-3 sentences)
    - Key statistics from the supplied data
    - Detailed findings
    - Recommendations

    Args:
        report_type (str): One of 'daily_summary', 'threat_analysis', 'model_performance'
        data (dict, optional): Statistics and findings to include

    Returns:
        str: Formatted report text ready for display or download
    """
    # TODO: Implement
    pass
