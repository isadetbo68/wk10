from log_viewer.services.file_source import FileLogSource
from log_viewer.services.csv_source import CsvLogSource
from log_viewer.services.mock_sourse import MockLogSource
import sys


def make_source(path: str):
    path_l = (path or "").lower()
    if path_l.endswith(".csv"):
        return CsvLogSource(path)
    if path_l.endswith(".txt") or path_l.endswith(".log"):
        return FileLogSource(path)
    if path_l == "mock" or not path:
        return MockLogSource()
    # default fallback
    return FileLogSource(path)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else ""
    src = make_source(path)
    logs = src.load_logs()
    print(f"Loaded {len(logs)} logs from {path or 'mock'}")
    for i, l in enumerate(logs[:20], start=1):
        print(i, l)


if __name__ == "__main__":
    main()
