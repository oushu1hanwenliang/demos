from hdfs import InsecureClient
import unittest


class HdfsApp(unittest.TestCase):

    def setUp(self):
        print('-----------test start-----------')
        self.fs = InsecureClient(url='http://IP:50070', user='用户名', root='/')

    def test_mkdir(self):
        """
        创建HDFS文件夹
        :return:
        """
        self.fs.makedirs('/hdfsapi/test')

    def test_text(self):
        """
        查看HDFS内容
        :return:
        """
        with self.fs.read('/README.txt', encoding='utf-8', delimiter='\n') as reader:
            for line in reader:
                print(line)

    def test_write(self):
        """
        HDFS创建文件并写入内容，查看参数replication设置副本数
        :return:
        """
        s = 'this is python conn hdfs'
        with self.fs.write("/hdfsapi/test/ppppp.txt", encoding="utf-8", replication=2) as f:
            f.write(s)

    def test_replication(self):
        """
        设置HDFS的文件的副本数
        :return:
        """
        print(self.fs.set_replication('/hdfsapi/test/a.txt', 2))

    def test_delete(self):
        """
        HDFS删除文件
        :return:
        """
        self.fs.delete('/hdfsapi/test/c.txt')

    def test_rename(self):
        """
        HDFS文件重命名
        :return:
        """
        old_path = '/hdfsapi/test/a.txt'
        new_path = '/hdfsapi/test/c.txt'
        self.fs.rename(old_path, new_path)

    def test_upload_from_local_file(self):
        """
        上传本地文件到HDFS
        :return:
        """
        local_path = 'F:\\Code\\hadoop\\hadoop_hdfs\\hello.txt'
        hdfs_path = '/hdfsapi/test/testdir/'
        self.fs.upload(hdfs_path, local_path)

    def test_down_to_local_file(self):
        """
        下载HDFS文件到本地
        :return:
        """
        local_path = 'F:\\Code\\hadoop\\hadoop_hdfs\\'
        hdfs_path = '/hdfsapi/test/b.txt'
        self.fs.download(hdfs_path, local_path)

    def test_list(self):
        """
        返回目录下的文件，第二个参数，返回文件的相关信息
        :return:
        """
        print(self.fs.list('/hdfsapi/test/', True))

    def test_recursive(self):
        """
        深度遍历该目录下的所有文件
        :return:
        """
        for item in self.fs.walk('/hdfsapi/test/'):
            print(item)

    def test_file_status(self):
        """
        查看文件块信息
        :return:
        """
        print(self.fs.status('/hdfsapi/test/b.txt'))

    def tearDown(self):
        print('-------test finished--------------')


if __name__ == '__main__':
    # unittest.main()

    suite = unittest.TestSuite()
    # 单个执行测试用例
    suite.addTest(HdfsApp('test_file_status'))
    runner = unittest.TextTestRunner()
    runner.run(suite)