# Don't hardcode values in expressions. Store them in variables and use the variables in your code.
from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flatmates_bill import flat

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    # GET method
    def get(self):
        my_bill_form = BillForm()
        return render_template('bill_form_page.html', bill_form=my_bill_form)

    def post(self):
        my_bill_form = BillForm(request.form)
        amount = float(my_bill_form.amount.data)
        period = my_bill_form.period.data

        name1 = my_bill_form.name1.data
        day_in_house1 = float(my_bill_form.days_in_house1.data)

        name2 = my_bill_form.name2.data
        day_in_house2 = float(my_bill_form.days_in_house2.data)

        the_bill = flat.Bill(amount, period)
        flatmate1 = flat.Flatmate(name1, day_in_house1)
        flatmate2 = flat.Flatmate(name2, day_in_house2)

        return render_template("bill_form_page.html", bill_form=my_bill_form, name1=flatmate1.name, name2=flatmate2.name,
                               amount1=round(flatmate1.pays(the_bill, flatmate2),2),
                               amount2=round(flatmate2.pays(the_bill, flatmate1),2),
                               result=True)


# class ResultsPage(MethodView):
    # POST method
    # def post(self):
    #     my_bill_form = BillForm(request.form)
    #     amount = float(my_bill_form.amount.data)
    #     period = my_bill_form.period.data
    #
    #     name1 = my_bill_form.name1.data
    #     day_in_house1 = float(my_bill_form.days_in_house1.data)
    #
    #     name2 = my_bill_form.name2.data
    #     day_in_house2 = float(my_bill_form.days_in_house2.data)
    #
    #     the_bill = flat.Bill(amount, period)
    #     flatmate1 = flat.Flatmate(name1,day_in_house1)
    #     flatmate2 = flat.Flatmate(name2,day_in_house2)
    #
    #     return render_template("results.html", name1=flatmate1.name, name2=flatmate2.name,
    #                            amount1=flatmate1.pays(the_bill, flatmate2),
    #                            amount2=flatmate2.pays(the_bill, flatmate1))


class BillForm(Form):
    amount = StringField("Bill Amount: ", default='100')
    period = StringField("Bill Period: ", default='December 2020')

    name1 = StringField("Name: ", default='John')
    days_in_house1 = StringField("Days in House: ", default='20')

    name2 = StringField("Name: ", default='Mary')
    days_in_house2 = StringField("Days in House: ", default='20')

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
# app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
