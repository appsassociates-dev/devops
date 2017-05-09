import boto3
from sys import platform

if "win" in platform.lower():
    print platform


class EMRUtil:
    def __init__(self):
        self.emr_client = boto3.client(service_name='emr', region_name='us-east-2')

    def addToKnownHosts(self, clusterID):
        instances = self.emr_client.list_instances(ClusterId=clusterID)
        hostsList = []
        for each in instances['Instances']:
            hostDict = {}
            hostDict['publicIP'] = each['PublicIpAddress']
            hostDict['hostname'] = each['PrivateDnsName']
            hostsList.append(hostDict)
        print hostsList

        # hosts = C:\Windows\System32\Drivers\etc\hosts incase Windows
        # host = /etc/hosts incase Linux
        hostsFile = "/etc/hosts"

        if "win" in platform.lower():
            hostsFile = "C:\Windows\System32\Drivers\etc\hosts"
            self.isWindows = True
            print "Windows"

        with open(hostsFile, 'r') as file:
            self.fileContent = file.read()
            print "File Content:", self.fileContent

        with open(hostsFile, 'a') as file:
            for each in hostsList:
                print self.fileContent.__contains__(each['publicIP'])
                if not self.fileContent.__contains__(each['publicIP']):
                    if self.isWindows:
                        line = "\n" + each['publicIP'] + '\t' + each['hostname'] + "\n"
                    else:
                        # for Linux host configuration
                        line = "\n" + each['publicIP'] + '\t' + each['hostname'] + "\n"
                    file.write(line)
        return True


if __name__ == '__main__':
    print "Hello"
    emr = EMRUtil()
    emr.addToKnownHosts(clusterID="j-136HI8CCU08C4")
