def my_function(billamount,tippercentage):
    total=billamount*(1+0.01*tippercentage)
    total=round(total,2)
    print(total)
my_function(400,76)