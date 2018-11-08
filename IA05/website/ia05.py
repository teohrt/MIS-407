from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("savings-form.html")

@app.route('/compute', methods=['POST'])
def compute():
    # For a POST request, request.form is a dictionary that contains the posted
    # form data. It should have values for 'rate', 'years', initial_balance,
    # and monthly_deposit.
    # Compute the monthly interest rate and number of months, and
    # use those values to compute the savings table
    # as a list where each row in the savings_table list has a dictionary:
    # {'month': month, 'deposit': deposit, 'interest': interest, 'balance': balance}
    # and provide that list to the template's savings_report.
    rate = float(request.form['rate'])
    years = int(request.form['years'])
    balance = float(request.form['initial_balance'])
    monthly_deposit = float(request.form['monthly_deposit'])
    savings_table = []

    numberOfMonths = years * 12
    monthly_rate = rate / 12
    for month in range(1, numberOfMonths+1, 1):
        interest = (balance * monthly_rate)
        balance = balance + interest + monthly_deposit

        row = {'month': month, 'deposit': monthly_deposit, 'interest': interest, 'balance': balance}
        savings_table.append(row)

    return render_template("savings-table.html", rate=rate, years=years,
                           monthly_deposit=monthly_deposit,
                           final_balance=balance,
                           savings_table=savings_table)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
