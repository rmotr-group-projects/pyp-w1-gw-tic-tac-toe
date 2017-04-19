valid_positions = [
    (0,0), (0,1), (0,2),
    (1,0), (1,1), (1,2),
    (2,0), (2,1), (2,2),
]

invalid_positions = [
    (2,3), (3,2), (3,3), (9,9), (-1,-1), 1, "something", False, (0,0,0)
]

boards ={
        "winner-x": [[
                ["X", "O", "O"],
                ["O", "X", "X"],
                ["O", "O", "X"],
            ],
            [
                ["O", "O", "X"],
                ["O", "X", "X"],
                ["X", "O", "O"],
            ],
            [
                ["X", "X", "X"],
                ["X", "O", "O"],
                ["O", "O", "X"],
            ],
            [
                ["X", "O", "O"],
                ["X", "X", "X"],
                ["O", "O", "X"],
            ],
            [
                ["X", "O", "O"],
                ["O", "O", "X"],
                ["X", "X", "X"],
            ],
            [
                ["X", "O", "X"],
                ["O", "O", "X"],
                ["O", "X", "X"],
            ],
            [
                ["X", "X", "O"],
                ["O", "X", "O"],
                ["O", "X", "X"],
            ],
            [
                ["X", "X", "O"],
                ["X", "O", "O"],
                ["X", "O", "X"],
            ]],
        "winner-o":[[
            ["O", "X", "X"],
            ["X", "O", "O"],
            ["X", "X", "O"],
        ],
        [
            ["X", "X", "O"],
            ["X", "O", "O"],
            ["O", "X", "X"],
        ],
        [
            ["O", "O", "O"],
            ["O", "X", "X"],
            ["X", "X", "O"],
        ],
        [
            ["O", "X", "X"],
            ["O", "O", "O"],
            ["X", "X", "O"],
        ],
        [
            ["O", "X", "X"],
            ["X", "X", "O"],
            ["O", "O", "O"],
        ],
        [
            ["O", "X", "O"],
            ["X", "X", "O"],
            ["X", "O", "O"],
        ],
        [
            ["O", "O", "X"],
            ["X", "O", "X"],
            ["X", "O", "O"],
        ],
        [
            ["O", "O", "X"],
            ["O", "X", "X"],
            ["O", "X", "O"],
        ]],
        "incomplete-board": [
            ["X", "O", "O"],
            ["O", "-", "-"],
            ["O", "X", "O"],
        ],
        "no-winner": [
            ["X", "O", "O"],
            ["O", "X", "X"],
            ["O", "X", "O"],
        ],
}   