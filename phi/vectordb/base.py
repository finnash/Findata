from abc import ABC, abstractmethod
from typing import List

from phi.document import Document


class VectorDb(ABC):
    @abstractmethod
    def create(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def insert(self, document: Document) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(self, query_embedding: List[float], num_documents: int = 5) -> List[Document]:
        raise NotImplementedError