(define mfile (open-input-file "/home/leneth/dev/challenges/advent2021/day3/input.txt"))
; 
(define (powcon file)  

	(define (bitrule file total len bit incl excl rule)
	  	 
		  

		(define c-line (read-line file))
		(if (or (eof-object? c-line) #f )
		  	(if (= len 1) 
			  	RETURN_LAST
				(countbin file 0 0 (+ bit 1) (if (rule total (/ len 2)) 
													(cons*  incl)
												 )
				)
			)
			(countbin file (map + nlist (map char->digit (string->list c-line)) ) (+ len 1))
			;(map + nlist (map char->digit (string->list c-line)) )
			
		)
		
	)
	(define flist (countbin file (list 0 0 0 0 0 0 0 0 0 0 0 0) 0) )
		(* (string->number(string-append "#b" (list->string (map digit->char (map (lambda (x) (if (> (/ (car flist) 2 ) x) 0 1) ) (car (cdr flist))))))) 
	   (string->number(string-append "#b" (list->string (map digit->char (map (lambda (x) (if (> (/ (car flist) 2 ) x) 1 0) ) (car (cdr flist))))))))
)
(powcon mfile)
