from PyQt5.QtCore import QObject, pyqtSlot

class JSBridge(QObject):

    def __init__(self, doc_widget, det_widget, app):
        super(JSBridge, self).__init__()
        self.doc_widget = doc_widget
        self.det_widget = det_widget
        self.app = app

    @pyqtSlot()
    def switch_to_detail(self):
        self.selected = self.doc_widget.page().mainFrame().findAllElements("*.selected")
        for elem in self.selected:
            id = elem.attribute("id", "0")
            self.highlight_detail(id)

        self.app.setActiveTabDetailView()

    def highlight_detail(self, id):
        # cleanup
        clean_sel = self.det_widget.page().mainFrame().findAllElements(".feature-text")
        for elem in clean_sel:
            elem.setStyleProperty("border", "")

        self.selection = self.det_widget.page().mainFrame().findAllElements(".feature-text.text-" + id)
        for elem in self.selection:
            elem.setStyleProperty("border", "dashed 2px red")
            elem.evaluateJavaScript("this.scrollIntoView({behavior: 'smooth', block: 'start'});")
