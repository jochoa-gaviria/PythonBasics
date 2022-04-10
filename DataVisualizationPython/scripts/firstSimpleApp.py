import justpy as jp


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course reviews", classes="text-h3 text-center q-pa-md") ## Use Quasar styling
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analys")
    return wp

jp.justpy(app)