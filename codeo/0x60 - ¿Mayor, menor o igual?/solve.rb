a, b = gets.split.map(&:to_i)

if(a == b) then
  puts "="
else if(a > b) then
  puts ">"
else 
  puts "<"
end