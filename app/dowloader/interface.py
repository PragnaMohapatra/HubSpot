from abc import ABC, abstractmethod
from typing import List, Optional

class IDownloader(ABC):
    """
    Abstract base class for a downloader.
    """

    @abstractmethod
    def download(self, url: str, destination: str) -> Optional[List[dict]]:
        """
        Download a file from the given URL to the specified destination.

        :param url: The URL of the file to download.
        :param destination: The local path where the file should be saved.
        """
        pass

