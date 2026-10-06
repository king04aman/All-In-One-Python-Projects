#include "database.h"
#include <QSqlQuery>
#include <QSqlDatabase>
#include <QSqlError>
#include <QDebug>

Database::Database(){
    QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE");
    db.setDatabaseName("finance.db");

    if(!db.open()){
        qDebug() <<"database failed: " << db.lastError().text();
        return;
    }
}


void Database::addTransaction(QString category, QString tag, double amount){


}


double Database::getTotal(){
    query.exec(
        "SELECT SUM(amount) "
        "FROM transactions"
        );
    double total = 0;
    if (query.next()) {
        total = query.value(0).toDouble();

    }
    return total;

}

double Database::totalSpending(){
    query.exec(
        "SELECT SUM(amount) "
        "FROM transactions"
        );
    double total = 0;
    if (query.next()) {
        total = query.value(0).toDouble();

    }
    return total;

}
double Database::totalGiving(){
    query.exec(
        "SELECT SUM(amount) "
        "FROM transactions"
        );
    double total = 0;
    if (query.next()) {
        total = query.value(0).toDouble();

    }
    return total;

}
double Database::totalSaving(){
    query.exec(
        "SELECT SUM(amount) "
        "FROM transactions"
        );
    double total = 0;
    if (query.next()) {
        total = query.value(0).toDouble();

    }
    return total;

}


void Database::createTable(){

    query.exec(
        "CREATE TABLE transactions ("
           "id INTEGER PRImary KEY AUTOINCREMENT,"
           "category TEXT,"
           "tag TEXT,"
           "amount REAL"
           ")"
        );
}
