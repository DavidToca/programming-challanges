var exists = struct{}{}

type set struct {
	m map[int]struct{}
}

func NewSet() *set {
	s := &set{}
	s.m = make(map[int]struct{})
	return s
}

func (s *set) Add(value int) {
	s.m[value] = exists
}

func (s *set) Remove(value int) {
	delete(s.m, value)
}

func (s *set) Contains(value int) bool {
	_, c := s.m[value]
	return c
}

func min(x, y int) int {
	if x > y {
		return y
	}
	return x
}

func distributeCandies(candyType []int) int {
	max_n_candies := len(candyType) / 2

	unique_candy := NewSet()
	unique_candy_count := 0

	for c := range candyType {
		if !unique_candy.Contains(candyType[c]) {
			unique_candy.Add(candyType[c])
			unique_candy_count = unique_candy_count + 1
		}
	}
	return min(max_n_candies, unique_candy_count)
}