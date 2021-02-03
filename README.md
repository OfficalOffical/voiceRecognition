# Voice Recognition 

Voice recognition with sciPy

# How to setup

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install sounddevice sciPy
```
# Usage

After compiling program starts to record for 1 second and comparing what you said to word list using peak point.

### findMax( *int) :
Finds max peak point inside the given array and returns it's x and y positions.

### switchToString (int) : 
It just converts index of arrays to strings because we are using jagged array. Used for more readable output.

the words starting with ses (means sound in English) holds array values of sound that given.




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
