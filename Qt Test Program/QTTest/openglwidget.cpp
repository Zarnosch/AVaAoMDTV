#include "openglwidget.h"

#include <QMessageBox>
#include <QtOpenGL>

OpenGLWidget::OpenGLWidget(QWidget *parent) :
    QGLWidget(QGLFormat(QGL::SampleBuffers), parent)
{
    m_R = 255;
    m_G = 255;
    m_B = 255;
}

OpenGLWidget::~OpenGLWidget()
{

}

void OpenGLWidget::initializeGL()
{

}

void OpenGLWidget::paintGL()
{
    draw();
}

void OpenGLWidget::draw()
{
    //glClearColor(m_R / 255.0f, m_G / 255.0f, m_B / 255.0f, 1.0f);
    //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
}

void OpenGLWidget::SetRValue(int value)
{
    m_R = value;

    updateGL();
}


void OpenGLWidget::SetGValue(int value)
{
    m_G = value;

    updateGL();
}

void OpenGLWidget::SetBValue(int value)
{
    m_B = value;

    updateGL();
}
