import sys
import os
import json
import  urllib2

class JobInfo:
    def __init__(self, config, oozieURL):
        self.oozieUrl = oozieURL
        # self.__configuration = json.loads(open(app_properties, "r").read())
        self.__configuration = config
        print "Configuration: %s" % self.__configuration
        a = self.__getJobInfo()
        self.coordinatorId = a["coordJobId"]
        self.jobName = a["coordJobName"]
        self.jobPath = a["coordJobPath"]
        self.srcPath = config["folder"]

    def __getJobInfo(self):
        url = self.oozieUrl + 'v1/job/' + self.__configuration['jobId'] + '?show=info'
        print url
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        output = response.read()
        return json.loads(output)