Summary: Plasma 5 user work in separate activities support files
Name: kactivities-workspace
Version: 5.5.0
Release: 1
License: GPLv2+
Group: Graphical desktop/KDE
Url: https://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/kactivities/%{name}-%{version}.tar.xz
# These QML imports are in KF kactivities package
Patch0: kactivities-workspace-5.5.0-exclude-qml-imports.patch
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Activities) >= 5.20.0
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: boost-devel
# This package was split from KF kactivities since KF 5.20
Conflicts:	kactivities < 5.20

%description
Plasma 5 user work in separate activities support files.

KActivities provides the infrastructure needed to manage a user's activites,
allowing them to switch between tasks, and for applications to update their
state to match the user's current activity. This includes a daemon, a library
for interacting with that daemon, and plugins for integration with other
frameworks.

%files
%{_qt5_plugindir}/kio_activities.so
#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
