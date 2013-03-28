(defn collatz [n accum]
  (if (= n 1)
    (reverse (cons 1 accum))
    (if (mod n 2)
      (let [a (+ (* 3 n) 1)] (collatz a (cons a accum))
      (let [b (/ n 2)] (collatz b (cons b accum)))))))
(collatz 5 '())