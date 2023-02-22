is_starting_block_for_player = {0: True, 1: True, 2: True, 3: True}


def placement_is_valid(state, proposed_coordinates, player):
    global is_starting_block_for_player, isvalid
    isvalid = False
    all_immediate_neighbours = []
    if is_starting_block_for_player[player]:
        # check if a player is on the square
        for coord in proposed_coordinates:
            if not __square_is_within_gameboard(state, coord) or not __square_has_player(state, coord, None):
                return False
        for i in range(len(proposed_coordinates)):
            for j in range(len(proposed_coordinates)):
                x = proposed_coordinates[j][1]
                y = proposed_coordinates[j][0]
                if x < 0 or y < 0:
                    return False
                if (x == 0 and y == 0) or (y == 19 and x == 19) or (y == 0 and x == 19) or (y == 19 and x == 0):
                    isvalid = True
            if isvalid:
                is_starting_block_for_player[player] = False
                return True
            else:
                return False
    else:
        for coord in proposed_coordinates:
            if not __square_is_within_gameboard(state, coord) or not __square_has_player(state, coord, None):
                return False
            for immediate_neighbour in __get_immediate_neighbours(coord):
                if __square_is_within_gameboard(state, immediate_neighbour) and not immediate_neighbour in proposed_coordinates:
                    if __square_has_player(state, immediate_neighbour, player):
                        return False
                    all_immediate_neighbours.append(immediate_neighbour)
        if not is_starting_block_for_player[player] and not __is_block_connected(state, proposed_coordinates, player, all_immediate_neighbours):
            return False
        return True


def __is_block_connected(state, proposed_coordinates, player, all_immediate_neighbours):
    for coord in proposed_coordinates:
        for diagonal_neighbour in __get_diagonal_neighbours(coord):
            if __square_is_within_gameboard(state, diagonal_neighbour) and not diagonal_neighbour in proposed_coordinates and not diagonal_neighbour in all_immediate_neighbours:
                if __square_has_player(state, diagonal_neighbour, player):
                    return True
    return False


def __get_immediate_neighbours(square):
    return [[square[0]-1, square[1]],
            [square[0]+1, square[1]],
            [square[0], square[1]-1],
            [square[0], square[1]+1]]


def __get_diagonal_neighbours(square):
    return [[square[0]+1, square[1]+1],
            [square[0]+1, square[1]-1],
            [square[0]-1, square[1]+1],
            [square[0]-1, square[1]-1]]


def __square_is_within_gameboard(state, square):
    return not (square[0] < 0 or square[1] < 0 or square[0] > len(state) - 1 or square[1] > len(state) - 1)


def __square_has_player(state, square, expected_player):
    return state[square[0]][square[1]] == expected_player