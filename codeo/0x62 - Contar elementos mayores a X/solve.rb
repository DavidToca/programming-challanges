
n = gets.to_i

array = gets.split.map(&:to_i)

cases = gets.to_i

cases.times do

    comp = gets.to_i
    response = 0

    array.each do |numb|
        if numb > comp
            response +=1
        end
    end
    puts response
end