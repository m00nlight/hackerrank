# encoding: utf-8

class Trie
  attr_accessor :leaf, :children
  def initialize(leaf)
    self.leaf = leaf
    self.children = { }
  end

  def insert(word)
    return false if self.leaf
    head, tail = word[0], word[1..-1]

    return false if tail.size == 0 and not self.children[head].nil?

    if tail.size == 0
      self.children[head] = Trie.new(true)
      return true
    else
      if self.children[head].nil?
        self.children[head] = Trie.new(false)
      end
      return self.children[head].insert(tail)
    end
  end
end


def main
  n = gets.to_i
  trie = Trie.new(false)
  judge, ans = "GOOD SET", ""
  n.times do |_|
    w = gets.lstrip.rstrip
    if not trie.insert(w)
      judge, ans = "BAD SET", w
      break
    end
  end
  puts [judge, ans].join("\n")
end


main
