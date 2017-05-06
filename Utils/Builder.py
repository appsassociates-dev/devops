import os
import shutil

from BeautifulSoup import BeautifulSoup

# from mavenpy.run import Maven
from Utils.Maven import Maven


class Builder:
    def __init__(self):
        self.maven = Maven()

    def buildJar(self, pomDir):
        pomDir_absolutePath = self.getAbsolutePath(pomDir)
        pomfile = pomDir_absolutePath + "/pom.xml"
        print "Path: %s" % pomfile
        # s = self.maven.run_in_dir(pomDir_absolutePath, "clean", "package")
        s = self.maven.run_on_file(pomfile, "clean", "package")

        jarAbosoluPath = pomDir_absolutePath + '/target/' + self.getJarFileNameFromPomXml(pomfile)
        return jarAbosoluPath

    def getAbsolutePath(self, folder):
        # print "Current Dir: %s" % os.getcwd()
        return os.path.join(os.getcwd(), folder)

    def getJarFileNameFromPomXml(self, pomFilePath):
        # pomFilePath = "E:\code\Apps\devops\Config\Source\Spark\pom.xml"
        pom = open(pomFilePath, 'r').read()
        soup = BeautifulSoup(pom)
        artifactid = soup.find('artifactid').string
        version = soup.find('version').string
        jarFileName = artifactid + '-' + version + '.jar'
        return jarFileName

    def buildZip(self, folder, serviceName):
        zipFileName = serviceName + '.zip'
        shutil.make_archive(serviceName, 'zip', folder)
        return zipFileName


if __name__ == '__main__':
    builder = Builder()
    src = 'Config\Source\Spark'
    jar = builder.buildJar(src)
    print jar
    print os.path.isfile(jar)
    # path = builder.getAbsolutePath('Config\Source\Spark')
    # print builder.buildZip(path, 'spark')
    # print builder.getJarFileNameFromPomXml("E:\code\Apps\devops\Config\Source\Spark\pom.xml")
