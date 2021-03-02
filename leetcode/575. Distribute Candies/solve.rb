# @param {Integer[]} candy_type
# @return {Integer}
def distribute_candies(candy_type)
    max_n_candies = candy_type.length / 2
    unique_candy =  Set.new(candy_type)
    return [max_n_candies, unique_candy.length].min
end