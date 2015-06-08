# encoding: utf-8
require 'set'

def pre_calc
  ret = Set.new([0,1,2,3,4,5,6,7,8,9])
  deque = [0,1,2,3,4,5,6,7,8,9]
  maxn = 10 ** 18
  len = lambda { |x| x.to_s.size}

  while (not deque.empty?)
    elem = deque.shift
    l = len.call(elem)
    (0..2).each { |j|
      c = elem * (l + j)
      if (not ret.include?(c)) and c <= maxn and (len.call(c) == l + j)
        ret.add(c)
        deque.push(c)
      end
    }
  end

  ret
end

def main
  nums = pre_calc
  n = gets.to_i
  (1..n).each do |t|
    a, b = gets.split(/\s+/).map(&:to_i)
    puts nums.select { |x| x >= a and x <= b}.size
  end
end

main
