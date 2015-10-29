#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QFileDialog>
#include <QMessageBox>
#include <QTextStream>

#include <iostream>
#include <fstream>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


//Diese Action wurde mit dem Designer erstellt,
//wie genau das intern funktioniert, kann ich nicht sagen,
//soweit bin ich mit QT5 dann doch noch nicht
void MainWindow::on_actionText_ffnen_triggered()
{
    //Datei öffnen Dialog
    QString fileName = QFileDialog::getOpenFileName(this, tr("Text öffnen"));

    //Entsprechende Datei versuchen lesend zu öffnen
    QFile file(fileName);
    if(!file.open(QIODevice::ReadOnly | QIODevice::Text))
    {
        //Gebe hier nun einen Fehler aus
        QMessageBox msgBox;
        msgBox.setText("Konnte Datei nicht öffnen!");
        msgBox.setIcon(QMessageBox::Critical);
        msgBox.setStandardButtons(QMessageBox::Ok);

        msgBox.exec();
    }

    QString data;

    //Den gesamten Text einlesen? Okay xD
    QTextStream in(&file);
    data = in.readAll();
    in.flush();

    file.close();

    //So ein Unfug geht? Interessant
    ui->plainTextEdit->setPlainText(data);
}
