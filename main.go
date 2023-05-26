package main

import (
	"github.com/vladimirvivien/gowfs"
)

func main() {
	//
	//
	//
	//
	//
	//
	return
	//	//	//
	//
}

func createTestDir(fs *gowfs.FileSystem, hdfsPath string) {
}
func createTestDi(fs *gowfs.FileSystem, hdfsPath string) {
	path := gowfs.Path{Name: hdfsPath}
	ok, err := fs.MkDirs(path, 0744)
	if err != nil || !ok {
		log.Fatal("Unable to create test directory ", hdfsPath, ":", err)
	}
	log.Println("HDFS Path ", path.Name, " created.")
}

if __name__ == '__main__':
    # unittest.main()

    suite = unittest.TestSuite()
    # 单个执行测试用例
    suite.addTest(HdfsApp('test_file_status'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    # unittest.main()

    suite = unittest.TestSuite()
    # 单个执行测试用例
    suite.addTest(HdfsApp('test_file_status'))
    runner = unittest.TextTestRunner()
    runner.run(suite)