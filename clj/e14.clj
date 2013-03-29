(defn collatz [n]
  (let [x (first n)]
    (if (= x 1)
      (reverse n)
      (if (= (mod x 2) 0)
	(let [even (/ x 2)] (collatz (cons even n)))
	(let [odd (+ (* 3 x) 1)] (collatz (cons odd n)))))))
