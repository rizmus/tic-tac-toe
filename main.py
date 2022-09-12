from tic_tac_toe import tic_tac_toe

sel_ans = input('Если вы хотите играть вдвоем, введите T: ')

if sel_ans == 'T' or sel_ans == 't':
    tic_tac_toe.main('--mode t')
else:
    tic_tac_toe.main("--mode s")