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
    return re.sub(r"(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]*)",
                  lambda match: match.group(1) + "=" + redaction
                  if match.group(1) in fields else match.group(0), message)
