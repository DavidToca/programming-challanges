n = gets.to_i

a = gets.split.map(&:to_i)

def solve(array)
    min_number = -1000000001

    last_number = min_number

    array.each do |numb|
        if last_number >numb
            return "Desordenado"
        end
        last_number = numb
    end
    return "Ordenado"
end

puts(solve(a))