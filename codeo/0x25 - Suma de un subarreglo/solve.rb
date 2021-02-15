n = gets.to_i

array = gets.split.map(&:to_i)

cases = gets.to_i

total = 0

array.map!{ |numb|
    total+=numb
    total
}

cases.times do

    p, q = gets.split.map(&:to_i)

    if p == 0
        puts array[q]
    else
        puts array[q] - array[p-1]
    end


end