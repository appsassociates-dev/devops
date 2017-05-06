from ScheduledJobUpdater import ScheduledJobUpdater


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


class ScheduledJobUpdaterAWSDataPipe(ScheduledJobUpdater):
    def __init__(self):
        ScheduledJobUpdater.__init__(self)
        self.logger.error("Creating ScheduledJobUpdaterAWSDataPipe instance:%d!" % (id(self)))
        pass

    def FindMatchingJob(self, jobIdToSearch):
        pass

    def GetPathOfExecutable(self, jobDetail):
        pass

    def OverwriteExecutable(self, jobDetail, pathOfExeToUpdate):
        pass
