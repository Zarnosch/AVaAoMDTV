#from textparser.textutil.structures import *
from string import Template
import os

class ViewGenerator(object):

    barebone_element = """<tr>
                    <td class="feature-text text-${id}">${text}</td>
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
    color: ${f1};
}
.feature-body.f2-${id} {
    background-color: ${f2};
    color: ${f2};
}
.feature-body.f3-${id} {
    background-color: ${f3};
    color: ${f3};
}
.feature-body.f4-${id} {
    background-color: ${f4};
    color: ${f4};
}
.feature-body.f5-${id} {
    background-color: ${f5};
    color: ${f5};
}
.feature-text.text-${id} {
    background-color: ${avg_color};
    padding: 5px;
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
    def generate_css(text, app):
        filled_style = ""

        for sent in text.Sentences:
            data_set = {}
            data_set["id"] = sent.id
            data_set["f1"] = GenScale.get_color(sent.voc_complexity, app)
            data_set["f2"] = GenScale.get_color(sent.avg_word_len, app)
            data_set["f3"] = GenScale.get_color(sent.nominals, app)
            data_set["f4"] = GenScale.get_color(sent.sent_len, app)
            data_set["f5"] = GenScale.get_color(sent.depth, app)
            data_set["avg_color"] = GenScale.get_color(GenScale.get_avg_color(sent, app, sliders=False), app)

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

            avg_color = GenScale.get_avg_color(sent, app)

            gen_css += Template(ViewGenerator.barebone_document_css).substitute(id=sent.id, color=GenScale.get_color(avg_color, app))

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

    color_scale_template = "rgb(${r}, ${g}, ${b})" #"hsl(228, 50%, ${blue}%)" "hsl(8, 70%, ${red}%)"

    """Returns a string containing the css rgb() color for the given value."""
    @staticmethod
    def get_color(value, app):
        color_filled = ""
        if value < 0.5:
            nv = 2*value
            red_percent = round((1-nv) * app.bestColor.red() + nv * app.neutralColor.red())
            green_percent = round((1-nv) * app.bestColor.green() + nv * app.neutralColor.green())
            blue_percent = round((1-nv) * app.bestColor.blue() + nv * app.neutralColor.blue())
            color_filled = Template(GenScale.color_scale_template).substitute(r=red_percent, g=green_percent, b=blue_percent)
        else:
            nv = 2*(value-0.5)
            red_percent = round((1-nv) * app.neutralColor.red() + nv * app.worstColor.red())
            green_percent = round((1-nv) * app.neutralColor.green() + nv * app.worstColor.green())
            blue_percent = round((1-nv) * app.neutralColor.blue() + nv * app.worstColor.blue())
            color_filled = Template(GenScale.color_scale_template).substitute(r=red_percent, g=green_percent, b=blue_percent)

        return color_filled

    @staticmethod
    def get_avg_color(sent, app, sliders=True):
        avg_color = 0

        if app.kompVokIsActive:
            avg_color += sent.voc_complexity * ((app.kompVokWeight/100) if sliders else 1)
        if app.wlengthIsActive:
            avg_color += sent.avg_word_len * ((app.wlengthWeight/100) if sliders else 1)
        if app.nomIsActive:
            avg_color += sent.nominals * ((app.nomWeight/100) if sliders else 1)
        if app.slenghtIsActive:
            avg_color += sent.sent_len * ((app.slenghtWeight/100) if sliders else 1)
        if app.kompSatzIsActive:
            avg_color += sent.depth * ((app.kompSatzWeight/100) if sliders else 1)

        divider = ((app.kompVokWeight/100) + (app.wlengthWeight/100) + (app.nomWeight/100) + (app.slenghtWeight/100) + (app.kompSatzWeight/100)) if sliders else 5
        if divider > 0:
            avg_color /= divider
        else:
            avg_color = 0.5

        return avg_color
