from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, key, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65) if decrypt else chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97) if decrypt else chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result_message = None  # Initialize result_message

    if request.method == 'POST':
        key = int(request.form['key'])
        operation = request.form['operation']
        text = request.form['text']

        try:
            if operation == 'encrypt':
                result = caesar_cipher(text, key)
                result_message = "Text encrypted successfully"
            elif operation == 'decrypt':
                result = caesar_cipher(text, key, decrypt=True)
                result_message = "Text decrypted successfully"
            else:
                return render_template('index.html', error="Invalid operation. Please choose encrypt or decrypt.")

        except Exception as e:
            return render_template('index.html', error=f"An error occurred: {str(e)}")

    return render_template('index.html', result_message=result_message)

if __name__ == '__main__':
    app.run(debug=True)
