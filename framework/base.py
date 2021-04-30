import logging


class LoggingObject:
    def __init__(self, name=None):
        """Base class for all objects with logging

        Args:
            name: logger name. By convention: the name of the logger
            is the name of the object. Get it via __name__ and provide
            as an argument to super class constructor
        """
        if not name:
            name = __name__
        self.logger = logging.getLogger(name)
