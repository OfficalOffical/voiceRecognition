# Voice Recognition 

The program turns voice to text With Scipy. The computer makes guess what you are saying with more training it will give more accurate results. 

# How to setup

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install sounddevice sciPy
```

After installing sciPy library compile the python and it's ready to go.
# Usage

After compiling program starts to record for 1 second and comparing what you said to the word list using peak point.

### findMax( *int) :
Finds max peak point inside the given array and returns its x and y positions.

### switchToString (int) : 
It just converts the index of arrays to strings because we are using a jagged array. Used for more readable output.

the words starting with ses (means sound in English) holds array values of sound that given.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
