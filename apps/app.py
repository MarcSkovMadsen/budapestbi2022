import panel as pn
import param

ACCENT = "#4f81bd"

CSS = """
fast-card.pn-wrapper {
    height: calc( 100vh - 150px );
    --type-ramp-base-font-size: 24px;
    --type-ramp-base-line-height: 30px;
}
"""
pn.config.raw_css.append(CSS)
pn.extension("ace", sizing_mode="stretch_width")

class Page(pn.viewable.Viewer):
    def __init__(self, **params):
        super().__init__(**params)

        self._view = self.create_view()

    def create_view(self):
        raise NotImplementedError()
    
    def __panel__(self):
        return self._view

class Introduction(Page):
    def create_view(self):
        return """
# Python Data Apps – Running in the browser

Data app frameworks enables you to explore your data and models interactively and share them with
the world. It’s a super power for you and your team.

In this talk I will introduce you to [Panel](https://panel.holoviz.org) data apps and show you why it’s a good choice for your next data
app in Python. I will also demonstrate how easy it is, to **share your data app with the world**.
NO SERVER REQUIRED.

# Marc Skov Madsen, PhD, CFA®

I'm a domain expert in data, models and analytics. I've been working with asset management of
financial and physical assets for +15 years in the financial and energy sectors. I've worked within
analysis, modelling, innovation, business development, trading, operation, finance and risk
management.

[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/%C3%98rsted_logo.svg/800px-%C3%98rsted_logo.svg.png" style="height:50px">](https://orsted.com/)
"""

class IntroductionToPython(Page):
    def create_view(self):
        tiobe = """
[<img src="https://raw.githubusercontent.com/MarcSkovMadsen/budapestbi2022/main/apps/tiobe.jpg">](https://www.tiobe.com/tiobe-index/)

The [TIOBE Index](https://www.tiobe.com/tiobe-index/) is an indicator of the popularity of programming languages.
"""
        pypi = """
[<img src="https://raw.githubusercontent.com/MarcSkovMadsen/budapestbi2022/main/apps/pypi-stats.jpg">](https://pypi.org)
"""

        example = """\
import panel as pn

pn.extension()

def sum(a,b):
    "Returns the sum of a and b"
    return a+b

a = pn.widgets.IntSlider(start=0, end=10, name="a")
b = pn.widgets.IntSlider(start=0, end=10, name="b")

pn.Column(
    a, b, pn.bind(sum,a,b)
)
"""
        
        def sum(a,b):
            "Returns the sum of a and b"
            return a+b

        a = pn.widgets.IntSlider(start=0, end=10, name="a")
        b = pn.widgets.IntSlider(start=0, end=10, name="b")

        output = pn.Column(
            a, b, pn.bind(sum,a,b), sizing_mode="fixed", width=300, margin=(10,25)
        )
        
        code = pn.Row(
            pn.widgets.Ace(value=example, height=550, sizing_mode="stretch_both", language="python"),
            output,  
        )

        return pn.Column(
            "# Python is the worlds most popular programming language",
            pn.Tabs(
            ("📈",tiobe),
            ("📦",pypi),
            ("📄", code), margin=(0, 25), sizing_mode="stretch_both",
        ), sizing_mode="stretch_both")

class IntroductionToPythonDataViz(Page):
    def create_view(self):
        return "Introduction to Pythons Data Viz"

class DataAppsIsASuperPowerForYou(Page):
    def create_view(self):
        return "Data Apps is a super power for you"

class PanelIsAwesome(Page):
    def create_view(self):
        return "Panel is an awesome data app framework"

class PythonInTheBrowser(Page):
    def create_view(self):
        return "Python in the browser will help democratize data and viz"

class PanelConvert(Page):
    def create_view(self):
        return "`panel convert` makes it much easier"

class PanelSharing(Page):
    def create_view(self):
        return "Panel Sharing creates a community"


PAGES = [
    Introduction(name="Introduction 👈"),
    IntroductionToPython(name="Python is VERY POPULAR 🔥"),
    IntroductionToPythonDataViz(name="Python is a super power for data viz 💪"),
    DataAppsIsASuperPowerForYou(name="Data Apps is a SUPER POWER for you 🦸"),
    PanelIsAwesome(name="Panel is an AWESOME data app framework 👌"),
    PythonInTheBrowser(name="Python gives new possibilities ✨"),
    PanelConvert(name="Panel convert makes it much easier ⭐"),
    PanelSharing(name="Panel Sharing for SHARING DATA APPS 🌎")
]
PAGE_MAP = {page.name: page for page in PAGES}

page_selector = pn.widgets.RadioButtonGroup(name="Page", options=list(PAGE_MAP.keys()), orientation="vertical", button_type="success")

@pn.depends(page_selector)
def page_view(page):
    return PAGE_MAP[page]

if pn.state.location:
    pn.state.location.sync(page_selector, {'value': 'page'})

pn.template.FastListTemplate(
    site="BudapestBI 2022",
    title="Python Data Apps – Running in the browser",
    favicon="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/320297ccb92773da099f6b97d267cc0433b67c23/favicon/ap-1f77b4.ico",
    sidebar=[page_selector], main=[page_view],
    theme_toggle=False, accent=ACCENT
).servable()