;(use-modules (ice-9 rdelim))
(define mfile (open-input-file "/home/leneth/dev/challenges/advent2021/day3/input.txt"))
; 
(define (powcon file)  

	(define (countbin file nlist len)
	  	 
		  

		(define c-line (read-line file))
		(if (or (eof-object? c-line) #f )
			(list len  nlist)
			(countbin file (map + nlist (map char->digit (string->list c-line)) ) (+ len 1))
			;(map + nlist (map char->digit (string->list c-line)) )
			
		)
		
	)
;(countbin file (list 0 0 0 0 0 0 0 0 0 0 0 0) 0)
	(define flist (countbin file (list 0 0 0 0 0 0 0 0 0 0 0 0) 0) )
	;(car (cdr flist))
;(string->number(string-append "#b" (list->string (map digit->char (map (lambda (x) (if (> (/ (car flist) 2 ) x) 0 1) ) (car (cdr flist)))))))
		(* (string->number(string-append "#b" (list->string (map digit->char (map (lambda (x) (if (> (/ (car flist) 2 ) x) 0 1) ) (car (cdr flist))))))) 
	   (string->number(string-append "#b" (list->string (map digit->char (map (lambda (x) (if (> (/ (car flist) 2 ) x) 1 0) ) (car (cdr flist))))))))
)
(powcon mfile)
