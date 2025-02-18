import dash_labs as dl
import dash_html_components as html
import dash

app = dash.Dash(__name__, plugins=[dl.plugins.FlexibleCallbacks()])
tpl = dl.templates.DbcCard(title="Simple App", columns=6)


@app.callback(
    dl.Input(html.Button(children="Click Me"), "n_clicks", label="Button to click"),
    template=tpl,
)
def callback(n_clicks):
    return "Clicked {} times".format(n_clicks)


app.layout = tpl.layout(app)

if __name__ == "__main__":
    app.run_server(debug=True)
