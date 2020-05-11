package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"

	"github.com/sunhay/mit-6.824-2017/mapreduce"
)

// Run using `time go run wc.go master sequential pg-*.txt`
// Correct if `sort -n -k2 mrtmp.wcseq | tail -10` produces:
/*
	he: 34077
	was: 37044
	that: 37495
	I: 44502
	in: 46092
	a: 60558
	to: 74357
	of: 79727
	and: 93990
	the: 154024
*/
// Or just run `bash ./test-wc.sh`

//
// The map function is called once for each file of input. The first
// argument is the name of the input file, and the second is the
// file's complete contents. You should ignore the input file name,
// and look only at the contents argument. The return value is a slice
// of key/value pairs.
//
func mapF(filename string, contents string) []mapreduce.KeyValue {
	words := strings.FieldsFunc(contents, func(r rune) bool { return !unicode.IsLetter(r) })
	kvs := make([]mapreduce.KeyValue, 1)
	for _, word := range words {
		kvs = append(kvs, mapreduce.KeyValue{word, "1"})
	}
	return kvs
}

//
// The reduce function is called once for each key generated by the
// map tasks, with a list of all the values created for that key by
// any map task.
//
func reduceF(key string, values []string) string {
	return strconv.Itoa(len(values))
}

// Can be run in 3 ways:
// 1) Sequential (e.g., go run wc.go master sequential x1.txt .. xN.txt)
// 2) Master (e.g., go run wc.go master localhost:7777 x1.txt .. xN.txt)
// 3) Worker (e.g., go run wc.go worker localhost:7777 localhost:7778 &)
func main() {
	if len(os.Args) < 4 {
		fmt.Printf("%s: see usage comments in file\n", os.Args[0])
	} else if os.Args[1] == "master" {
		var mr *mapreduce.Master
		if os.Args[2] == "sequential" {
			mr = mapreduce.Sequential("wcseq", os.Args[3:], 3, mapF, reduceF)
		} else {
			mr = mapreduce.Distributed("wcseq", os.Args[3:], 3, os.Args[2])
		}
		mr.Wait()
	} else {
		mapreduce.RunWorker(os.Args[2], os.Args[3], mapF, reduceF, 100)
	}
}