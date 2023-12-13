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
}

func (l *Line) processBit(idx, counts, badCount int) int {
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
		Nums:      nums,
		NumLen:    len(nums),
		Len:       len(springs),
		GoodMaybe: maybeGood,
		BadMaybe:  maybeBad,
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
		go func(idx int, ss string, n []int) {
			results <- result{
				Index: idx,
				Count: processLine(ss, n),
			}
			wg.Done()
		}(j, bits[0], nums)
	}

	var wgCount sync.WaitGroup
	wgCount.Add(1)
	go func() {
		count := 0
		for v := range results {
			fmt.Printf("Line %d: %d\n", v.Index+1, v.Count)
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

/*
import sys


def processme(springs, nums, idx, counts, badCount, minDone, maxDone, running):
    if idx == len(springs):
        if badCount:
            return nums[-1] == badCount and len(nums) == (counts + 1)
        else:
            return len(nums) == counts

    if running < minDone[idx] or running > maxDone[idx]:
        return 0

    rv = 0
    if springs[idx] in '#?': # damaged
        if counts < len(nums) and badCount < nums[counts]:
            rv += processme(springs, nums, idx + 1, counts, badCount + 1, minDone, maxDone, running + 1)

    if springs[idx] in '.?': # good
        if badCount:
            if counts < len(nums) and badCount == nums[counts]:
                rv += processme(springs, nums, idx + 1, counts + 1, 0, minDone, maxDone, running)
        else:
            rv += processme(springs, nums, idx + 1, counts, 0, minDone, maxDone, running)

    return rv

def doit(line):
    rv = 0
    springs, nums = line.split(' ')

    springs = '?'.join([springs] * 5)
    nums = ','.join([nums] * 5)

    nums = [int(x) for x in nums.split(',')]

    shortest = '.'.join('#' * n for n in nums)
    rightest = (' ' * (len(springs) - len(shortest))) + shortest
    leftest = shortest + (' ' * (len(springs) - len(shortest)))

    minDone = [rightest[:i].count('#') for i in range(len(springs))]
    maxDone = [leftest[:i].count('#') for i in range(len(springs))]

    return processme(springs, nums, 0, 0, 0, minDone, maxDone, 0)

i = 0
mm = int(sys.argv[1])
idx = int(sys.argv[2])
for line in sys.stdin:
    line = line.strip()
    if len(line):
        if i % mm == idx:
            rv = doit(line)
            print(i, rv, flush=True)
        i += 1


print(rv)
*/
