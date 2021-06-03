# ToTheMoon

# Plan...
1. Fetch data points using python script and Bybit.com api
2. Output correctly formatted data to data.m (we want sets of 40 klines (each kline has 6 attributes), the y label will be the last klines close / open ratio?)
3. Use octave NN backprop to learn params (where it'll take first 39 klines and last kline's open price to determine y = )

- we want y to be a classification problem between buy and sell.
- so some decimal between 0 and 1
we will label each dataset's y as some float between 0 and 1
to determine y for each set. we will look at close / open ratio in relationship to max close / open ratio of entire set??

does nn need to know the scale of the buy? or just needs to differentiate between buy and sell binarily?
i think for now we can just do binary
label each set as buy or sell.

architecture 240 300 300 1

lets do 80 20 split training / test
nn

# TODOS
* re-organize util functions using oop? nah.
* use octave scripts to learn params
