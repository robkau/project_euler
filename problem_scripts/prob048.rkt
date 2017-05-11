; Problem 48:
; The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
; Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
; https://projecteuler.net/problem=48

; Solved with a recursive algorithm that crawls over each term in the series and sums the values

#lang racket

(define (sum-series end sum n)
  (cond
    ; Base case. Return the sum with the final number added.
    [(equal? n end) (+ sum (expt n n))]
    ; Otherwise add this number to the sum and go to the next one
    [else (sum-series end (+ sum (expt n n)) (+ n 1))]
  )
)

; Verify the sample value matches
(sum-series 10 0 1) ; equals 10405071317

; Calculate the answer
(modulo (sum-series 1000 0 1) 10000000000)  ;  equals 9110846700

; Congratulations, the answer you gave to problem 48 is correct.
; You are the 86726th person to have solved this problem.