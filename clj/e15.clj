(defn fac [n]
  "recursive factorial"
  (if (< n 2) 1
      (* n (fac (- n 1)))))

(defn choose [n, k]
  "Binomial coefficient choose(n, k)"
  (/ (fac n)
     (* (fac (- n k))
	(fac k))))

(defn count-lattice [rows, cols]
  (choose (* 2 rows) cols))