package main

import (
	"errors"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
	"sync"
)

type Line struct {
	Len       int
	NumLen    int
	Nums      []int
	GoodMaybe []bool
	BadMaybe  []bool

	cachedAnswers map[int]int
}

func (l *Line) processBit(idx, counts, badCount int) int {
	key := (idx << 32) | (counts << 16) | badCount
	rv, ok := l.cachedAnswers[key]
	if ok {
		return rv
	}
	rv = l.expProcessBit(idx, counts, badCount)
	l.cachedAnswers[key] = rv
	return rv
}

func (l *Line) expProcessBit(idx, counts, badCount int) int {
	if idx == l.Len {
		if badCount == 0 {
			if l.NumLen == counts {
				return 1
			} else {
				return 0
			}
		} else {
			if l.Nums[l.NumLen-1] == badCount && l.NumLen == (counts+1) {
				return 1
			} else {
				return 0
			}
		}
	} else {

		rv := 0
		if l.GoodMaybe[idx] {
			if badCount == 0 {
				rv += l.processBit(idx+1, counts, 0)
			} else {
				if counts < l.NumLen && badCount == l.Nums[counts] {
					rv += l.processBit(idx+1, counts+1, 0)
				}
			}
		}
		if l.BadMaybe[idx] {
			if counts < l.NumLen && badCount < l.Nums[counts] {
				rv += l.processBit(idx+1, counts, badCount+1)
			}
		}
		return rv
	}
}

func processLine(springs string, nums []int) int {
	maybeGood, maybeBad := make([]bool, len(springs)), make([]bool, len(springs))
	for i, ch := range springs {
		if ch == '#' || ch == '?' {
			maybeBad[i] = true
		}
		if ch == '.' || ch == '?' {
			maybeGood[i] = true
		}
	}
	return (&Line{
		Nums:          nums,
		NumLen:        len(nums),
		Len:           len(springs),
		GoodMaybe:     maybeGood,
		BadMaybe:      maybeBad,
		cachedAnswers: make(map[int]int),
	}).processBit(0, 0, 0)
}

func doit() error {
	type result struct {
		Index int
		Count int
	}

	inb, err := io.ReadAll(os.Stdin)
	if err != nil {
		return err
	}

	results := make(chan result)
	var wg sync.WaitGroup

	lines := strings.Split(string(inb), "\n")
	for j, line := range lines {
		bits := strings.Split(line, " ")
		if len(bits) != 2 {
			return errors.New("bad line")
		}

		for i := 0; i < len(bits); i++ {
			var s []string
			for j := 0; j < 5; j++ {
				s = append(s, bits[i])
			}
			sep := "?"
			if i > 0 {
				sep = ","
			}
			bits[i] = strings.Join(s, sep)
		}

		numsS := strings.Split(bits[1], ",")
		nums := make([]int, len(numsS))
		for i, s := range numsS {
			nums[i], err = strconv.Atoi(s)
			if err != nil {
				return err
			}
		}
		wg.Add(1)
		go func(idx int, ss string, n []int, ll string) {
			results <- result{
				Index: idx,
				Count: processLine(ss, n),
			}
			wg.Done()
		}(j, bits[0], nums, line)
	}

	var wgCount sync.WaitGroup
	wgCount.Add(1)
	go func() {
		count := 0
		for v := range results {
			// fmt.Printf("Line %d: %d\n", v.Index+1, v.Count)
			count += v.Count
		}
		fmt.Printf("Total: %d\n", count)
		wgCount.Done()
	}()

	wg.Wait()
	close(results)

	wgCount.Wait()

	return nil
}

func main() {
	err := doit()
	if err != nil {
		log.Fatal(err)
	}
}
