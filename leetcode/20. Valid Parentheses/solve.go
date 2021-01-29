import (
	"container/list"
	"fmt"
)

type Stack struct {
	stack *list.List
}

func (c *Stack) Push(value rune) {
	c.stack.PushFront(value)
}

func (c *Stack) Pop() rune {
	return c.stack.Front().Value.(rune)
}

func (c *Stack) Empty() bool {
	return c.stack.Len() == 0
}

func isValid(s string) bool {

	queue := &Stack{
		stack: list.New(),
	}

	brackets := make(map[rune]rune)

	brackets['}'] = '{'
	brackets[']'] = '['
	brackets[')'] = '('

	runes := []rune(s)

	for _, char := range runes {
		val, ok := brackets[char]
		if ok {

			if queue.Empty() {
				return false
			}

			top := queue.Pop()

			if top != val {
				return false
			}

		} else {
			queue.Push(char)
		}
	}

	return queue.Empty()

}