;(use extras)
(define mfile (open-input-file "/home/leneth/dev/challenges/advent2021/day1/1-1-input.txt"))
;
(define (count-inc file) 

	(define (count-iter file prev) 
		(let ((c-line (read file)))  
		(if (eof-object? c-line )
			0
			(+ (if (> (if (string? c-line)(string->number c-line) c-line) prev) 1 0) (count-iter file c-line))
		)
		)
	)
	(count-iter file 5000)
	
)

(count-inc mfile)
#| 
(define (count-inc file) 
	
	(count-iter file 5000)
	)


(define (count-iter file prev) 
	(let ((c-line (read file)))  
  	(print "line")
	  (if (eof-object? c-line )
		0
		(+ (if (> c-line prev) 1 0) (count-iter file c-line))
	)
	)	
)


(define l "/home/leneth/dev/challenges/advent2021/1-1-input.txt")
(let ((p (open-input-file l)))
	(print (count-inc p))
)
;|#
