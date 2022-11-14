import panel as pn
import param
pn.extension(sizing_mode="stretch_width")

class Page(pn.viewable.Viewer):
    def view(self):
        raise NotImplementedError()
    
    def __panel__(self):
        return self.view

class Outline(Page):
    def view(self):
        return "Hello"

PAGES = [Outline()]

selector = pn.widgets.RadioButtonGroup(name="Page", value=PAGES[0], options=PAGES)

@pn.depends(selector)
def get_page(func):
    return func()

pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Starter App",
    favicon="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/320297ccb92773da099f6b97d267cc0433b67c23/favicon/ap-1f77b4.ico",
    sidebar=[selector], main=[get_page],
).servable()