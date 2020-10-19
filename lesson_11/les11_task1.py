def count_pts(win, draw, loss):
    return win * 3 + draw * 1 + loss * 0


print(f'Team score is: {count_pts(7, 3, 0)}')
