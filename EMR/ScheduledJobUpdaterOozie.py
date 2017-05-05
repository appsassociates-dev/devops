import json
import urllib2
import logging
from abc import abstractmethod, ABCMeta
from ScheduledJobUpdater import ScheduledJobUpdater
from JobInfo import JobInfo

class ScheduledJobUpdaterOozie(ScheduledJobUpdater):
    def __init__(self):
        ScheduledJobUpdater.__init__(self)
        self.logger.error("Creating ScheduledJobUpdaterOozie instance:%d!" % (id(self)))
        pass

    def FindMatchingJob(self, jobIdToSearch):
        return None

    def GetPathOfExecutable(self, jobDetail):
        return None

    def OverwriteExecutable(self, jobDetail, pathOfExeToUpdate):
        return None
