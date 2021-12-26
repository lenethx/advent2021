;(use extras)
(define mfile (open-input-file "/home/leneth/dev/challenges/advent2021/day1/1-1-input.txt"))
;
(define (count-inc file) 

	(define (count-iter file prev prev2 prev3) 
		(define c-line (read file))
		(define d-line (if (string? c-line)(string->number c-line) c-line))
		(if (eof-object? c-line )
			0
			(+ (if (> (+ d-line prev prev2) (+ prev prev2 prev3)) 1 0) (count-iter file d-line prev prev2))
		)
		
	)
	(count-iter file (read file) (read file) 150000)
	
)

(count-inc mfile)
