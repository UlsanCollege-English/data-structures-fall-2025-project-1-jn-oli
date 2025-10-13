# src/parser.py
from typing import Optional, Tuple, List

def parse_command(line: str) -> Optional[Tuple[str, List[str]]]:
    """
    Parse a single CLI command line.
    Returns (command, args) or None for comments/blank lines.
    Commands are case-sensitive per spec.
    Lines starting with '#' or blank -> None.
    """
    if line is None:
        return None
    s = line.strip()
    if s == "":
        # blank line is handled by CLI (ends session), here return empty to signal it
        return ("", [])
    if s.startswith("#"):
        return None
    parts = s.split()
    cmd = parts[0]
    args = parts[1:]
    return (cmd, args)
