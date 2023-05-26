package main

import (
	"log"

	"github.com/vladimirvivien/gowfs"
)

func main() {
	return
}

func createTestDir(fs *gowfs.FileSystem, hdfsPath string) {
	path := gowfs.Path{Name: hdfsPath}
	ok, err := fs.MkDirs(path, 0744)
	if err != nil || !ok {
		log.Fatal("Unable to create test directory ", hdfsPath, ":", err)
	}
	log.Println("HDFS Path ", path.Name, " created.")
}
