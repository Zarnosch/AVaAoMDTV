#from textparser.textutil.structures import *
from string import Template
import os

class ViewGenerator(object):

    barebone_element = """<tr>
                    <td>${text}</td>
                    <td class="feature-body f1-${id}">${f1}</td>
                    <td class="feature-body f2-${id}">${f2}</td>
                    <td class="feature-body f3-${id}">${f3}</td>
                    <td class="feature-body f4-${id}">${f4}</td>
                    <td class="feature-body f5-${id}">${f5}</td>
                </tr>
                """

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

    @staticmethod
    def generate_html(text):
        filled_txt = ""

        for sent in text.Sentences:
            data_set = {}
            data_set["id"] = sent.id
            data_set["text"] = sent.Text
            data_set["f1"] = sent.sent_len
            data_set["f2"] = sent.avg_word_len
            data_set["f3"] = sent.voc_complexity
            data_set["f4"] = sent.depth
            data_set["f5"] = sent.nominals

            filled_txt += Template(ViewGenerator.barebone_element).substitute(data_set)

        filled_template = ""
        with open("../../generated_html/index_template.html", "r") as f:
            for line in f:
                filled_template += Template(line).substitute(fill_me=filled_txt)

        with open("../../generated_html/index.html", "w") as f:
            f.write(filled_template)



    @staticmethod
    def generate_css(text):
        filled_style = ""

        for sent in text.Sentences:
            data_set = {}
            data_set["id"] = sent.id
            data_set["f1"] = GenScale.get_color(sent.sent_len)
            data_set["f2"] = GenScale.get_color(sent.avg_word_len)
            data_set["f3"] = GenScale.get_color(sent.voc_complexity)
            data_set["f4"] = GenScale.get_color(sent.depth)
            data_set["f5"] = GenScale.get_color(sent.nominals)

            filled_style += Template(ViewGenerator.barebone_css).substitute(data_set)

        filled_template = ""
        with open("../../generated_html/style_template.css", "r") as f:
            for line in f:
                filled_template += Template(line).substitute(fill_me=filled_style)

        with open("../../generated_html/style.css", "w") as f:
            f.write(filled_template)

class GenScale(object):

    light_percent_min = 40
    light_percent_max = 100

    hsl_template_blue = "hsl(228, 50%, ${blue}%)"
    hsl_template_red = "hsl(8, 70%, ${red}%)"

    """Returns a string containing the css rgb() color for the given value."""
    @staticmethod
    def get_color(value):
        hsl_filled = ""
        if value < 0.5:
            nv = 2*value
            ligth_percent = (1-nv) * GenScale.light_percent_min + nv * GenScale.light_percent_max
            hsl_filled = Template(GenScale.hsl_template_blue).substitute(blue=ligth_percent)
        else:
            nv = 2*(value-0.5)
            ligth_percent = (1-nv) * GenScale.light_percent_max + nv * GenScale.light_percent_min
            hsl_filled = Template(GenScale.hsl_template_red).substitute(red=ligth_percent)

        return hsl_filled

# class SampleText(object):
#     def __init__(self):
#         self.Sentences = [SampleSent(0), SampleSent(1)]
#
#
# class SampleSent(object):
#     def __init__(self, id):
#         self.id = id
#         self.Text = "Construction started in 1963, and the freeway opened on December 18, 1970."
#         self.sent_len = 0
#         self.avg_word_len = 0.3
#         self.voc_complexity = 1
#         self.depth = 0.7
#         self.nominals = 0.5
#
# if __name__ == '__main__':
#
#     GenerateColorScale.get_color(0.33333)
#     stext = SampleText()
#
#     ViewGenerator.generate_css(stext)
#     ViewGenerator.generate_html(stext)
