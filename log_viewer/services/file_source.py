from typing import List, Dict, Any
from log_viewer.interface.data_sourse import ILogSource


class FileLogSource(ILogSource):
	"""Simple file-backed log source: each line is a log message."""

	def __init__(self, path: str, encoding: str = "utf-8"):
		self.path = path
		self.encoding = encoding

	def load_logs(self) -> List[Dict[str, Any]]:
		logs: List[Dict[str, Any]] = []
		try:
			with open(self.path, encoding=self.encoding) as f:
				for ln in f:
					logs.append({"message": ln.rstrip("\n")})
		except FileNotFoundError:
			return []
		return logs
