"""
    This program updates the given source  zip file to the AWS Lambda for given Lambda function ARN.
"""
import os
import boto3

from Utils.Builder import Builder


class LambdaUpdater(object):
    def __init__(self, config):
        self.__config = config  # Place holder for lambda configuration
        self.__client = boto3.client('lambda')
        self.__absoluteFolderPath = self.__getAbsolutePath(self.__config['folder'])


    def __getAbsolutePath(self, folder):
        # print "Current Dir: %s" % os.getcwd()
        return os.path.join(os.getcwd(), folder)

    def upload_lambda_fuction(self):

        builder = Builder()

        if self.__config['language'] == "python":
            self.__file_location = builder.buildZip(self.__absoluteFolderPath, self.__config['serviceName'])
        elif self.__config['language'] == "java":
            self.__file_location = builder.buildJar(self.__config['pomDir'])

        file_bytes_read = open(self.__file_location, "rb").read()

        response = self.__client.update_function_code(
            FunctionName=self.__config['arn'],
            ZipFile=file_bytes_read,
            Publish=True
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        return False
