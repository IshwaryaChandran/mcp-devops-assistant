from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

def run_command(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    if "pods" in user_input:
        result = run_command("kubectl get pods -A")
    elif "nodes" in user_input:
        result = run_command("kubectl get nodes")
    elif "deployments" in user_input:
        result = run_command("kubectl get deployments -A")
    elif "logs" in user_input:
        result = "Feature coming soon"
    else:
        result = "I don't understand yet"

    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)