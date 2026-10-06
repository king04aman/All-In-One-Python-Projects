#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "transactionwindow.h"
#include <QtCharts/QChartView>
#include <QtCharts/QPieSeries>
#include <QtCharts/QChart>
#include <QMovie>
#include <QDebug>
#include <QPixmap>



MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->transactionButton, &QPushButton::clicked, this, &MainWindow::transactionbutton);
    //Display:
        // Title
        QPixmap balanceImage("C:/Users/wilso/CLionProjects/Personal Finance Tracker/Finance Dashboard FIles/FinanceApp/title.png");
        ui->giftitle->setPixmap(balanceImage);


        //Gif Label
        QMovie *movie = new QMovie("C:/Users/wilso/CLionProjects/Personal Finance Tracker/Finance Dashboard FIles/FinanceApp/f005.gif");

        ui->giflabel->setMovie(movie);
        movie->setScaledSize(QSize(50, 50));
        ui->giflabel->setAlignment(Qt::AlignCenter);
        ui->giflabel->setMovie(movie);
        movie->start();


        //Category Table
        ui->categories_tableWidget->setRowCount(1);
        ui->categories_tableWidget->setColumnCount(3);
        ui->categories_tableWidget->setHorizontalHeaderLabels({"Category","Tag", "Amount"});

        ui->categories_tableWidget->setItem(0,0, new QTableWidgetItem("Eden's Mission Trip"));
        ui->categories_tableWidget->setItem(0,1, new QTableWidgetItem("Giving"));
        ui->categories_tableWidget->setItem(0,2, new QTableWidgetItem("$40"));
        ui->categories_tableWidget->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);


        //Income Pie Chart
        QPieSeries *series = new QPieSeries();

        series->append("Spending", 40);
        series->append("Giving", 20);
        series->append("Saving", 15);

        QChart *chart = new QChart();

        chart->addSeries(series);
        chart->setTitle("Money Allocation");


        ui->income_tableView->setChart(chart);
}






//Functions
void MainWindow::transactionbutton(){
    transactionwindow *window = new transactionwindow(this);
    window->show();
}



MainWindow::~MainWindow()
{
    delete ui;
}

