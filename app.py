from flask import Flask, render_template, request
import model   # model.py must exist

app = Flask(__name__)

valid_userid = [
    '00sab00','1234','zippy','zburt5','joshua','dorothy w',
    'rebecca','walker557','samantha','raeanne','kimmie',
    'cassie','moore222'
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend_top5():
    user_name = request.form.get("User Name")

    if not user_name:
        return render_template("index.html", text="Please enter a user name")

    if user_name not in valid_userid:
        return render_template(
            "index.html",
            text="No Recommendation found for the user"
        )

    # Get recommendations
    top20_products = model.recommend_products(user_name)
    top5_products = model.top5_products(top20_products)

    return render_template(
        "index.html",
        column_names=top5_products.columns.values,
        row_data=top5_products.values.tolist(),
        zip=zip,
        text="Recommended products"
    )

if __name__ == "__main__":
    app.run(debug=False)
