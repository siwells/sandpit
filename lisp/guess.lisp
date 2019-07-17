; open clisp in the same folder as this file then do (load "guess.lisp") before calling (start-over)

(defparameter *small* 1)
(defparameter *big* 100)
(defun guess-my-number () 
    (ash (+ *small* *big*) -1))
(defun smaller () 
    (setf *big* (1- (guess-my-number))) 
    (guess-my-number))
(defun bigger () 
    (setf *small* (1+ (guess-my-number))) 
    (guess-my-number))
(defun start-over () 
    (defparameter *small* 1) 
    (defparameter *big* 100) 
    (princ "Think of a number & I'll guess it") 
    (guess-my-number))
(defun yes () 
    (write-line "Yay!!!") 
    (start-over))
