"""Utility functions with no data lineage."""
import logging

def get_logger(name):
    return logging.getLogger(name)

def format_date(dt):
    return dt.strftime("%Y-%m-%d")