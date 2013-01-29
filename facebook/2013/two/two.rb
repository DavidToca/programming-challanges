
entrada = File.open("input.in","r")
salida = File.open("output.out","w")


m = entrada.readline.chomp.to_i

n_case = 1

entrada.each do |line|

  #open parentesis stack
  op_stack = []

  #close parentesis de sobra

  n_close = 0

  len = line.length)

  result = nil

  for i in 0...(len)

    c = line[i]

    next_char = (i == len-1 )? nil : line[i+1]

    if c == '(' then
      # un nuevo parentesis abierto
      op_stack.push(i)

    elsif c == ')' then

      #si no esta balanceado
      if op_stack.length == 0 then

        #si no tiene 
        if next_char != ":" then
          result=false
          break
        else
          n_close +=1
        end

      #si esta balanceado
      else
        #parentesis estan balanceados
        op_stack.pop()

      end


    end



  end


 end

 salida.puts "Case ##{n_case}: #{result}"

 n_case += 1

end


entrada.close
salida.close

