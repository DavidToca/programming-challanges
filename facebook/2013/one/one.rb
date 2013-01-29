
entrada = File.open("beautiful_stringstxt.txt","r");
salida = File.open("output.out","w");


m = entrada.readline.chomp.to_i

n_case = 1

entrada.each do |line|

 new_line = line.downcase.gsub(/[^a-z]/,"")


 frequences = {}

 new_line.each_char do |c|

    unless frequences[c] then
      frequences[c] = 1
    else
      frequences[c] +=1
    end

 end

 repetition = frequences.values.sort.reverse

#  puts "repetition =#{repetition}"

  max_value = 26


  result = 0
  repetition.each do |n|

   result += n * max_value

    max_value -= 1


  end

 salida.puts "Case ##{n_case}: #{result}"

 n_case += 1

end


entrada.close
salida.close

