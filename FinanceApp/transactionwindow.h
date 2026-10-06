#ifndef TRANSACTIONWINDOW_H
#define TRANSACTIONWINDOW_H

#include <QDialog>

namespace Ui {
class transactionwindow;
}

class transactionwindow : public QDialog
{
    Q_OBJECT

public:
    explicit transactionwindow(QWidget *parent = nullptr);
    ~transactionwindow();

private:
    Ui::transactionwindow *ui;

private slots:
    void cancelbutton();
    void savebutton();

};

#endif // TRANSACTIONWINDOW_H
