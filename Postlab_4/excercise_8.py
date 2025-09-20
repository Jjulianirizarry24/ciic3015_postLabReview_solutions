def is_right_triangle(side_a, side_b, side_c):
    hipo= max(side_a, side_b, side_c)
    if(side_a==hipo):
        return side_a*side_a==side_b*side_b+side_c*side_c
    elif (side_b==hipo):
        return side_b*side_b==side_a*side_a+side_c*side_c
    else:
        return side_c*side_c==side_a*side_a+side_b*side_b