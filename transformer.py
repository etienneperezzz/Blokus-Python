from block import Block


def rotate_90(selected_block, selected_segment):
    offset = selected_block.coordinates[selected_segment]
    new_coords = []
    for coord in selected_block.coordinates:
        new_coords.append([-(coord[1] - offset[1]), coord[0] - offset[0]])
    return Block(selected_block.index, selected_block.position, new_coords)


def flip(selected_block, selected_segment):
    offset = selected_block.coordinates[selected_segment]
    print(offset)
    new_coords = []
    for coord in selected_block.coordinates:
        new_coords.append([coord[0] - offset[0], -(coord[1] - offset[1])])
    return Block(selected_block.index, selected_block.position, new_coords)
