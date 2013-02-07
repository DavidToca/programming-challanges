require_relative "stack.rb"

class Tower

  def initialize(n)

    @n_disk = n

  end


  #move the disk of number "number" of the from tower to the to tower using the aux tower
  def move(from,to,aux,number)

    towers = {from: from, to: to, aux: aux}

    memory_stack = Stack.new("memory")

    #intial value
    memory_stack.push({from: :from, to: :to, aux: :aux, number: number})

    until memory_stack.empty? do

      memory = memory_stack.pop

      from = towers[memory[:from]]
      to = towers[memory[:to]]
      aux = towers[memory[:aux]]
      number = memory[:number]

      number_on_top = from.seek

    #is number on top
    if number == number_on_top
      number_on_top = from.pop
      puts "move #{number} #{from.name} -> #{to.name}"
      to.push(number_on_top)

    else

      #now lets put back the others numbers on top of him from the auxiliar
      memory_stack.push({:from => memory[:aux], :to => memory[:to], :aux => memory[:from], :number => number-1})


      #now I can move him
      memory_stack.push({:from => memory[:from], :to => memory[:to], :aux => memory[:aux], :number => number})


      #moves all numbers on top of him to the auxiliar tower
      memory_stack.push({:from => memory[:from], :to => memory[:aux], :aux => memory[:to], :number => number-1})

    end

   end


  end

  def solve

    start_stack, aux_stack, end_stack = Stack.new("A"), Stack.new("B"), Stack.new("C")

    #add all disk to first stack
    @n_disk.downto(1){|x| start_stack.push(x)}

    move(start_stack,end_stack,aux_stack,@n_disk)

  end


end


number_of_disk = ARGV[0].to_i

towers = Tower.new(number_of_disk)

towers.solve


