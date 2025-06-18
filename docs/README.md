# Documentation Build Instructions

This guide describes how to build the documentation from sources.

## 1. Install dependencies

Make sure you have Python installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

## 2. Build the documentation

To generate the HTML documentation, run the following command from the `docs` directory:

- **On Linux/macOS:**
  ```bash
  make html
  ```
- **On Windows:**
  ```cmd
  .\make.bat html
  ```

The generated documentation will be available in the `_build/html` folder.

## 3. Open the documentation

Open the `index.html` file in the `_build/html` directory with your web browser.
