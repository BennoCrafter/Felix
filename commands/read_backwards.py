def read_backwards():
    usr_inp = input(">>What should i read backwards?:  ")
    print(usr_inp[::-1])
    ### OLD ###
    # usr_inp_backwards = ""
    # len_usr_inp = len(usr_inp)
    #
    # for i in range(1, len_usr_inp+1):
    #     usr_inp_backwards = usr_inp_backwards + usr_inp[len_usr_inp-i]
    # print(usr_inp_backwards)
