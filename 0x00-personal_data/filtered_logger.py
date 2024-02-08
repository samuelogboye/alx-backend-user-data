#!/usr/bin/env python3
'''
Filtered Logger
'''
import re


def filter_datum(
        fields: list,
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    Filter the message
    """
    for field in fields:
        message = re.sub(
            rf"{field}=.*?{separator}",
            rf"{field}={redaction}{separator}",
            message)
    return message
