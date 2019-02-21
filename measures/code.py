
# code for subsetting the rows in trials.csv
$range(((int(expInfo['participant'])-1)*430+1), ((int(expInfo['participant'])-1)*430+87), 1)

$range(((int(expInfo['participant'])-1)*430+87), ((int(expInfo['participant'])-1)*430+173), 1)

$range(((int(expInfo['participant'])-1)*430+173), ((int(expInfo['participant'])-1)*430+259), 1)

$range(((int(expInfo['participant'])-1)*430+259), ((int(expInfo['participant'])-1)*430+345), 1)

$range(((int(expInfo['participant'])-1)*430+345), ((int(expInfo['participant'])-1)*430+431), 1)



# shortened for testing
range(((1-1)*430+1), ((1-1)*430+87), 1)
