import os

import boto3
from pywebhdfs.webhdfs import PyWebHdfsClient


class HdfsHandler:
    def __init__(self, hadoopHost, hadopPort='50070', user='hadoop'):
        # self.hdfs = PyWebHdfsClient(host='52.14.121.163', port='50070', user_name='hadoop')
        self.hdfs = PyWebHdfsClient(host=hadoopHost, port=hadopPort, user_name=user)
        self.s3_client = boto3.client('s3')

    def copyToHDFS(self, src_path, hdfs_path):
        if hdfs_path.startswith("hdfs"):
            temp_path = hdfs_path.split("8020")
            self.new_hdfs_path = temp_path[1] + '/lib'
            print "New Path: %s" % self.new_hdfs_path
        # create a new client instance
        # print "New Path: %s" % self.new_hdfs_path[1]
        jar_name = os.path.basename(src_path)
        print src_path
        fileContent = open(src_path, 'rb').read()

        # copies file to local for testing purpose
        # with open("E:/temp/java-0.0.2.jar", "wb") as jarfile:
        #     jarfile.write(fileContent)

        # create a new file on hdfs
        print('making new file at: {0}\n'.format(jar_name))
        result = self.hdfs.create_file(self.new_hdfs_path + "/" + jar_name, fileContent, overwrite=True)
        print "HDFS Copy Result: %s" % result
        return result

    def list_hdfs_dir(self, hdfs_path):
        print self.hdfs.list_dir(hdfs_path)


class S3Handler:
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def copyToS3(self, src_path, s3_path):
        file_name = os.path.basename(src_path)
        print "File Name: %s" % file_name
        # str = open(src_path, 'rb').read()
        print 'copying file : %s to S3 Bucket: %s' % (src_path, s3_path)
        self.s3_client.upload_file(src_path, s3_path, file_name)


if __name__ == '__main__':
    sender = HdfsHandler('52.14.121.163')
    src = r'E:\code\Apps\devops\Config\Source\Spark\target\java-0.0.2.jar'
    print "jar file:", os.path.basename(src)
    sender.copyToHDFS(src, 'hdfs://ip-172-31-23-66.us-east-2.compute.internal:8020/user/hadoop/hari')
    sender.list_hdfs_dir('sumo-s3processed')
