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
	front := c.stack.Front()
	c.stack.Remove(front)
	return front.Value.(rune)
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
			fmt.Println("char in brakets")
			if queue.Empty() {
				fmt.Println("queue is empty")
				return false
			}

			top := queue.Pop()

			if top != val {
				fmt.Println("top different than val ", top, "!=", val)
				return false
			}

		} else {
			fmt.Println("pushing ", char)
			queue.Push(char)
		}
	}
	fmt.Println("queue is empty? ", queue.Empty())
	return queue.Empty()

}
