import time 

class TimeError(Exception) : 
    """A custom exception used to report errors in use of Timer Class"""

class Timer : 
    def __init__(self) : 
        self._start_time = None
        self._elapsed_time = None

    def start(self) : 
        """start a new timer"""
        if self._start_time is not None :
            raise TimeError("Timer is running. Use .stop()")
        self._start_time = time.perf_counter()

    def stop(self) : 
        """Save the elapsed time and re-initialize timer"""
        if self._start_time is None : 
            raise TimeError("Timer is not running. User .start()")
        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

    def elapsed(self) : 
        """Report elapsed time"""
        if self._elapsed_time is None : 
            raise TimeError("Timer is not running. Use .start()")
        retunr (self._elapsed_time)

    def __str__(self) : 
        """print() prints elapsed time"""
        return str(self._elapsed_time)