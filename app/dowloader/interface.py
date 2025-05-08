from abc import ABC, abstractmethod
from typing import List, Optional
import logging

class IDownloader(ABC):
    """
    Abstract base class for a downloader.
    """

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        logging.basicConfig(level=logging.INFO)

    @abstractmethod
    def download(self, url: str, destination: str) -> Optional[List[dict]]:
        """
        Download a file from the given URL to the specified destination.

        :param url: The URL of the file to download.
        :param destination: The local path where the file should be saved.
        """
        self.logger.info(f"Downloading from {url} to {destination}")
        pass

