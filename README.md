# Password_Generator

This script generates a random password ranging from length 8 to 50 inclusive

## Installation

**Using git**

```bash
git clone 
cd 
```

## Parameters

`pass_length` Required. Length of the password, from 8 to 50 inclusive

## Usage

```bash
python script.py PASS_LENGTH
```

## Note

* `pass_length` cannot go below 8 and cannot go above 50
* The script guarentees no consecutive values, such as `ABC`, `123`, `abc`
* The script guarentees at least 1 number, symbol, uppcase letter and lowercase letter.
* The script guarantees that no character is repeated three times.

## License

This repository is licensed under the [Unlicense](LICENSE)
