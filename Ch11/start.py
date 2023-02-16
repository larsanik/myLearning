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
        for j in range(0, widht)


def main():
    gird_model = init()


if __name__ == '__main__':
    main()




