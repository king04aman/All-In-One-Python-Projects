cmake_minimum_required(VERSION 3.19)

project(FinanceApp LANGUAGES CXX)


find_package(Qt6 6.5 REQUIRED COMPONENTS Core Widgets Charts)
find_package(Qt6 6.5 REQUIRED COMPONENTS Core Widgets Charts Sql)

qt_standard_project_setup()

qt_add_executable(FinanceApp
    WIN32 MACOSX_BUNDLE
    main.cpp
    mainwindow.cpp
    mainwindow.h
    mainwindow.ui
    transactionwindow.h transactionwindow.cpp transactionwindow.ui
    database.cpp
    database.h


)

target_link_libraries(FinanceApp
    PRIVATE
        Qt6::Core
        Qt6::Widgets
        Qt6::Charts
        Qt6::Sql
)

include(GNUInstallDirs)

install(TARGETS FinanceApp
    BUNDLE DESTINATION .
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)