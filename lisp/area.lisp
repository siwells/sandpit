; the function AreaOfCircle
; calculates the area of a circle
; where the radius of said circle
; comes from user input

(defun AreaOfCircle()
    (terpri)
    (princ "Enter Radius: ")
    (setq radius (read))
    (setq area (* 3.1416 radius radius))
    (princ "Area: ")
    (write area)
)
(AreaOfCircle)
