#
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
#

Name:       harbour-hydrogen

# >> macros
%define zipversion sfos-v0.5.1
# << macros

Summary:    hydrogen, a matrix client
Version:    0.5.1
Release:    2
Group:      Qt/Qt
License:    ASL 2.0
BuildArch:  noarch
URL:        https://github.com/hydrogen-sailfishos/harbour-hydrogen
Source0:    %{name}-%{version}.tar.bz2
Source1:    https://github.com/hydrogen-sailfishos/hydrogen-web/releases/download/%{zipversion}/hydrogen-web-%{zipversion}.tar.gz
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   libsailfishapp-launcher
Requires:   sailfish-components-webview-qt5
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.3
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(qt5embedwidget)
BuildRequires:  pkgconfig(sailfishwebengine)
BuildRequires:  sailfish-svg2png
BuildRequires:  desktop-file-utils

%description
Hydrogen is "A minimal Matrix chat client, focused on performance, offline
functionality, and broad browser support"

This App packages Hydrogen matrix client in a webview + SailfishOS integration.

%if 0%{?_chum}
Title: Hydrogen
Type: desktop-application
Categories:
 - InstantMessaging
 - Network
Custom:
  Repo: https://github.com/hydrogen-sailfishos/harbour-hydrogen
PackageIcon: https://raw.githubusercontent.com/hydrogen-sailfishos/harbour-hydrogen/hackathon/icons/svgs/harbour-hydrogen.svg
Links:
  Homepage: https://github.com/hydrogen-sailfishos/harbour-hydrogen
  Bugtracker: https://github.com/hydrogen-sailfishos/harbour-hydrogen/issues
  Hackathon: https://github.com/orgs/hydrogen-sailfishos/projects/1/
%endif

%prep
%setup -q -n %{name}-%{version}
%if 0%{?sailfishos_version}
# add release version to QML app
sed -i "s/unreleased/%{version}/" qml/pages/AppSettingsPage.qml
if [ ! -f %{SOURCE1} ]
then
  echo "Missing %{SOURCE1}"
  exit 1
fi
# we use hydrogen/target because locally fetching hydrogen-web in that folder builds it there
mkdir -p hydrogen/target

# but this is the pre-built web app from github
tar -C hydrogen/target -xvzf %{SOURCE1}

# create config from sample
if [ ! -f hydrogen/target/config.json ]
then
    mv hydrogen/target/config.sample.json hydrogen/target/config.json
fi
%endif

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/%{name}-open-url.desktop

%files
%defattr(-,root,root,-)
%defattr(0644,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/applications/%{name}-open-url.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
# >> files
# << files

%changelog
