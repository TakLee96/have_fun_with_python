(define (factorial x)
    (if (<= x 1) 1
        (* x (factorial (- x 1)))
    )
)

(define (fib x)
    (if (<= x 1) x
        (+ (fib (- x 1)) (fib (- x 2)))
    )
)

(define (map fn lst)
    (if (null? lst) nil
        (cons (fn (car lst)) (map fn (cdr lst)))
    )
)

(define (reduce fn s lst)
    (if (null? lst) s
        (fn (car lst) (reduce fn s (cdr lst)))
    )
)

(define (make-btree entry left right) (
    cons entry (cons left right)
))

(define (entry tree)
    (car tree)
)

(define (left tree)
    (cons (cdr tree))
)

(define (right tree)
    (cdr (cdr tree))
)

(define (btree-sum tree)
    (if (null? tree) 0
        (+ (+ (btree-sum (left tree)) (btree-sum (right tree))) (entry tree))
    )
)
