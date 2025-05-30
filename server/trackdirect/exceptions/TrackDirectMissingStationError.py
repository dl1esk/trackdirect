from server.trackdirect.exceptions.TrackDirectGenericError import TrackDirectGenericError


class TrackDirectMissingStationError(TrackDirectGenericError):
    """Raised when unexpected format of a supported packet format is encountered
    """

    def __init__(self, message, data=None):
        """The __init__ method.

        Args:
            message (str): Exception message
            data (dict):   Packet data that caused parse error. Defaults to None.
        """
        super().__init__(message)
        self.packet = data if data is not None else {}
