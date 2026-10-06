#include "transactionwindow.h"
#include "ui_transactionwindow.h"
#include <QMovie>

transactionwindow::transactionwindow(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::transactionwindow)
{
    ui->setupUi(this);
    connect(ui->saveButton, &QPushButton::clicked, this, &transactionwindow::savebutton);
    connect(ui->cancelButton, &QPushButton::clicked, this, &transactionwindow::cancelbutton);
    //Gif Label
    QMovie *movie = new QMovie("C:/Users/wilso/CLionProjects/Personal Finance Tracker/Finance Dashboard FIles/FinanceApp/transactiontitle.gif");

    ui->tgiflabel->setMovie(movie);
    movie->setScaledSize(QSize(371, 71));
    ui->tgiflabel->setAlignment(Qt::AlignCenter);
    ui->tgiflabel->setMovie(movie);
    movie->start();

}

void transactionwindow::cancelbutton(){
    this->close();
}
void transactionwindow::savebutton(){
    //backend saving
    this->close();
}

transactionwindow::~transactionwindow()
{
    delete ui;
}
