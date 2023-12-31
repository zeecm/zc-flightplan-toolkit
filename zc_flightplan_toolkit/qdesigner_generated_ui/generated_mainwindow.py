# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QGraphicsView,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLayout,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTableView,
    QTabWidget,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from zc_flightplan_toolkit.gui_classes import CustomQTableView


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1455, 930)
        self.toolbar_preferences_button = QAction(mainWindow)
        self.toolbar_preferences_button.setObjectName("toolbar_preferences_button")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_tabs = QTabWidget(self.centralwidget)
        self.main_tabs.setObjectName("main_tabs")
        self.route_info_tab = QWidget()
        self.route_info_tab.setObjectName("route_info_tab")
        self.gridLayout_3 = QGridLayout(self.route_info_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.start_airport_label = QLabel(self.route_info_tab)
        self.start_airport_label.setObjectName("start_airport_label")

        self.horizontalLayout_2.addWidget(self.start_airport_label)

        self.start_airport_lineedit = QLineEdit(self.route_info_tab)
        self.start_airport_lineedit.setObjectName("start_airport_lineedit")

        self.horizontalLayout_2.addWidget(self.start_airport_lineedit)

        self.end_airport_label = QLabel(self.route_info_tab)
        self.end_airport_label.setObjectName("end_airport_label")

        self.horizontalLayout_2.addWidget(self.end_airport_label)

        self.end_airport_lineedit = QLineEdit(self.route_info_tab)
        self.end_airport_lineedit.setObjectName("end_airport_lineedit")

        self.horizontalLayout_2.addWidget(self.end_airport_lineedit)

        self.get_route_info_button = QPushButton(self.route_info_tab)
        self.get_route_info_button.setObjectName("get_route_info_button")
        self.get_route_info_button.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.get_route_info_button)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.route_info_table = QTableView(self.route_info_tab)
        self.route_info_table.setObjectName("route_info_table")
        self.route_info_table.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.route_info_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.route_info_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.route_info_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.route_info_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_2.addWidget(self.route_info_table)

        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.main_tabs.addTab(self.route_info_tab, "")
        self.airport_info_tab = QWidget()
        self.airport_info_tab.setObjectName("airport_info_tab")
        self.gridLayout = QGridLayout(self.airport_info_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.decoded_metar_table = QTableView(self.airport_info_tab)
        self.decoded_metar_table.setObjectName("decoded_metar_table")
        self.decoded_metar_table.setMaximumSize(QSize(16777215, 500))
        self.decoded_metar_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.decoded_metar_table.setHorizontalScrollMode(
            QAbstractItemView.ScrollPerPixel
        )
        self.decoded_metar_table.horizontalHeader().setVisible(False)

        self.gridLayout_8.addWidget(self.decoded_metar_table, 14, 3, 1, 1)

        self.metar_label = QLabel(self.airport_info_tab)
        self.metar_label.setObjectName("metar_label")

        self.gridLayout_8.addWidget(self.metar_label, 11, 3, 1, 1)

        self.runway_info_label = QLabel(self.airport_info_tab)
        self.runway_info_label.setObjectName("runway_info_label")

        self.gridLayout_8.addWidget(self.runway_info_label, 2, 0, 1, 2)

        self.airport_info_table = QTableView(self.airport_info_tab)
        self.airport_info_table.setObjectName("airport_info_table")
        self.airport_info_table.setMaximumSize(QSize(16777215, 100))
        self.airport_info_table.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.airport_info_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.airport_info_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.airport_info_table.setHorizontalScrollMode(
            QAbstractItemView.ScrollPerPixel
        )

        self.gridLayout_8.addWidget(self.airport_info_table, 1, 0, 1, 4)

        self.map_label = QLabel(self.airport_info_tab)
        self.map_label.setObjectName("map_label")

        self.gridLayout_8.addWidget(self.map_label, 2, 3, 1, 1)

        self.metar_display = QTextBrowser(self.airport_info_tab)
        self.metar_display.setObjectName("metar_display")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.metar_display.sizePolicy().hasHeightForWidth()
        )
        self.metar_display.setSizePolicy(sizePolicy)
        self.metar_display.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_8.addWidget(self.metar_display, 12, 3, 1, 1)

        self.runway_info_table = CustomQTableView(self.airport_info_tab)
        self.runway_info_table.setObjectName("runway_info_table")
        self.runway_info_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.runway_info_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.runway_info_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.runway_info_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout_8.addWidget(self.runway_info_table, 10, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.enter_airport_id_label = QLabel(self.airport_info_tab)
        self.enter_airport_id_label.setObjectName("enter_airport_id_label")

        self.horizontalLayout.addWidget(self.enter_airport_id_label)

        self.airport_id_lineedit = QLineEdit(self.airport_info_tab)
        self.airport_id_lineedit.setObjectName("airport_id_lineedit")

        self.horizontalLayout.addWidget(self.airport_id_lineedit)

        self.get_airport_info_button = QPushButton(self.airport_info_tab)
        self.get_airport_info_button.setObjectName("get_airport_info_button")
        self.get_airport_info_button.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.get_airport_info_button)

        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.runway_map_view = QGraphicsView(self.airport_info_tab)
        self.runway_map_view.setObjectName("runway_map_view")
        sizePolicy.setHeightForWidth(
            self.runway_map_view.sizePolicy().hasHeightForWidth()
        )
        self.runway_map_view.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.runway_map_view, 10, 3, 1, 1)

        self.datis_info_label = QLabel(self.airport_info_tab)
        self.datis_info_label.setObjectName("datis_info_label")

        self.gridLayout_8.addWidget(self.datis_info_label, 11, 0, 1, 2)

        self.label = QLabel(self.airport_info_tab)
        self.label.setObjectName("label")

        self.gridLayout_8.addWidget(self.label, 13, 3, 1, 1)

        self.atis_display = QTextBrowser(self.airport_info_tab)
        self.atis_display.setObjectName("atis_display")
        self.atis_display.setMinimumSize(QSize(0, 0))

        self.gridLayout_8.addWidget(self.atis_display, 12, 0, 3, 2)

        self.gridLayout.addLayout(self.gridLayout_8, 0, 1, 1, 1)

        self.main_tabs.addTab(self.airport_info_tab, "")
        self.tracks_information_tab = QWidget()
        self.tracks_information_tab.setObjectName("tracks_information_tab")
        self.gridLayout_5 = QGridLayout(self.tracks_information_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tracks_tabs = QTabWidget(self.tracks_information_tab)
        self.tracks_tabs.setObjectName("tracks_tabs")
        self.north_atlantic_tracks_tab = QWidget()
        self.north_atlantic_tracks_tab.setObjectName("north_atlantic_tracks_tab")
        self.gridLayout_6 = QGridLayout(self.north_atlantic_tracks_tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.get_north_atlantic_tracks_button = QPushButton(
            self.north_atlantic_tracks_tab
        )
        self.get_north_atlantic_tracks_button.setObjectName(
            "get_north_atlantic_tracks_button"
        )

        self.gridLayout_6.addWidget(self.get_north_atlantic_tracks_button, 0, 0, 1, 1)

        self.north_atlantic_text_display = QTextBrowser(self.north_atlantic_tracks_tab)
        self.north_atlantic_text_display.setObjectName("north_atlantic_text_display")

        self.gridLayout_6.addWidget(self.north_atlantic_text_display, 1, 0, 1, 1)

        self.tracks_tabs.addTab(self.north_atlantic_tracks_tab, "")
        self.pacific_tracks_tab = QWidget()
        self.pacific_tracks_tab.setObjectName("pacific_tracks_tab")
        self.gridLayout_7 = QGridLayout(self.pacific_tracks_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.get_pacific_tracks_button = QPushButton(self.pacific_tracks_tab)
        self.get_pacific_tracks_button.setObjectName("get_pacific_tracks_button")

        self.gridLayout_7.addWidget(self.get_pacific_tracks_button, 0, 0, 1, 1)

        self.pacific_tracks_display = QTextBrowser(self.pacific_tracks_tab)
        self.pacific_tracks_display.setObjectName("pacific_tracks_display")

        self.gridLayout_7.addWidget(self.pacific_tracks_display, 1, 0, 1, 1)

        self.tracks_tabs.addTab(self.pacific_tracks_tab, "")

        self.gridLayout_4.addWidget(self.tracks_tabs, 0, 0, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.main_tabs.addTab(self.tracks_information_tab, "")

        self.gridLayout_2.addWidget(self.main_tabs, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1455, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.toolbar_preferences_button)

        self.retranslateUi(mainWindow)

        self.main_tabs.setCurrentIndex(0)
        self.tracks_tabs.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(mainWindow)

    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(
            QCoreApplication.translate(
                "mainWindow", "ZhaoCong's Flight Planning Tool", None
            )
        )
        self.toolbar_preferences_button.setText(
            QCoreApplication.translate("mainWindow", "Preferences", None)
        )
        self.start_airport_label.setText(
            QCoreApplication.translate("mainWindow", "Start Airport ID:", None)
        )
        self.end_airport_label.setText(
            QCoreApplication.translate("mainWindow", "End Airport ID:", None)
        )
        self.get_route_info_button.setText(
            QCoreApplication.translate("mainWindow", "Get Route Info", None)
        )
        self.main_tabs.setTabText(
            self.main_tabs.indexOf(self.route_info_tab),
            QCoreApplication.translate("mainWindow", "Route Information", None),
        )
        self.metar_label.setText(
            QCoreApplication.translate("mainWindow", "METAR", None)
        )
        self.runway_info_label.setText(
            QCoreApplication.translate("mainWindow", "Runways", None)
        )
        self.map_label.setText(QCoreApplication.translate("mainWindow", "Map", None))
        self.enter_airport_id_label.setText(
            QCoreApplication.translate("mainWindow", "Enter Airport ID:", None)
        )
        self.get_airport_info_button.setText(
            QCoreApplication.translate("mainWindow", "Get Airport Info", None)
        )
        self.datis_info_label.setText(
            QCoreApplication.translate("mainWindow", "D-ATIS", None)
        )
        self.label.setText(
            QCoreApplication.translate("mainWindow", "Decoded METAR", None)
        )
        self.main_tabs.setTabText(
            self.main_tabs.indexOf(self.airport_info_tab),
            QCoreApplication.translate("mainWindow", "Airport Information", None),
        )
        self.get_north_atlantic_tracks_button.setText(
            QCoreApplication.translate(
                "mainWindow", "Fetch North Atlantic Tracks Data", None
            )
        )
        self.tracks_tabs.setTabText(
            self.tracks_tabs.indexOf(self.north_atlantic_tracks_tab),
            QCoreApplication.translate("mainWindow", "North Atlantic Tracks", None),
        )
        self.get_pacific_tracks_button.setText(
            QCoreApplication.translate("mainWindow", "Fetch Pacific Tracks Data", None)
        )
        self.tracks_tabs.setTabText(
            self.tracks_tabs.indexOf(self.pacific_tracks_tab),
            QCoreApplication.translate("mainWindow", "Pacific Tracks", None),
        )
        self.main_tabs.setTabText(
            self.main_tabs.indexOf(self.tracks_information_tab),
            QCoreApplication.translate("mainWindow", "Tracks Information", None),
        )
        self.menuFile.setTitle(QCoreApplication.translate("mainWindow", "File", None))

    # retranslateUi
