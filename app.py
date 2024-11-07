from flask import Flask, request, jsonify
import subprocess
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/download" method="post">
            <input type="text" name="link" placeholder="Enter video link here">
            <button type="submit">Download Subtitles</button>
        </form>
    '''

@app.route('/download', methods=['POST'])
def download():
    link = request.form['link']
    if not link:
        return jsonify({"error": "No link provided"}), 400

    try:
        result = subprocess.run(
            ["isubrip", link], 
            capture_output=True, 
            text=True
        )

        if result.returncode == 0:
            return jsonify({"message": "Subtitles downloaded successfully"})
        else:
            return jsonify({"error": result.stderr}), 500

    except Exception as e:
        print("Error:", e)
        print(traceback.format_exc())
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
