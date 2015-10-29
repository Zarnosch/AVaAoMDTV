#ifndef OPENGLWIDGET_H
#define OPENGLWIDGET_H

#include <QGLWidget>

class OpenGLWidget : public QGLWidget
{
    Q_OBJECT //Dieses MAKRO ist PFLICHT! Nach Hinzufügen muss qmake nochmal gestartet werden

private:
    int m_R;
    int m_G;
    int m_B;

public:
   OpenGLWidget(QWidget* parent=0);
   ~OpenGLWidget();

protected:
   void initializeGL();
   void paintGL();
   //void resizeGL(int width, int height);

public slots:
    void SetRValue(int value);
    void SetGValue(int value);
    void SetBValue(int value);

private:
    void draw();
};

#endif // OPENGLWIDGET_H
