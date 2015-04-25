(require 'clojure.string)

(def max-size 50)

(def memo1 (java.util.HashMap.))
(def memo2 (java.util.HashMap.))

(doseq [i (range (inc max-size))]
  (doseq [j (range (inc max-size))]
    (. memo1 put (str i "," j) -1)
    (. memo2 put (str i "," j) -1)))

(doseq [i (range 2)]
  (doseq [j (range 2)]
    (. memo1 put (str i "," j) 0)))

(. memo2 put (str "0,0") 0)


(defn solve1
  [x y]
  (letfn [(grundy [p q]
            (let [s (java.util.HashSet.)
                  res (atom 0)]
              (if (not (= (. memo1 get (str p "," q)) -1))
                (. memo1 get (str p "," q))
                (do
                  (. s add (grundy (- p 2) (- q 1)))
                  (. s add (grundy (- p 1) (- q 2)))
                  (while (. s contains @res)
                    (swap! res inc))
                  (. memo1 put (str p "," q) @res)
                  @res))))]
    (grundy x y)))

(defn solve2
  [x y]
  (letfn [(grundy [p q]
            (let [s (java.util.HashSet.)
                  res (atom 0)]
              (if (not (= (. memo2 get (str p "," q)) -1))
                (. memo2 get (str p "," q))
                (do
                  (doseq [i (range p)]
                    (. s add (grundy i q)))
                  (doseq [j (range q)]
                    (. s add (grundy p j)))
                  (doseq [d (range 1 (inc (min p q)))]
                    (. s add (grundy (- p d) (- q d))))
                  (while (. s contains @res)
                    (swap! res inc))
                  (. memo2 put (str p "," q) @res)
                  @res))))]
    (grundy x y)))

(defn outer
  [xs ys]
  (for [x xs
        y ys]
    (vector x y)))

(def ans1 (reduce #(assoc %1 %2 (solve1 (first %2) (last %2)))
                  {} (outer (range max-size)
                            (range max-size))))

(def ans2 (reduce #(assoc %1 %2 (solve2 (first %2) (last %2)))
                  {} (outer (range max-size)
                            (range max-size))))

(defn solve
  [a b c d]
  (let [x (get ans1 [a, b])
        y (get ans2 [c d])]
    (if (= (bit-xor x y) 0)
      (println "LOSE")
      (println "WIN"))))


(let [t (Integer/parseInt (read-line))]
  (doseq [_ (range t)]
    (let [[a, b, c, d] (map #(Integer/parseInt %)
                            (clojure.string/split (read-line) #"\s+"))]
      (solve a b c d))))
