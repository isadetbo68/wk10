from abc import ABC, abstractmethod
from typing import List, Dict, Any


class ILogSource(ABC):
	"""Interface for log sources.

	Implementations should provide `load_logs()` which returns a list
	of dictionaries (one per log entry).
	"""

	@abstractmethod
	def load_logs(self) -> List[Dict[str, Any]]:
		raise NotImplementedError()
