from log_viewer.interface.data_sourse import ILogSource
from typing import List, Dict, Any


class MockLogSource(ILogSource):
	def __init__(self, items=None):
		self._items = items or [
			{"timestamp": "2026-01-01T00:00:00", "level": "INFO", "message": "mock started"},
			{"timestamp": "2026-01-01T00:00:01", "level": "ERROR", "message": "mock error"},
		]

	def load_logs(self) -> List[Dict[str, Any]]:
		return list(self._items)
