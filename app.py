from flask import Flask, render_template, request

app = Flask(__name__)

# Caesar Cipher Logic
def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift if mode == 'E' else -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        mode = request.form.get("mode")
        text = request.form.get("text")
        shift = request.form.get("shift", "0")

        try:
            shift = int(shift)
        except ValueError:
            shift = 0  # Default to 0 if shift is not a valid integer

        if mode in ['E', 'e', 'D', 'd']:  # Case-insensitive check
            result = caesar_cipher(text, shift, mode.upper())  # Always use upper for consistency

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
