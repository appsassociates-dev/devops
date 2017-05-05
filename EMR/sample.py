import sys
import os
import json
import  urllib2
from JobInfo import JobInfo



class ServiceIdentifier(object):
    def __init__(self, config):
        try:
            # Step 1: Reads the config.json, output.json and chages.txt files are cmd arguments
            self.configuration = json.loads(open(config, "r").read())
        except Exception as error:
            print "FATAL ERROR: %s" % str(error)


if __name__ == '__main__':
    siobj = ServiceIdentifier('E:\config.json')
    oozieurl = siobj.configuration["emr"][0]["oozieUrl"]
    print siobj.configuration
    print oozieurl
    # print siobj.configuration['emr'][0]['oozieJobs'][0]

    jiobj = JobInfo(siobj.configuration['emr'][0]['oozieJobs'][0], oozieurl)
    print jiobj.coordinatorId
    print jiobj.jobName
    print jiobj.jobPath
    print jiobj.srcPath
    print jiobj.oozieUrl
