# This script will generate a two column data file comprise of 1 through 10 in one column, and twice that in another column

# Let's create a header
echo 'xaxis yaxis' > data/linear_data.dat

# Let's perform a for loop in order to create the columns
for xdat in {1..10};
do
    echo $xdat $((xdat*2)) >> data/linear_data.dat
done

echo blah blah
