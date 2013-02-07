class Stack


  def initialize(name)

    @name = name

    @data = []

  end


  def push(info)

    @data.push(info)


  end


  def pop

    @data.pop

  end


  def seek

    @data.last

  end

  def name

    "Stack #{@name}"

  end

  def empty?
    @data.empty?
  end


  def to_s

    @data.to_s

  end


end
