open Core;;

let data file = In_channel.read_lines file;;

let rec parse data =
match data with
| [] -> []
| h :: t -> match (String.get h 0) with
           | 'u' -> (-((int_of_char (String.get h ((String.length h) - 1))) - 48), 0) :: parse t
           | 'd' -> ((int_of_char (String.get h ((String.length h) - 1)) - 48), 0) :: parse t
           | 'f' -> (0, (int_of_char (String.get h ((String.length h) - 1))) - 48) :: parse t
           | _ -> [];;

let data = parse (data "../../inputs/day02.txt");;

let rec solve_a_aux data vert horiz =
match data with
| [] -> vert * horiz
| (v, h) :: t -> solve_a_aux t (vert + v) (horiz + h)

let solve_a data = solve_a_aux data 0 0;;

let rec solve_b_aux data aim vert horiz =
match data with
| [] -> vert * horiz
| (v, h) :: t -> solve_b_aux t (aim + v) (vert + (aim * h)) (horiz + h);;

let solve_b data = solve_b_aux data 0 0 0;;