#ifndef DATABASE_H
#define DATABASE_H
#include <QSqlQuery>
#include <QString>

class Database{
    public:
        QSqlQuery query;
        Database();
        void createTable();
        void addTransaction(QString category, QString tag, double amount);
        double getTotal();
        double totalSpending();
        double totalGiving();
        double totalSaving();

};





#endif // DATABASE_H
