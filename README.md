# Chemical Properties

Python module for getting simple chemical properties of any element.

## Features
- Atomic Number.
- Number of electrons/protons/neutrons.
- Electron Configuration.
- Name/Symbol.

## Usage
```py
from elements import Element # Import Module.

el = Element('carbon') # or Element(6).

print(el.electron_configuration) # Print the electron configuration of the element.
```
### Output
```
['1s2', '2s2', '2p2']
```
## License
Licensed under the [MIT License](LICENSE).