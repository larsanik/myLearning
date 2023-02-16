def init():
    """ Init list cells """
    height = 100
    width = 100

    grid_model = [0] * height

    for i in range(height):
        grid_model[i] = [0] * width
    # test out
    # print(grid_model)
    return grid_model


def next_gen():
    """Calc next generation"""
    global gird_model

    for i in range(0, height):
        for j in range(0, widht):
            cell = 0
            if gird_model [i][j] == 0:
                count = count_neighbors(gird_model, i, j)



def count_neighbors(grid, row, col):
   """Calc lives neighbors"""
   count = 0
   if row-1 >= 0:
        count = count + grid[row-1][col]
   if (row-1 >= 0) and (col-1 >= 0):
       count = count + grid[row-1][col-1]
   if (row-1 >= 0) and (col+1 < width):
       count = count + grid[row-1][col+1]
   if col-1 >= 0:
       count = count + grid[row][col-1]
   if col + 1 < width:
       count = count + grid[row][col+1]
   if row + 1 < height:
       count = count + grid[row+1][col]
   if (row + 1 < height) and (col-1 >= 0):
       count = count + grid[row+1][col-1]
   if (row + 1 < height) and (col+1 < width):
       count = count + grid[row+1][col+1]
   return count


def main():
    gird_model = init()


if __name__ == '__main__':
    main()




