##finance dashboard issue :]
from flask import Flask, render_template_string

app = Flask(__name__)

# Sample expense data
expenses = [
    {"category": "Food", "amount": 120},
    {"category": "Rent", "amount": 800},
    {"category": "Transport", "amount": 60},
]

@app.route("/")
def dashboard():
    total = sum(e["amount"] for e in expenses)
    categories = ", ".join(e["category"] for e in expenses)
    return render_template_string("""
        <h1>Finance Dashboard</h1>
        <p><b>Total Spending:</b> ${{ total }}</p>
        <p><b>Categories:</b> {{ categories }}</p>
    """, total=total, categories=categories)

if __name__ == "__main__":
    app.run(debug=True)
