# encoding: utf-8

def solve(arr)
  min_value = arr.min
  ans = []
  ((min_value - 5)..min_value).each do |i|
    tmp = arr.map { |x|
      (x - i) / 5 + (x - i) % 5 / 2 + (x - i) % 5 % 2
    }.inject(:+)
    ans.push(tmp)
  end
  ans.min
end

def main
  contents = $stdin.readlines
  contents[1..-1].each_slice(2) do |_, arr|
    arr = arr.split(" ").map(&:to_i)
    puts solve(arr)
  end
end

main
