from abc import abstractmethod, ABCMeta

class ScheduledJobUpdater:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def getExecutablepath(self):
        # gets the appPath from Oozie thorugh rest API using self.getJobInfo()
        # and returns the HDFS path for the job
        # where binary can be updated/replaced
        return None

    @abstractmethod
    def getJobInfo(self):
        #returns the job info
        return None

    @abstractmethod
    def makeBundle(self):
        # makes bundle (.zip/jar) as per the language convention and return the bundle path
        return None

    @abstractmethod
    def updateExecutable(self, src, target):
        # updates the bundle in the target (ex. hdfs)
        return None
