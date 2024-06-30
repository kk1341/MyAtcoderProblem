#!/usr/bin/env python3
n = int(input())
figure_list = []
for i in range(1, 2*n+2):
    figure_list.append(i)

turn = 'Takahashi'
for i in range(2*n+1):
    if turn == 'Takahashi':
        print(figure_list[0])
        figure_list.remove(figure_list[0])
        turn = 'Aoki'
    else:
        select_figure = int(input())
        if select_figure not in figure_list:
            exit()
        else:
            figure_list.remove(select_figure)
            turn = 'Takahashi'