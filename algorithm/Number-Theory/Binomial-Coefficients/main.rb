# encoding: utf-8

def solve(n, p)
  r, m, base = 1, n, p
  while m > 0
    r *= (m % base) + 1
    m /= base
  end
  puts (n + 1 - r)
end

def main
  t = gets.to_i
  (1..t).each do |_|
    n, p = gets.split(/\s+/).map(&:to_i)
    solve(n, p)
  end
end

main
