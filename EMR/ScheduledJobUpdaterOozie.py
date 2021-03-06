import json
import urllib2

from ScheduledJobUpdater import ScheduledJobUpdater
from Utils.Builder import Builder
from Utils.CopyHandler import HdfsHandler


class ScheduledJobUpdaterOozie(ScheduledJobUpdater):
    def __init__(self, jobConfig, emrConfig):
        self.jobConfiguration = jobConfig
        self.oozieUrl = emrConfig['oozieUrl']
        self.masterHost = emrConfig['masterHost']
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
            print "calling java jar bundler"
            builder = Builder()
            jar = builder.buildJar(self.jobConfiguration['folder'])
            print "Jar File Location: %s" % jar
            return jar
        return None

    def updateExecutable(self, src, target):
        # updates the bundle in the target (ex. hdfs)
        if self.jobConfiguration['storageType'] == 'hdfs':
            print "calling hdfs handler"
            sender = HdfsHandler(self.masterHost)
            return sender.copyToHDFS(src, target)

        elif self.jobConfiguration['storageType'] == 's3':
            print "calling s3 handler"
        return None

    def update(self):
        # updates the oozie job
        target = self.getExecutablepath()
        print "target: %s" % target
        src = self.makeBundle()
        res = self.updateExecutable(src, target)
        return res
