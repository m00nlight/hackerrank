# encoding: utf-8

def solve(nums, qs)
  tmp = nums[1..-1].map { |x| x - nums[0]}
  g = tmp.inject(tmp[0]) { |acc, x| acc.gcd(x)}
  qs.each do |query|
    puts g.gcd(nums[0] + query)
  end
end

def main
  n, q = gets.chomp.split(/\s+/).map { |x| x.to_i}
  nums = gets.split(/\s+/).map { |x| x.to_i}
  qs = []
  (1..q).each do |i|
    num = gets.to_i
    qs << num
  end

  solve(nums, qs)
end

main
