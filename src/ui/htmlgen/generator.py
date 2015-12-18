from textparser.textutil.structures import *
from string import Template
import os

class HTMLGenerator(object):

    barebone_element = """<tr>
                    <td>${text}</td>
                    <td class="feature-body f1-${id}">${f1}</td>
                    <td class="feature-body f2-${id}">${f2}</td>
                    <td class="feature-body f3-${id}">${f3}</td>
                    <td class="feature-body f4-${id}">${f4}</td>
                    <td class="feature-body f5-${id}">${f5}</td>
                </tr>
                """

    def generate(self, text):
        self.filled_txt = ""

        for sent in text.Sentences:
            data_set = {}
            data_set["id"] = sent.id
            data_set["text"] = sent.Text
            data_set["f1"] = sent.sent_len
            data_set["f2"] = sent.avg_word_len
            data_set["f3"] = sent.voc_complexity
            data_set["f4"] = sent.depth
            data_set["f5"] = sent.nominals

            self.filled_txt += Template(self.barebone_element).substitute(data_set)

        self.filled_template = ""
        with open("../../generated_html/index_template.html", "r") as f:
            for line in f:
                self.filled_template += Template(line).substitute(fill_me=self.filled_txt)

        with open("../../generated_html/index.html", "w") as f:
            f.write(self.filled_template)


class CSSGenerator(object):

    barebone_css = """
.feature-body.f1-${id} {
    background-color: ${f1};
}
.feature-body.f2-${id} {
    background-color: ${f2};
}
.feature-body.f3-${id} {
    background-color: ${f3};
}
.feature-body.f4-${id} {
    background-color: ${f4};
}
.feature-body.f5-${id} {
    background-color: ${f5};
}
"""

    def generate(self, text):
        self.filled_style = ""

        for sent in text.Sentences:
            data_set = {}
            data_set["id"] = sent.id
            data_set["f1"] = "red"#sent.sent_len
            data_set["f2"] = "green"#sent.avg_word_len
            data_set["f3"] = "blue"#sent.voc_complexity
            data_set["f4"] = "yellow"#sent.depth
            data_set["f5"] = "pink"#sent.nominals

            self.filled_style += Template(self.barebone_css).substitute(data_set)

        self.filled_template = ""
        with open("../../generated_html/style_template.css", "r") as f:
            for line in f:
                self.filled_template += Template(line).substitute(fill_me=self.filled_style)

        with open("../../generated_html/style.css", "w") as f:
            f.write(self.filled_template)

# class SampleText(object):
#     def __init__(self):
#         self.Sentences = [SampleSent(0), SampleSent(1)]
#
#
# class SampleSent(object):
#     def __init__(self, id):
#         self.id = id
#         self.Text = "Construction started in 1963, and the freeway opened on December 18, 1970."
#         self.sent_len = 0.5
#         self.avg_word_len = 0.3
#         self.voc_complexity = 0.9
#         self.depth = 0.2
#         self.nominals = 0.4
#
# if __name__ == '__main__':
#     htmlgen = HTMLGenerator()
#     cssgen = CSSGenerator()
#     text = SampleText()
#
#     htmlgen.generate(text)
#     cssgen.generate(text)
