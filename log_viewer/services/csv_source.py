import csv
from typing import List, Dict, Any
from log_viewer.interface.data_sourse import ILogSource


class CsvLogSource(ILogSource):
    """CSV-backed log source. Expects a header row; returns each row as dict."""

    def __init__(self, path: str, encoding: str = "utf-8"):
        self.path = path
        self.encoding = encoding

    def load_logs(self) -> List[Dict[str, Any]]:
        logs: List[Dict[str, Any]] = []
        try:
            with open(self.path, newline="", encoding=self.encoding) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert OrderedDict to regular dict
                    logs.append(dict(row))
        except FileNotFoundError:
            return []
        return logs
