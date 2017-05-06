import logging

from pywebhdfs.webhdfs import PyWebHdfsClient

logging.basicConfig(level=logging.INFO)
_LOG = logging.getLogger(__name__)

example_dir = '/tmp'
example_file = '{dir}/example.txt'.format(dir=example_dir)
# example_data = '01010101010101010101010101010101010101010101\n'
rename_dir = '/tmp'

hdfs = PyWebHdfsClient(host='52.14.121.163', port='50070',
                       user_name='hadoop', timeout=10)

listdir_stats = hdfs.list_dir(rename_dir)
print listdir_stats

example_data = "HelloWorld"

hdfs.create_file(example_file, example_data)

file_status = hdfs.get_file_dir_status(example_file)
print file_status
