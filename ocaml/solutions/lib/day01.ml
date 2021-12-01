open Core;;

let data file = In_channel.read_lines file;;

let rec parse data = match data with
| [] -> []
| h :: t -> (int_of_string h) :: (parse t);;

let data = parse (data "../../inputs/day01.txt");;

let rec solve_a data = match data with
| [] -> 0
| _ :: [] -> 0
| prev :: curr :: tail -> if curr > prev then 1 + (solve_a (curr :: tail)) else (solve_a (curr :: tail));;

let rec solve_b data = match data with
| [] -> 0
| _ :: [] -> 0
| _ :: _ :: [] -> 0
| _ :: _ :: _ :: [] -> 0
| a :: b :: c :: d :: t -> if  d > a then 1 + (solve_b (b :: c :: d :: t)) else (solve_b (b :: c :: d :: t));;