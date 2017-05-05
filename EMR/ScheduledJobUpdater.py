from abc import abstractmethod, ABCMeta
from JobInfo import JobInfo

class Logger:
    def __init__(self):
        pass

    def debug(self, message):
        self.__print(message)

    def error(self, message):
        self.__print(message)

    def info(self, message):
        self.__print(message)

    def warn(self, message):
        self.__print(message)

    def __print(self, message):
        print message

class ScheduledJobUpdater:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.logger = Logger()
        pass

    def UpdateExecutable(self, jobIdToSearch, pathOfExeToUpdate):
        jobDetail = self.FindMatchingJob(jobIdToSearch)
        if jobDetail == None:
            self.logger.error("Job:%s doesn't exist! " % (jobIdToSearch))
            return

        uri = self.GetPathOfExecutable(jobDetail)
        if uri == None:
            self.logger.error("Failed to get executable path for Job:%s!" % (jobIdToSearch))
            return

        status = self.OverwriteExecutable(jobDetail, pathOfExeToUpdate)
        if not status:
            self.logger.error("Failed to overwrite executable for Job:%s!" % (jobIdToSearch))
            return

    @abstractmethod
    def FindMatchingJob(self, jobIdToSearch):
        return JobInfo()

    @abstractmethod
    def GetPathOfExecutable(self, jobDetail):
        return ExecutableInfo()

    @abstractmethod
    def OverwriteExecutable(self, jobDetail, pathOfExeToUpdate):
        return None

    def __copyToS3(self, source, destination):
        return None

    def __copyToHdfs(self, source, destination):
        return None

    def __copyToLocalFs(self, source, destination):
        return None

