import sys

from EMR.ScheduledJobUpdaterOozie import ScheduledJobUpdaterOozie
from Lambda.LambdaUpdater import LambdaUpdater
from Utils.ChangedResources import ChangedResources

# logging.basicConfig(level=logging.DEBUG)
# _LOG = logging.getLogger(__name__)

if __name__ == '__main__':
    if len(sys.argv) < 2: raise Exception(
        "ERROR: Insufficient number of arguments, changes.txt, config.json and output.json file paths must be given")
    crobj = ChangedResources(sys.argv[1], sys.argv[2], sys.argv[3])
    print "Changed Resources", crobj.changedResources
    changedLambdas = crobj.getChangedLambdas()
    print "Lambdas: ", changedLambdas
    changedEMRs = crobj.getChangedEMRs()
    print "EMRs: ", changedEMRs

    for eachLambda in changedLambdas:
        config = crobj.configReaderObj.getConfiguration(eachLambda)
        # print config
        if LambdaUpdater(config).upload_lambda_fuction():
            print "[SUCCESS] Lamda Function: %s updated successfully" % config['serviceName']
        else:
            print "FAILED to update Lamda Function: %s" % config['serviceName']

    for each in changedEMRs:
        emrConfig = crobj.configReaderObj.getConfiguration(each)
        changedEMRjobs = crobj.identifyEMRjobs(each)
        print "EMR Cluster:%s Jobs Changed:%s " % (each, changedEMRjobs)
        for eachJobChanged in changedEMRjobs:
            jobConfig = crobj.configReaderObj.getEMRJobConfiguration(eachJobChanged['jobName'])
            print "JobName:%s JobType:%s JobConfig:%s" % (
            eachJobChanged['jobName'], eachJobChanged['jobType'], jobConfig)
            if eachJobChanged['jobType'] == 'oozie':
                if ScheduledJobUpdaterOozie(jobConfig, emrConfig).update():
                    print "[SUCCESS] EMR Job: %s updated successfully" % eachJobChanged['jobName']
