

class VertexError(Exception):
    """
    Custom exception for the Graph class
    """
    def __init__(self, message: str) -> None:
        """
        Creates a VertexError instance
        :param message: the error message
        """
        self.__message = message


class EdgeError(Exception):
    """
    Custom exception for the Graph class
    """
    def __init__(self, message: str) -> None:
        """
        Creates an EdgeError instance
        :param message: the error message
        """
        self.__message = message
