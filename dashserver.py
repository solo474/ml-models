import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H3(children='Points'),

    html.Div(children='''
        Tree
    ''')
])

if __name__ == '__main__':
    app.run_server(port=8081,host="0.0.0.0",debug=True)
