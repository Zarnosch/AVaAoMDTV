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
    barebone_document_css = """
.feature-block-${id} {
    width: 100px;
    height: 100px;
    float: left;
    background-color: ${color};
}
"""

    @staticmethod
    def generate_html(text):
        filled_txt = ""

        for sent in text.Sentences:
            data_set = {}
            data_set["id"] = sent.id
            data_set["text"] = sent.Text
            data_set["f1"] = sent.voc_complexity
            data_set["f2"] = sent.avg_word_len
            data_set["f3"] = sent.nominals
            data_set["f4"] = sent.sent_len
            data_set["f5"] = sent.depth

            filled_txt += Template(ViewGenerator.barebone_element).substitute(data_set)

        file = os.path.dirname(__file__)
        index_template = os.path.join(file, '../../generated_html/index_template.html')

        filled_template = ""
        with open(index_template, "r") as f:
            for line in f:
                filled_template += Template(line).substitute(fill_me=filled_txt)

        index = os.path.join(file, '../../generated_html/index.html')
        with open(index, "w") as f:
            f.write(filled_template)



    @staticmethod
    def generate_css(text):
        filled_style = ""

        for sent in text.Sentences:
            data_set = {}
            data_set["id"] = sent.id
            data_set["f1"] = GenScale.get_color(sent.voc_complexity)
            data_set["f2"] = GenScale.get_color(sent.avg_word_len)
            data_set["f3"] = GenScale.get_color(sent.nominals)
            data_set["f4"] = GenScale.get_color(sent.sent_len)
            data_set["f5"] = GenScale.get_color(sent.depth)

            filled_style += Template(ViewGenerator.barebone_css).substitute(data_set)

        file = os.path.dirname(__file__)
        style_template = os.path.join(file, '../../generated_html/style_template.css')

        filled_template = ""
        with open(style_template, "r") as f:
            for line in f:
                filled_template += Template(line).substitute(fill_me=filled_style)

        style = os.path.join(file, '../../generated_html/style.css')
        with open(style, "w") as f:
            f.write(filled_template)

    @staticmethod
    def generate_document_view(text, app):
        gen_html = ""
        gen_css = ""

        for sent in text.Sentences:
            gen_html += Template("""            <div class="feature-block-${id}"></div>\n""").substitute(id=sent.id)

            avg_color = 0
            active_count = 0
            if app.kompVokIsActive:
                avg_color += sent.voc_complexity * (app.kompVokWeight/100)
                active_count += 1;
            if app.wlengthIsActive:
                avg_color += sent.avg_word_len * (app.wlengthWeight/100)
                active_count += 1;
            if app.nomIsActive:
                avg_color += sent.nominals * (app.nomWeight/100)
                active_count += 1;
            if app.slenghtIsActive:
                avg_color += sent.sent_len * (app.slenghtWeight/100)
                active_count += 1;
            if app.kompSatzIsActive:
                avg_color += sent.depth * (app.kompSatzWeight/100)
                active_count += 1;

            if active_count > 0:
                avg_color /= active_count
            else:
                avg_color = 0.5

            gen_css += Template(ViewGenerator.barebone_document_css).substitute(id=sent.id, color=GenScale.get_color(avg_color))

        file = os.path.dirname(__file__)
        html_template = os.path.join(file, '../../generated_html/document_view_template.html')

        filled_template = ""
        with open(html_template, "r") as f:
            for line in f:
                filled_template += Template(line).substitute(html=gen_html)

        html = os.path.join(file, '../../generated_html/document_view.html')
        with open(html, "w") as f:
            f.write(filled_template)

        style = os.path.join(file, '../../generated_html/document_view.css')
        with open(style, "w") as f:
            f.write(gen_css)


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
#     stext = SampleText()
#
#     ViewGenerator.generate_document_view(stext)
