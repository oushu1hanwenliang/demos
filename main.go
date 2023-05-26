package main

import (
	"fmt"
	"log"

	"github.com/vladimirvivien/gowfs"
)

func main() {
	fs, err := gowfs.NewFileSystem(gowfs.Configuration{Addr: "http://43.138.23.161:9000", User: "hadoop"})
	if err != nil {
		log.Fatal(err)
	}
	checksum, err := fs.GetFileChecksum(gowfs.Path{Name: "/user/kafka/hello.txt"})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(checksum)

	createTestDir(fs, "/user/kafka/hello1.txt")
}

func createTestDir(fs *gowfs.FileSystem, hdfsPath string) {
	path := gowfs.Path{Name: hdfsPath}
	ok, err := fs.MkDirs(path, 0744)
	if err != nil || !ok {
		log.Fatal("Unable to create test directory ", hdfsPath, ":", err)
	}
	log.Println("HDFS Path ", path.Name, " created.")
}
