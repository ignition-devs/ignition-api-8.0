__all__ = ["Dataset"]

from abc import ABCMeta, abstractmethod


class Dataset(ABCMeta):
    """A dataset is a collection of values arranged in a structured
    format.

    Most datasets are two dimensional -- they can be viewed as a table
    with rows and columns being the two dimensions. Values in a dataset
    are usually accessed by specifying one index for each dimension of
    data (row and column for tables).
    """

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def getColumnCount(cls):
        pass

    @abstractmethod
    def getColumnIndex(cls, name):
        pass

    @abstractmethod
    def getColumnName(cls, col):
        pass

    @abstractmethod
    def getColumnNames(cls):
        pass

    @abstractmethod
    def getColumnType(cls, col):
        pass

    @abstractmethod
    def getColumnTypes(cls):
        pass

    @abstractmethod
    def getPrimitiveValueAt(cls):
        pass

    @abstractmethod
    def getQualityAt(cls, row, col):
        pass

    @abstractmethod
    def getRowCount(cls):
        pass

    @abstractmethod
    def getValueAt(cls, *args):
        pass
