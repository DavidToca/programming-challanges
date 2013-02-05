# just for testing
 $stdin = File.open("input.in")

t = gets.chomp.to_i

t.times do

  input = gets.chomp.split("")

  letters = input.uniq

  counts = {}

  letters.each{ |l| counts[l] = input.count(l) }

  total = 0

  counts.each do |letter, count|

    total += count / 2 + count % 2

  end

  puts total

end
