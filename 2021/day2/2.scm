(define mfile (open-input-file "/home/leneth/dev/challenges/advent2021/day2/input.txt"))
;
(define (xtimes-y file) 

	(define (count-ufd file x y a)
	  	 
		  

		(define c-line (read-line file))
		(if (eof-object? c-line )
			(* x y)
			(count-ufd file 
				(if (string-prefix? "forward" c-line )(+ (string->number (string-tail c-line 8)) x) x) 
				(if (string-prefix? "forward" c-line )(+ (* a (string->number (string-tail c-line 8))) y) y) 
				(if (string-prefix? "up" c-line )(- a (string->number (string-tail c-line 3))) 
					(if (string-prefix? "down" c-line )(+ (string->number (string-tail c-line 5)) a) a)
				)
			)
			
		)
		
	)
	(count-ufd file 0 0 0)
)
(xtimes-y mfile)
