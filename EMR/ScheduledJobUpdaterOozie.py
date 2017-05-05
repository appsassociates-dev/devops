import json
import urllib2
from ScheduledJobUpdater import ScheduledJobUpdater

class ScheduledJobUpdaterOozie(ScheduledJobUpdater):
    def __init__(self, jobConfig, oozieUrl):
        self.jobConfiguration = jobConfig
        self.oozieUrl = oozieUrl
        ScheduledJobUpdater.__init__(self)
        print("Creating ScheduledJobUpdaterOozie instance:%d!" % (id(self)))
        pass

    def getExecutablepath(self):
        # gets the appPath from Oozie thorugh rest API using self.getJobInfo()
        # and returns the HDFS path for the job
        # where binary can be updated/replaced
        jobInfo = self.getJobInfo()
        print json.dumps(jobInfo)
        return jobInfo['coordJobPath']

    def getJobInfo(self):
        # returns the job info
        url = self.oozieUrl + 'v1/job/' + self.jobConfiguration['jobId'] + '?show=info'
        print url
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        output = response.read()
        return json.loads(output)

    def makeBundle(self):
        # makes bundle (.zip/jar) as per the language convention and return the bundle path
        if self.jobConfiguration['language'] == 'python':
            print "call python zip bundler"
        elif self.jobConfiguration['language'] == 'java':
            print "call java jar bundler"
        return None

    def updateExecutable(self, src, target):
        # updates the bundle in the target (ex. hdfs)
        return None


    def update(self):
        # updates the oozie job
        target = self.getExecutablepath()
        src = self.makeBundle()
        self.updateExecutable(src, target)
        if self.jobConfiguration['storageType'] == 'hdfs':
            print "call hdfs handler"
        elif self.jobConfiguration['storageType'] == 's3':
            print "call hdfs handler"
        return None