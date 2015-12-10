from textparser.textutil.structures import *

class HTMLGenerator(object):
    header = """
    <head>
        <meta charset="utf-8">
        <title>AVAMD</title>

        <link rel="stylesheet" href="skeleton.css" media="screen" title="no title" charset="utf-8">
        <link rel="stylesheet" href="style.css" media="screen" title="no title" charset="utf-8">
    </head>
"""

    body = """<div class="container">
            <div class="row">
                <div class="column xs-seven">
                    {text}
                </div>
                <div class="column xs-one feature-1">
                    {feature1}
                </div>
                <div class="column xs-one feature-2">
                    {feature2}
                </div>
                <div class="column xs-one feature-3">
                    {feature3}
                </div>
                <div class="column xs-one feature-4">
                    {feature4}
                </div>
                <div class="column xs-one feature-5">
                    {feature5}
                </div>
            </div>
        </div>"""

    def __init__(self):
        self.sample_data = {
            "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "feature1": 1,
            "feature2": 0.8,
            "feature3": 0.6,
            "feature4": 0.4,
            "feature5": 0.5
        }

        self.body_filled = """<body>""" + self.fill_template(self.body, self.sample_data) + """</body>"""
        self.full = """<html>""" + self.header + self.body_filled + """</html>"""

        with open("generated_html/index.html", "w") as file:
            file.write(self.full)


    def fill_template(self, template, data):
        return template.format(**data)

    def generate(self, text):
        self.body_filled = """<body>"""

        for sent in text.Sentences:
            data_set = {}
            data_set["text"] = sent.Text
            data_set["feature1"] = sent.sent_len
            data_set["feature2"] = sent.avg_word_len
            data_set["feature3"] = sent.voc_complexity
            data_set["feature4"] = sent.depth
            data_set["feature5"] = sent.nominals

            self.body_filled += self.fill_template(self.body, data_set)

        self.body_filled += """</body>"""

        self.full = """<html>""" + self.header + self.body_filled + """</html>"""

        with open("generated_html/index.html", "w") as file:
            file.write(self.full)
             

class CSSGenerator(object):

    css_template = """
.column.xs-one.feature-1 {feature1}

.column.xs-one.feature-2 {feature2}

.column.xs-one.feature-3 {feature3}

.column.xs-one.feature-4 {feature4}

.column.xs-one.feature-5 {feature5}
"""

    def __init__(self):
        self.sample_data = {
            "feature1": "{background-color: rgb(255, 0, 0); color: rgb(255, 0, 0);}",
            "feature2": "{background-color: rgb(200, 55, 0); color: rgb(200, 55, 0);}",
            "feature3": "{background-color: rgb(100, 155, 0); color: rgb(100, 155, 0);}",
            "feature4": "{background-color: rgb(55, 200, 0); color: rgb(55, 200, 0);}",
            "feature5": "{background-color: rgb(0, 255, 0); color: rgb(0, 255, 0);}",
        }

        self.full = self.css_template.format(**self.sample_data)

        with open("generated_html/style.css", "w") as file:
            file.write(self.full)

    def generate(self, text):
        data_set = {}
        data_set["feature1"] = sent.sent_len
        data_set["feature2"] = sent.avg_word_len
        data_set["feature3"] = sent.voc_complexity
        data_set["feature4"] = sent.depth
        data_set["feature5"] = sent.nominals
