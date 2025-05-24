# bookbot

BookBot is my first Boot.dev project!  It’s a Python command-line application that analyzes text files (books) by counting total words and calculating the frequency of each character, then printing a formatted console report.

## Features

* Reads any `.txt` file and processes its content
* Counts total number of words
* Calculates character frequency (case-insensitive)
* Prints a clear, comprehensive report to the console

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/LyricalEcho/bookbot.git
   cd bookbot
   ```
2. Ensure you have Python 3.x installed:

   ```bash
   python3 --version
   ```

## Usage

Run the CLI tool with the path to your text file:

```bash
python3 main.py path/to/book.txt
```

Example:

```bash
python3 main.py books/frankenstein.txt
```

## Project Structure

```
bookbot/
├── .gitignore       # Files and directories ignored by Git
├── main.py          # Entry point for the book analysis CLI
├── stats.py         # Helper functions for counting words and characters
└── README.md        # Project documentation
```

## Example Output

```text
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

Character frequencies:
- 'e': 46043
- 't': 30365
- 'a': 26743
  ...
--- End report ---
```

## Contributing

Contributions are welcome!  Feel free to open issues or submit pull requests for enhancements or bug fixes.

## License

This project is for educational purposes and follows open-source guidelines.
