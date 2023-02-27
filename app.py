from flask import Flask
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Grocery</title>

        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th, td {
                padding: 5px;
                text-align: left;
            }
        </style>
    </head>
    <body>

        <h1>My Grocery List</h1>
        
        <table>
            <tr>
                <th>Name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>Type</th>
            </tr>
    '''
    for grocery in db.all():
        html += f'''
        <tr>
            <td>{grocery["name"]}</td>
            <td>{grocery["quantity"]}</td>
            <td>{grocery["price"]}$</td>
            <td>{grocery["type"]}</td>
        </tr>
        
    '''
    html += '''
    </table>
    
    </body>
    </html>

    '''
    return html


# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    pass


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    html = '''<html>
    <head>
        <title>Grocery</title>

        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th, td {
                padding: 5px;
                text-align: left;
            }
        </style>
    </head>
    <body>

        <h1>My Grocery List</h1>

        <table>
            <tr>
                <th>Name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>Type</th>
            </tr>

    '''
    for grocery in db.get_by_type(type):
        html += f'''
        <tr>
            <td>{grocery["name"]}</td>
            <td>{grocery["quantity"]}</td>
            <td>{grocery["price"]}$</td>
            <td>{grocery['type']}</td>
        </tr>
        
    '''
    html += '''
    </table>
    
    </body>
    </html>

    '''
    return html

# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    html = '''<html>
    <head>
        <title>Grocery</title>

        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th, td {
                padding: 5px;
                text-align: left;
            }
        </style>
    </head>
    <body>

        <h1>My Grocery List</h1>

        <table>
            <tr>
                <th>Name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>Type</th>
            </tr>

    '''
    for grocery in db.get_by_name(name):
        html += f'''
        <tr>
            <td>{grocery["name"]}</td>
            <td>{grocery["quantity"]}</td>
            <td>{grocery["price"]}$</td>
            <td>{grocery['type']}</td>
        </tr>
        
    '''
    html += '''
    </table>
    
    </body>
    </html>

    '''
    return html


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    html = '''<html>
    <head>
        <title>Grocery</title>

        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th, td {
                padding: 5px;
                text-align: left;
            }
        </style>
    </head>
    <body>

        <h1>My Grocery List</h1>

        <table>
            <tr>
                <th>Name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>Type</th>
            </tr>

    '''
    for grocery in db.get_by_price(price):
        html += f'''
        <tr>
            <td>{grocery["name"]}</td>
            <td>{grocery["quantity"]}</td>
            <td>{grocery["price"]}$</td>
            <td>{grocery['type']}</td>
        </tr>
        
    '''
    html += '''
    </table>
    
    </body>
    </html>

    '''
    return html



if __name__ == '__main__':
    app.run(debug=True)