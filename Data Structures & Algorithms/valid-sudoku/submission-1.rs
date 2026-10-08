use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut rows: Vec<HashSet<char>> = vec![HashSet::new(); 9];
        let mut cols: Vec<HashSet<char>> = vec![HashSet::new(); 9];
        let mut subbox: Vec<HashSet<char>> = vec![HashSet::new(); 9];
    
        for i in 0..9 {
            for j in 0..9 {
                let c = board[i][j];

                let idx = (i / 3) * 3 + j / 3;
                if c == '.' { continue; }
                if rows[i].contains(&c) || cols[j].contains(&c) || subbox[idx].contains(&c) {
                    println!("{},{}", i, j);
                    return false;
                }

                rows[i].insert(c);
                cols[j].insert(c);
                subbox[idx].insert(c);
            }
        }

        true
    }

    
}

pub fn subbox_index(i: usize, j: usize) -> usize {
    if i < 3 {
        if j < 3 {
            1
        } else if j >= 3 && j < 6 {
            2
        } else {
            3
        }
    } else if i >= 3 && i < 6  {
        if j < 3 {
            4
        } else if j >= 3 && j < 6 {
            5
        } else {
            6
        }
    } else {
        if j < 3 {
            7
        } else if j >= 3 && j < 6 {
            8
        } else {
            9
        }
    }
}